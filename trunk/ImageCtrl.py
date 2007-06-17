import wx
from wx.lib.scrolledpanel import *
from math import *

import Cmds
from Cmds.ShapeCmds import *
from Cmds.PathCmds import *
from Cmds.TransformCmds import *
from Cmds.ColorCmds import *
from Cmds.TextCmds import *
from Cmds.ImageCmds import *
from Cmds.UtilityCmds import *

DEF_IMAGE_WIDTH = 512
DEF_IMAGE_HEIGHT = 512

WIDTH = DEF_IMAGE_WIDTH
HEIGHT = DEF_IMAGE_HEIGHT

# class that draw image to itself
class DrawCtrl(wx.Panel):
	def __init__(self, parent, size=(640, 480)):
		wx.Panel.__init__(self, parent, wx.ID_ANY, size=size, style=wx.SIMPLE_BORDER)
		self.parent = parent
		self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.Bind(wx.EVT_SIZE, self.OnSize)
		
	def OnSize(self, evt):
		global WIDTH, HEIGHT
		
		if self.GetSize() != evt.GetSize():
			w, h = evt.GetSize()
			# set current size, min size and max size
			# it is necessary to make sizers work properly
			self.SetMinSize(evt.GetSize())
			self.SetMaxSize(evt.GetSize())
			self.SetSize(evt.GetSize())
			self.parent.canvas.Destroy()
			self.parent.canvas = wx.EmptyBitmap(w, h)
			self.parent.SetupScrolling()
			WIDTH = w
			HEIGHT = h
		
	def OnPaint(self, evt):
		parent = self.parent
		paintDC = wx.PaintDC(self)
		paintDC.Clear()
		memoryDC = wx.MemoryDC(parent.GetCanvas())
		parent.gc = gc = wx.GraphicsContext.Create(memoryDC)
		# set font
		gc.SetFont(parent.GetFont())
		# set transform matrix
		mat = gc.CreateMatrix()
		if parent.transform == None:
			parent.transform = mat.Get()
		else:
			a,b,c,d,tx,ty = parent.transform
			mat.Set(a,b,c,d,tx,ty)
		gc.SetTransform(mat)
		gc.SetBrush(parent.GetBrush())
		gc.SetPen(parent.GetPen())
		
		if parent.rendering == True:
			memoryDC.Clear()
			exec(parent.script)
		
		# save transform matrix
		mat = gc.GetTransform()
		parent.transform = mat.Get()
		# draw generated bitmap to window
		paintDC.DrawBitmap(parent.GetCanvas(), 0, 0)

# class that presents image to us
class ImageCtrl(ScrolledPanel):
	def __init__(self, parent):
		ScrolledPanel.__init__(self, parent, wx.ID_ANY)
		
		# create rendering surface and clear it
		self.canvas = wx.EmptyBitmap(DEF_IMAGE_WIDTH, DEF_IMAGE_HEIGHT)
		memoryDC = wx.MemoryDC(self.canvas)
		memoryDC.Clear()
		# this is the drawing widget
		self.drawCtrl = DrawCtrl(self, (DEF_IMAGE_WIDTH, DEF_IMAGE_HEIGHT))
		self.sizer = wx.BoxSizer(wx.HORIZONTAL)
		self.sizer.Add(self.drawCtrl)
		self.SetSizer(self.sizer)
		self.SetAutoLayout(1)
		self.SetupScrolling()
		
		self.rendering = False
		self.gc = None
		self.brush = wx.Brush(wx.Colour(0,0,0,255), wx.SOLID)
		self.pen = wx.Pen(wx.Colour(0,0,0,255), 1.0, wx.SOLID)
		self.font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
		self.colorMode = RGB
		self.colorRange = 1.0
		self.loadedImages = {}
		self.transform = None
		self.i = 0
		
	def LoadImage(self, path):
		imLoaded = False
		if path in self.loadedImages:
			imLoaded = True
		
		im = None
		if imLoaded == False:
			im = wx.Image(path)
			if not im.HasAlpha():
				im.InitAlpha()
			self.loadedImages[path] = im
		else:
			im = self.loadedImages[path]
		return im
		
	def GetColorMode(self):
		return self.colorMode
	
	def SetColorMode(self, cm):
		self.colorMode = cm
		
	def GetColorRange(self):
		return self.colorRange
	
	def SetColorRange(self, cr):
		self.colorRange = cr
	
	def GetGraphicsContext(self):
		return self.gc
	
	def GetCanvas(self):
		return self.canvas
	
	def SaveCanvas(self, name, type):
		self.canvas.SaveFile(name, type)
		
	def GetBrush(self):
		return self.brush
	
	def GetPen(self):
		return self.pen
	
	def GetFont(self):
		return self.font
	
	def ResizeCanvas(self, width, height):
		size = wx.Size(width, height)
		evt = wx.SizeEvent(size)
		self.drawCtrl.AddPendingEvent(evt)
		
	def EnableRendering(self, flag):
		self.rendering = flag
		
	def SetScript(self, script):
		self.script = script
		