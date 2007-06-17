import wx

# All helper functions must go here

# Remaps x from 0.0 .. __currentRange range to 0 .. 255.
def remapColourValue(x):
	wnd = wx.GetApp().GetTopWindow()
	ic = wnd.GetImageCtrl()
	
	fx = x/float(ic.GetColorRange())	# now it in 0.0 .. 1.0 range
	fx = int(fx*255)	# now it in 0 .. 255 range, 
	return fx		# so we can pass it to wx.Colour

# Converts CMYK value to RGB value.
# Returns ready to use wx.Colour value.
def convertCMYK2RGB(x, y=None, z=None, u=None, v=None):
	wnd = wx.GetApp().GetTopWindow()
	ic = wnd.GetImageCtrl()
	cr = ic.GetColorRange()
	
	# alpha ready to use
	a = remapColourValue(ic.GetColorRange())	# max value for alpha
	if v != None:
		a = remapColourValue(v)
	# c, m, y, k values are in 0.0 .. 1.0 range
	c = float(x/cr)
	m = float(y/cr)
	y = float(z/cr)
	k = float(u/cr)
	# converting
	r = int((1 - c) * (1 - k) * 255)
	g = int((1 - m) * (1 - k) * 255)
	b = int((1 - y) * (1 - k) * 255)
	return wx.Colour(r, g, b, a)
