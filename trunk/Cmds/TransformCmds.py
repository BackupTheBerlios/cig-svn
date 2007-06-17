import wx
import math

# transform modes
CENTER = 0
CORNER = 1

# TODO:
#	- implement transform(), skew()
#	- modify all funcs to support transform()

def transform(mode=CENTER):
	pass

def translate(x, y):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	gc.Translate(x, y)

def rotate(angle):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	gc.Rotate(math.radians(angle))

def scale(x, y=None):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	if y == None:
		y = x
	gc.Scale(x, y)

def skew(x, y=None):
	pass

def push():
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	gc.PushState()

def pop():
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	gc.PopState()

def reset():
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	identMat = gc.CreateMatrix()
	gc.SetTransform(identMat)
