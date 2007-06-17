import wx
import colorsys
from types import *
from CigDefs import *
from SupportFuncs import *

# TODO:
# - implement background()

def colormode(mode, rng=1.0):
	wnd = wx.GetApp().GetTopWindow()
	ic = wnd.GetImageCtrl()
	
	ic.SetColorMode(mode)
	ic.SetColorRange(rng)
	return mode

def color(x, y=None, z=None, u=None, v=None):
	wnd = wx.GetApp().GetTopWindow()
	ic = wnd.GetImageCtrl()
	cm = ic.GetColorMode()
	
	# if we have only one (or two) param(s)
	if z == None and u == None and v == None:
		# then construct gray-scale color
		colour = remapColourValue(x)
		a = remapColourValue(ic.GetColorRange())	# max value for alpha
		if y != None:
			a = remapColourValue(y)
		return wx.Colour(colour, colour, colour, a)
	
	# if we are in RGB mode then we need 3 (or 4 with alpha) params
	if cm == RGB:
		r = remapColourValue(x)
		g = remapColourValue(y)
		b = remapColourValue(z)
		a = remapColourValue(ic.GetColorRange())	# max value for alpha
		if u != None:
			a = remapColourValue(u)
		return wx.Colour(r, g, b, a)
	
	# if we are in HSB mode then we need 3 (or 4 with alpha) params
	if cm == HSB:
		# normalize values
		h = x/float(ic.GetColorRange())
		s = y/float(ic.GetColorRange())
		b = z/float(ic.GetColorRange())
		a = remapColourValue(ic.GetColorRange())	# max value for alpha
		if u != None:
			a = remapColourValue(u)
		# convert from HSB to RGB
		r, g, b = colorsys.hsv_to_rgb(h, s, b)
		# remap to 0..255
		r = remapColourValue(r)
		g = remapColourValue(g)
		b = remapColourValue(b)
		return wx.Colour(r, g, b, a)
		
	# if we are in CMYK mode then call convertCMYK2RGB
	if cm == CMYK:
		return convertCMYK2RGB(x,y,z,u,v)

# Sets fill color.
def fill(x, y=None, z=None, u=None, v=None):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	brush = wnd.GetImageCtrl().GetBrush()
	
	#if x is not wx.Colour:
		#clr = color(x, y, z, u, v)
	#else:
		#clr = x
		
	if type(x) !=  type(wx.Colour()):
		clr = color(x, y, z, u, v)
	else:
		clr = x
		
	brush.SetColour(clr)
	brush.SetStyle(wx.SOLID)
	gc.SetBrush(brush)
	return clr

# Sets transparent fill mode.
def nofill():
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	brush = wnd.GetImageCtrl().GetBrush()
	
	brush.SetStyle(wx.TRANSPARENT)
	gc.SetBrush(brush)

# Sets stroke color.
def stroke(x, y=None, z=None, u=None, v=None):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	pen = wnd.GetImageCtrl().GetPen()
	clr = None
	
	if type(x) !=  type(wx.Colour()):
		clr = color(x, y, z, u, v)
	else:
		clr = x
	pen.SetColour(clr)
	pen.SetStyle(wx.SOLID)
	gc.SetPen(pen)
	return clr

# Sets transparent stroke mode.
def nostroke():
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	pen = wnd.GetImageCtrl().GetPen()
	
	pen.SetStyle(wx.TRANSPARENT)
	gc.SetPen(pen)

# Sets stroke width.
def strokewidth(width):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	pen = wnd.GetImageCtrl().GetPen()
	
	pen.SetWidth(width)
	gc.SetPen(pen)
	return width

def background(x, y, z, u, v):
	pass
