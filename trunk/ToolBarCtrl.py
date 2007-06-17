import wx

from CigDefs import *

TOOLBAR_SIZE=32

class ToolBarCtrl(wx.ToolBar):
	def __init__(self, parent):
		wx.ToolBar.__init__(self, parent, wx.ID_ANY)

		# loading images
		#savePictImage = wx.ArtProvider.GetBitmap(wx.ART_FLOPPY, wx.ART_TOOLBAR,
		#	(TOOLBAR_SIZE, TOOLBAR_SIZE))
		openScriptImage = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR,
			(TOOLBAR_SIZE, TOOLBAR_SIZE))
		saveScriptImage = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR,
			(TOOLBAR_SIZE, TOOLBAR_SIZE))
		runScriptImage = wx.ArtProvider.GetBitmap(wx.ART_EXECUTABLE_FILE, wx.ART_TOOLBAR,
			(TOOLBAR_SIZE, TOOLBAR_SIZE))
		handbookImage = wx.ArtProvider.GetBitmap(wx.ART_HELP, wx.ART_TOOLBAR,
			(TOOLBAR_SIZE, TOOLBAR_SIZE))
		
		# adding all tools to toolbar
		#self.AddLabelTool(ID_TOOL_SAVE_PICT, "Save Picture", savePictImage,
		#	shortHelp="Save Picture")
		#self.AddSeparator()
		self.AddLabelTool(wx.ID_OPEN, "Open Script", openScriptImage,
			shortHelp="Open Script")
		self.AddLabelTool(wx.ID_SAVE, "Save Script", saveScriptImage,
			shortHelp="Save Script")
		self.AddSeparator()
		self.AddCheckLabelTool(ID_RUN_SCRIPT, "Run", runScriptImage,
			shortHelp="Run Script")
		self.AddSeparator()
		self.AddLabelTool(wx.ID_HELP, "Handbook", handbookImage,
			shortHelp="Handbook")
		
		self.Realize()