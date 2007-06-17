import wx

# TODO:
# - fix findpath() func

__currentPath = None

def beginpath(x=None, y=None):
	global __currentPath
	if __currentPath != None:
		__currentPath.Destroy()
		__currentPath = None
	
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	__currentPath = gc.CreatePath()
	if x != None and y != None:
		__currentPath.MoveToPoint(x, y)

def moveto(x, y):
	global __currentPath
	if __currentPath == None:
		return
	
	__currentPath.MoveToPoint(x, y)

def lineto(x, y):
	global __currentPath
	if __currentPath == None:
		return
	
	__currentPath.AddLineToPoint(x, y)

def curveto(h1x, h1y, h2x, h2y, x, y):
	global __currentPath
	if __currentPath == None:
		return
	
	__currentPath.AddCurveToPoint(h1x, h1y, h2x, h2y, x, y)

def endpath(draw=True):
	global __currentPath
	if __currentPath == None:
		return None
	
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	path = gc.CreatePath()
	path.AddPath(__currentPath)
	__currentPath.Destroy()
	__currentPath = None
	if draw == True:
		drawpath(path)
	return path

def findpath(lst, curvature=1.0):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	path = gc.CreatePath()
	for x, y in lst:
		path.AddQuadCurveToPoint(0, 0, x, y)
	return path

def drawpath(path):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	gc.DrawPath(path)

def beginclip(path):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	gc.ClipRegion(path)
	
def endclip():
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	gc.ResetClip()
