import wx
import keyword
from wx.stc import *

if wx.Platform == '__WXMSW__':
	faces = { 'times': 'Times New Roman',
			'mono' : 'Courier New',
			'helv' : 'Arial',
			'other': 'Comic Sans MS',
			'size' : 10,
			'size2': 8,
			}
elif wx.Platform == '__WXMAC__':
	faces = { 'times': 'Times New Roman',
			'mono' : 'Courier New',
			'helv' : 'Arial',
			'other': 'Comic Sans MS',
			'size' : 10,
			'size2': 8,
			}
else:
	faces = { 'times': 'Times',
			'mono' : 'Courier',
			'helv' : 'Helvetica',
			'other': 'new century schoolbook',
			'size' : 10,
			'size2': 8,
			}
			
class EditorCtrl(StyledTextCtrl):	
	def __init__(self, parent, eventRecevier, ID=wx.ID_ANY,
				pos=wx.DefaultPosition, size=wx.DefaultSize,
				style=0):
		StyledTextCtrl.__init__(self, parent, ID, pos, size, style)
		self.eventRecevier = eventRecevier
		
		#self.CmdKeyAssign(ord('B'), STC_SCMOD_CTRL, STC_CMD_ZOOMIN)
		#self.CmdKeyAssign(ord('N'), STC_SCMOD_CTRL, STC_CMD_ZOOMOUT)
		
		self.SetLexer(STC_LEX_PYTHON)
		self.SetKeyWords(0, " ".join(keyword.kwlist))
		
		self.SetProperty("fold", "1")
		self.SetProperty("tab.timmy.whinge.level", "1")
		self.SetMargins(0, 0)
		
		self.SetViewWhiteSpace(False)
		self.SetTabWidth(4)
		#self.SetBufferedDraw(False)
		#self.SetViewEOL(True)
		#self.SetEOLMode(STC_EOL_CRLF)
		#self.SetUseAntiAliasing(True)
		#self.SetScrollWidth(50)
		
		#self.SetEdgeMode(STC_EDGE_LINE)
		#self.SetEdgeColumn(78)
		
		# Setup a margin to hold line numbers
		self.SetMarginType(1, STC_MARGIN_NUMBER)
		self.SetMarginWidth(1, 25)
		
		# Setup a margin to hold fold markers
		self.SetMarginType(2, STC_MARGIN_SYMBOL)
		self.SetMarginMask(2, STC_MASK_FOLDERS)
		self.SetMarginSensitive(2, True)
		self.SetMarginWidth(2, 12)
		
		# Like a flattened tree control using circular headers and curved joins
		self.MarkerDefine(STC_MARKNUM_FOLDEROPEN, STC_MARK_CIRCLEMINUS, "white", "#404040")
		self.MarkerDefine(STC_MARKNUM_FOLDER, STC_MARK_CIRCLEPLUS, "white", "#404040")
		self.MarkerDefine(STC_MARKNUM_FOLDERSUB, STC_MARK_VLINE, "white", "#404040")
		self.MarkerDefine(STC_MARKNUM_FOLDERTAIL, STC_MARK_LCORNERCURVE, "white", "#404040")
		self.MarkerDefine(STC_MARKNUM_FOLDEREND, STC_MARK_CIRCLEPLUSCONNECTED, "white", "#404040")
		self.MarkerDefine(STC_MARKNUM_FOLDEROPENMID, STC_MARK_CIRCLEMINUSCONNECTED, "white", "#404040")
		self.MarkerDefine(STC_MARKNUM_FOLDERMIDTAIL, STC_MARK_TCORNERCURVE, "white", "#404040")
		
		self.Bind(EVT_STC_UPDATEUI, self.OnUpdateUI)
		self.Bind(EVT_STC_MARGINCLICK, self.OnMarginClick)
		
		# Global default styles for all languages
		self.StyleSetSpec(STC_STYLE_DEFAULT, "face:%(helv)s,size:%(size)d" % faces)
		self.StyleClearAll()  # Reset all to be like the default
		
		# Global default styles for all languages
		self.StyleSetSpec(STC_STYLE_DEFAULT, "face:%(helv)s,size:%(size)d" % faces)
		self.StyleSetSpec(STC_STYLE_LINENUMBER, "back:#C0C0C0,face:%(helv)s,size:%(size2)d" % faces)
		self.StyleSetSpec(STC_STYLE_CONTROLCHAR, "face:%(other)s" % faces)
		self.StyleSetSpec(STC_STYLE_BRACELIGHT, "fore:#FFFFFF,back:#0000FF,bold")
		self.StyleSetSpec(STC_STYLE_BRACEBAD, "fore:#000000,back:#FF0000,bold")
		
		# Python styles
		# Default 
		self.StyleSetSpec(STC_P_DEFAULT, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)
		# Comments
		self.StyleSetSpec(STC_P_COMMENTLINE, "fore:#007F00,face:%(other)s,size:%(size)d" % faces)
		# Number
		self.StyleSetSpec(STC_P_NUMBER, "fore:#007F7F,size:%(size)d" % faces)
		# String
		self.StyleSetSpec(STC_P_STRING, "fore:#7F007F,face:%(helv)s,size:%(size)d" % faces)
		# Single quoted string
		self.StyleSetSpec(STC_P_CHARACTER, "fore:#7F007F,face:%(helv)s,size:%(size)d" % faces)
		# Keyword
		self.StyleSetSpec(STC_P_WORD, "fore:#00007F,bold,size:%(size)d" % faces)
		# Triple quotes
		self.StyleSetSpec(STC_P_TRIPLE, "fore:#7F0000,size:%(size)d" % faces)
		# Triple double quotes
		self.StyleSetSpec(STC_P_TRIPLEDOUBLE, "fore:#7F0000,size:%(size)d" % faces)
		# Class name definition
		self.StyleSetSpec(STC_P_CLASSNAME, "fore:#0000FF,bold,underline,size:%(size)d" % faces)
		# Function or method name definition
		self.StyleSetSpec(STC_P_DEFNAME, "fore:#007F7F,bold,size:%(size)d" % faces)
		# Operators
		self.StyleSetSpec(STC_P_OPERATOR, "bold,size:%(size)d" % faces)
		# Identifiers
		self.StyleSetSpec(STC_P_IDENTIFIER, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)
		# Comment-blocks
		self.StyleSetSpec(STC_P_COMMENTBLOCK, "fore:#7F7F7F,size:%(size)d" % faces)
		# End of line where string is not closed
		self.StyleSetSpec(STC_P_STRINGEOL, "fore:#000000,face:%(mono)s,back:#E0C0E0,eol,size:%(size)d" % faces)
		
		self.SetCaretForeground("BLACK")
		
		# assign event handlers
		wx.EVT_MENU(eventRecevier, wx.ID_UNDO, self.OnUndo)
		wx.EVT_MENU(eventRecevier, wx.ID_REDO, self.OnRedo)
		wx.EVT_MENU(eventRecevier, wx.ID_CUT, self.OnCut)
		wx.EVT_MENU(eventRecevier, wx.ID_COPY, self.OnCopy)
		wx.EVT_MENU(eventRecevier, wx.ID_PASTE, self.OnPaste)
		wx.EVT_MENU(eventRecevier, wx.ID_SELECTALL, self.OnSelectAll)
		
	def OnUpdateUI(self, evt):
		# check for matching braces
		braceAtCaret = -1
		braceOpposite = -1
		charBefore = None
		caretPos = self.GetCurrentPos()

		if caretPos > 0:
			charBefore = self.GetCharAt(caretPos - 1)
			styleBefore = self.GetStyleAt(caretPos - 1)

		# check before
		if charBefore and chr(charBefore) in "[]{}()" and styleBefore == STC_P_OPERATOR:
			braceAtCaret = caretPos - 1

		# check after
		if braceAtCaret < 0:
			charAfter = self.GetCharAt(caretPos)
			styleAfter = self.GetStyleAt(caretPos)

			if charAfter and chr(charAfter) in "[]{}()" and styleAfter == STC_P_OPERATOR:
				braceAtCaret = caretPos

		if braceAtCaret >= 0:
			braceOpposite = self.BraceMatch(braceAtCaret)

		if braceAtCaret != -1  and braceOpposite == -1:
			self.BraceBadLight(braceAtCaret)
		else:
			self.BraceHighlight(braceAtCaret, braceOpposite)
		
	def OnMarginClick(self, evt):
		# fold and unfold as needed
		if evt.GetMargin() == 2:
			if evt.GetShift() and evt.GetControl():
				self.FoldAll()
			else:
				lineClicked = self.LineFromPosition(evt.GetPosition())

				if self.GetFoldLevel(lineClicked) & STC_FOLDLEVELHEADERFLAG:
					if evt.GetShift():
						self.SetFoldExpanded(lineClicked, True)
						self.Expand(lineClicked, True, True, 1)
					elif evt.GetControl():
						if self.GetFoldExpanded(lineClicked):
							self.SetFoldExpanded(lineClicked, False)
							self.Expand(lineClicked, False, True, 0)
						else:
							self.SetFoldExpanded(lineClicked, True)
							self.Expand(lineClicked, True, True, 100)
					else:
						self.ToggleFold(lineClicked)
		
	def FoldAll(self):
		lineCount = self.GetLineCount()
		expanding = True

		# find out if we are folding or unfolding
		for lineNum in range(lineCount):
			if self.GetFoldLevel(lineNum) & STC_FOLDLEVELHEADERFLAG:
				expanding = not self.GetFoldExpanded(lineNum)
				break

		lineNum = 0

		while lineNum < lineCount:
			level = self.GetFoldLevel(lineNum)
			if level & STC_FOLDLEVELHEADERFLAG and \
			(level & STC_FOLDLEVELNUMBERMASK) == STC_FOLDLEVELBASE:

				if expanding:
					self.SetFoldExpanded(lineNum, True)
					lineNum = self.Expand(lineNum, True)
					lineNum = lineNum - 1
				else:
					lastChild = self.GetLastChild(lineNum, -1)
					self.SetFoldExpanded(lineNum, False)

					if lastChild > lineNum:
						self.HideLines(lineNum+1, lastChild)

			lineNum = lineNum + 1
		
	def Expand(self, line, doExpand, force=False, visLevels=0, level=-1):
		lastChild = self.GetLastChild(line, level)
		line = line + 1

		while line <= lastChild:
			if force:
				if visLevels > 0:
					self.ShowLines(line, line)
				else:
					self.HideLines(line, line)
			else:
				if doExpand:
					self.ShowLines(line, line)

			if level == -1:
				level = self.GetFoldLevel(line)

			if level & STC_FOLDLEVELHEADERFLAG:
				if force:
					if visLevels > 1:
						self.SetFoldExpanded(line, True)
					else:
						self.SetFoldExpanded(line, False)

					line = self.Expand(line, doExpand, force, visLevels-1)

				else:
					if doExpand and self.GetFoldExpanded(line):
						line = self.Expand(line, True, force, visLevels-1)
					else:
						line = self.Expand(line, False, force, visLevels-1)
			else:
				line = line + 1

		return line

	# event handlers
	def OnUndo(self, evt):
		self.Undo()
		self.UpdateMenuItem(wx.ID_UNDO, self.CanUndo())
	
	def OnRedo(self, evt):
		self.Redo()
		self.UpdateMenuItem(wx.ID_REDO, self.CanRedo())
	
	def OnCut(self, evt):
		self.Cut()
	
	def OnCopy(self, evt):
		self.Copy()
	
	def OnPaste(self, evt):
		self.Paste()
	
	def OnSelectAll(self, evt):
		self.SelectAll()
		self.UpdateMenuItem(wx.ID_PASTE, self.CanPaste())
		
	# support functions
	def UpdateMenuItem(self, menuItemId, value):
		menuBar = self.eventRecevier.GetMenuBar()
		menuItem = menuBar.FindItemById(menuItemId)
		menuItem.Enable(value)
		
	def UpdateAllMenuItems(self):
		self.UpdateMenuItem(wx.ID_UNDO, self.CanUndo())
		self.UpdateMenuItem(wx.ID_REDO, self.CanRedo())
		self.UpdateMenuItem(wx.ID_PASTE, self.CanPaste())

