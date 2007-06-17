import wx

# Arrow styles
NORMAL = 0
FORTYFIVE = 1

# TODO:
# - implement arrow(), star() funcs

# Draws a rectangle.
# Returns a path containing the rectangle.
def rect(x, y, width, height, roundness=0.0, draw=True):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	path = gc.CreatePath()
	path.AddRoundedRectangle(x, y, width, height, roundness)
	if draw == True:
		gc.DrawPath(path)
	return path

# Draws an oval (ellipse).
# Returns a path containing the oval (ellipse).
def oval(x, y, width, height, draw=True):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	path = gc.CreatePath()
	path.AddEllipse(x, y, width, height)
	if draw == True:
		gc.DrawPath(path)
	return path

# Draws an circle.
# Returns a path containing the circle.
def circle(x, y, radius, draw=True):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	path = gc.CreatePath()
	path.AddCircle(x, y, radius)
	if draw == True:
		gc.DrawPath(path)
	return path
	
# Draws an arc.
# Returns a path containing the arc.
def arc(x, y, r, startAngle, endAngle, clockwise=True, draw=True):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	path = gc.CreatePath()
	path.AddArc(x, y, r, startAngle, endAngle, clockwise)
	if draw == True:
		gc.DrawPath(path)
	return path

# Draws a line.
# Returns a path containing the line.
def line(x1, y1, x2, y2, draw=True):
	wnd = wx.GetApp().GetTopWindow()
	gc = wnd.GetImageCtrl().GetGraphicsContext()
	path = gc.CreatePath()
	path.MoveToPoint(x1, y1)
	path.AddLineToPoint(x2, y2)
	if draw == True:
		gc.DrawPath(path)
	return path

# Draws an arrow.
# Returns a path containing the arrow.
def arrow(x, y, width, type=NORMAL, draw=True):
	pass

# Draws a star.
# Returns a path containing the star.
def star(x, y, points=20, outer=100, inner=50, draw=True):
	pass
