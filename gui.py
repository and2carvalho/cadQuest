# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Dec 20 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class pyFeed
###########################################################################

class PyFeed ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Estruturação Banco de Questoes", pos = wx.DefaultPosition, size = wx.Size( 298,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerApp = wx.BoxSizer( wx.VERTICAL )

		sbSizerLogo = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"logo" ), wx.VERTICAL )

		self.m_bitmap2 = wx.StaticBitmap( sbSizerLogo.GetStaticBox(), wx.ID_ANY, wx.Bitmap( u"logoCesumar.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizerLogo.Add( self.m_bitmap2, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizerApp.Add( sbSizerLogo, 0, wx.EXPAND, 5 )

		bSizerMain = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 2, 1, 0, 0 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Insira o código da Questão", wx.Point( 2,1 ), wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		gSizer1.Add( self.m_staticText2, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.f_idQuestao = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.f_idQuestao, 0, wx.TOP|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizerMain.Add( gSizer1, 0, wx.ALIGN_CENTER|wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 1, 1, 0, 0 )

		self.b_estruturar = wx.Button( self, wx.ID_ANY, u"Estruturar Qustão", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.b_estruturar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizerMain.Add( gSizer2, 0, wx.EXPAND, 5 )


		bSizerApp.Add( bSizerMain, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerApp )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.b_estruturar.Bind( wx.EVT_BUTTON, self.estrutura_questao )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def estrutura_questao( self, event ):
		event.Skip()


