import wx
from CigDefs import *

# TODO:
# - fix text() funcs
# - implement lineheight(), align() and textpath() funcs

def font(fontname=None, fontsize=None):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	fnt = wnd.GetImageCtrl().GetFont()
	
	if fontname != None:
		fnt.SetFaceName(fontname)
	if fontsize != None:
		fnt.SetPointSize(fontsize)
	gc.SetFont(fnt)
	return fnt.GetFaceName()

def fontsize(fontsize=None):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	fnt = wnd.GetImageCtrl().GetFont()
	
	if fontsize != None:
		fnt.SetPointSize(fontsize)
	gc.SetFont(fnt)
	return fnt.GetPointSize()

def text(txt, x, y, width=None, height=None, outline=True):
	wnd = wx.GetApp().GetTopWindow()
	ic = wnd.GetImageCtrl()
	gc = ic.GetGraphicsContext()
	
	gc.DrawText(txt, x, y)
	return gc.GetTextExtent(txt)

def textpath(txt, x, y, width=None, height=None):
	pass

def textwidth(txt, width=None):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	w, h = gc.GetTextExtent(txt)
	
	return w

def textheight(txt, width=None):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	w, h = gc.GetTextExtent(txt)
	
	return h

def textmetrics(txt, width=None):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	return gc.GetTextExtent(txt)

def lineheight(height=None):
	pass

def align(align=LEFT):
	pass
