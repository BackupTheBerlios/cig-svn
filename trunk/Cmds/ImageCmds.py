import wx
from SupportFuncs import *

# TODO:
# - speed :)
# - create image from data param (if passed)

# it's terrible :(
def image(path, x, y, width=None, height=None, alpha=1.0, data=None):
	wnd = wx.GetApp().GetTopWindow()
	ic = wnd.GetImageCtrl()
	gc = ic.GetGraphicsContext()
	alpha = remapColourValue(alpha)
	im = ic.LoadImage(path)
	
	# especially this part
	if im.GetAlpha(0, 0) != alpha:
		for x in range(im.GetWidth()):
			for y in range(im.GetHeight()):
				im.SetAlpha(x, y, alpha)
	
	bitmap = im.ConvertToBitmap()
	gc.DrawBitmap(bitmap, x, y, width, height)

def imagesize(path):
	wnd = wx.GetApp().GetTopWindow()
	ic = wnd.GetImageCtrl()
	im = ic.LoadImage(path)
	return (im.GetWidth(), im.GetHeight())
