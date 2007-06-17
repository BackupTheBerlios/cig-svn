#!/usr/bin/env python
import os
import wx

from CigDefs import *
from ToolBarCtrl import ToolBarCtrl
from ImageCtrl import ImageCtrl
from EditorCtrl import EditorCtrl

# TODO:
# - implement Handbook menu item

PROGRAM_NAME_FULL = 'Cool Image Generator'
PROGRAM_NAME = 'CIG'
PROGRAM_VERSION = '0.1'
PROGRAM_LICENSE = 'GPL v2'
PROGRAM_WEBSITE = 'http://cig.berlios.de/'

DEF_WIN_WIDTH = 800
DEF_WIN_HEIGHT = 600

class MainWindow(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, wx.ID_ANY, title, size=(DEF_WIN_WIDTH, DEF_WIN_HEIGHT))
		
		# setting up the 'File' menu
		fileMenu = wx.Menu()
		fileMenu.Append(ID_SAVE_IMAGE, "Save &Image...")
		fileMenu.AppendSeparator()
		fileMenu.Append(wx.ID_OPEN, "&Open Script...")
		fileMenu.Append(wx.ID_SAVE, "&Save Script")
		fileMenu.Append(wx.ID_SAVEAS, "Save Script &As...")
		fileMenu.AppendSeparator()
		fileMenu.Append(wx.ID_EXIT, "E&xit")

		# setting up the 'Edit' menu
		editMenu = wx.Menu()
		editMenu.Append(wx.ID_UNDO, "&Undo")
		editMenu.Append(wx.ID_REDO, "Re&do")
		editMenu.AppendSeparator()
		editMenu.Append(wx.ID_CUT, "Cu&t")
		editMenu.Append(wx.ID_COPY, "&Copy")
		editMenu.Append(wx.ID_PASTE, "&Paste")
		editMenu.AppendSeparator()
		editMenu.Append(wx.ID_SELECTALL, "Select &All")

		# setting up the 'Image' menu
		imageMenu = wx.Menu()
		imageMenu.AppendCheckItem(ID_RUN_SCRIPT, "&Run Script")

		# setting up the 'Help' menu
		helpMenu = wx.Menu()
		helpMenu.Append(wx.ID_HELP, "&Handbook")
		helpMenu.Append(wx.ID_ABOUT, "&About...")

		# creating the menubar
		self.menuBar = wx.MenuBar()
		self.menuBar.Append(fileMenu, "&File")
		self.menuBar.Append(editMenu, "&Edit")
		self.menuBar.Append(imageMenu, "&Image")
		self.menuBar.Append(helpMenu, "&Help")
		self.SetMenuBar(self.menuBar)
		
		# creating all necessary widgets
		self.toolBar = ToolBarCtrl(self)
		self.splitter = wx.SplitterWindow(self, style=wx.SP_LIVE_UPDATE)
		self.imageCtrl = ImageCtrl(self.splitter)
		self.editorCtrl = EditorCtrl(parent=self.splitter, eventRecevier=self)
		self.splitter.SetMinimumPaneSize(20)
		self.splitter.SetSashGravity(0.8)
		self.splitter.SplitVertically(self.imageCtrl, self.editorCtrl, -DEF_WIN_WIDTH/3)
		
		# use box sizer to set layout options
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.toolBar)
		self.sizer.Add(self.splitter, 1, wx.EXPAND)
		# layout sizers
		self.SetSizer(self.sizer)
		self.SetAutoLayout(1)
		self.Show(True)
		
		# set event handlers
		wx.EVT_MENU(self, ID_SAVE_IMAGE, self.OnSaveImage)
		wx.EVT_MENU(self, wx.ID_OPEN, self.OnOpenScript)
		wx.EVT_MENU(self, wx.ID_SAVE, self.OnSaveScript)
		wx.EVT_MENU(self, wx.ID_SAVEAS, self.OnSaveScriptAs)
		wx.EVT_MENU(self, wx.ID_EXIT, self.OnExit)
		wx.EVT_MENU(self, ID_RUN_SCRIPT, self.OnRunScript)
		wx.EVT_MENU(self, wx.ID_HELP, self.OnHandbook)
		wx.EVT_MENU(self, wx.ID_ABOUT, self.OnAbout)
		self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGED, self.OnSashChange)
		self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGING, self.OnSashChange)
		self.Bind(wx.EVT_MENU_OPEN, self.OnMenuOpen)
		self.Bind(wx.EVT_IDLE, self.OnIdle)
		
		# misc variables
		self.running = False
		self.filename = ""
		
	# Set/Get functions
	def GetImageCtrl(self):
		return self.imageCtrl
	
	def GetEditorCtrl(self):
		return self.editorCtrl

	# handers for 'File' menu
	def OnSaveImage(self, evt):
		types = "BMP files (*.bmp)|*.bmp"
		dlg = wx.FileDialog(self, "Choose an image file", "", "", types,
							wx.FD_SAVE or wx.FD_OVERWRITE_PROMPT)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetPath()
			self.imageCtrl.SaveCanvas(self.filename, wx.BITMAP_TYPE_BMP)
		dlg.Destroy()

	def OnOpenScript(self, evt):
		dlg = wx.FileDialog(self, "Choose a script file", "", "", "*.*", wx.FD_OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetPath()
			f = open(self.filename, 'r')
			self.editorCtrl.SetText(f.read())
			f.close()
		dlg.Destroy()

	def OnSaveScript(self, evt):
		if self.filename == "":
			self.OnSaveScriptAs(None)
		else:
			self.editorCtrl.SaveFile(self.filename)

	def OnSaveScriptAs(self, evt):
		dlg = wx.FileDialog(self, "Choose a script file", "", "", "*.*",
							wx.FD_SAVE or wx.FD_OVERWRITE_PROMPT)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetPath()
			self.editorCtrl.SaveFile(self.filename)
		dlg.Destroy()

	def OnExit(self, evt):
		self.Close(True)

	# handlers for 'Image' menu
	def OnRunScript(self, evt):
		if self.running == False:
			self.running = True
		else:
			self.running = False
		self.menuBar.Check(ID_RUN_SCRIPT, self.running)
		self.toolBar.ToggleTool(ID_RUN_SCRIPT, self.running)
		self.imageCtrl.SetScript(self.editorCtrl.GetText())
		self.imageCtrl.EnableRendering(self.running)
		self.Refresh()

	# handlers for 'Help' menu
	def OnHandbook(self, evt):
		msg = wx.MessageDialog(self, "NOT IMPLEMENTED", "CIG - Handbook", wx.OK)
		msg.ShowModal()

	def OnAbout(self, evt):
		info = wx.AboutDialogInfo()
		info.AddDeveloper("_XLaT_ (x86xlat at gmail.com)")
		info.SetCopyright("(CC) 2007")
		info.SetLicense(PROGRAM_LICENSE)
		info.SetDescription(PROGRAM_NAME_FULL)
		info.SetName(PROGRAM_NAME)
		info.SetVersion(PROGRAM_VERSION)
		info.SetWebSite(PROGRAM_WEBSITE)
		wx.AboutBox(info)

	def OnSashChange(self, evt):
		self.Refresh()
		
	def OnMenuOpen(self, evt):
		self.editorCtrl.UpdateAllMenuItems()
		
	def OnIdle(self, evt):
		if self.running == True:
			self.Refresh()

if __name__ == '__main__':
	app = wx.PySimpleApp()
	mainWindow = MainWindow(None, wx.ID_ANY, PROGRAM_NAME)
	app.SetTopWindow(mainWindow)
	app.MainLoop()
