import wx
import random as Random
from types import *
import math
import glob

# TODO:
# - implement autotext(), var() funcs

# Resizes drawing canvas.
def size(width, height):
	wnd = wx.GetApp().GetTopWindow()
	wnd.GetImageCtrl().ResizeCanvas(width, height)

# Returns random value.
def random(p1=None, p2=None):
	Random.seed()
	
	if p1 == None:
		p1 = 0
		if p2 == None:
			p2 = 1.0
	else:
		if p2 == None:
			p2 = p1
			p1 = 0
	
	if (type(p1) is IntType) and (type(p2) is IntType):
		return Random.randint(p1, p2)
	
	return Random.uniform(p1, p2)

# Returns random list element.
def choice(lst):
	return Random.choice(lst)

# Create iteratable 2D object.
def grid(cols, rows, colsize=1, rowsize=1):
	for c in range(cols):
		for r in range(rows):
			x = c * colsize
			y = r * rowsize
			yield (x,y)

# Returns list of filenames in path.
def files(path):
	return glob.glob(path)

# Generate random text from XML file.
def autotext():
	pass

# Create connection betweem variable and widget.
def var(name, type, default, minimum, maximum):
	pass

# Some math functions...
# Rotates point and returns new coordinates.
def coordinates(x0, y0, distance, angle):
	angle = math.radians(angle)
	x1 = x0 + math.cos(angle) * distance
	y1 = y0 + math.sin(angle) * distance
	return x1, y1

# Calculates angle (in degrees) between two points.
def angle(x0, y0, x1, y1):
	return math.degrees(math.atan2(y1-y0, x1-x0))

# Calculates distance between two points.
def distance(x0, y0, x1, y1):
	return math.sqrt(math.pow(x1-x0, 2) + math.pow(y1-y0, 2))

# Calculates reflection of point through an origin point.
def reflect(x0, y0, x1, y1, d=1.0, a=180):
	d *= distance(x0, y0, x1, y1)
	a += angle(x0, y0, x1, y1)
	x, y = coordinates(x0, y0, d, a)
	return x, y

# Fibonacci sequence
def fib(n):
	if n == 0: return 0
	if n == 1: return 1
	if n >= 2: return fib(n-1) + fib(n-2)

# Calculates two proportional numbers whose sum is n.
def goldenratio(n, f=4):
	f = max(1, min(f, 10))
	n /= float(fib(f+2))
	return n*fib(f+1), n*fib(f)
