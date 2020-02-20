# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Feb 19 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Login
###########################################################################

class Login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PyFeed - Unicesumar EAD", pos = wx.DefaultPosition, size = wx.Size( 298,342 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 298,342 ), wx.Size( 298,342 ) )
		self.SetExtraStyle( wx.FRAME_EX_METAL )

		bSizerApp = wx.BoxSizer( wx.VERTICAL )

		sbSizerLogo = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Gerenciador Banco de Questoes" ), wx.VERTICAL )

		self.m_bitmap2 = wx.StaticBitmap( sbSizerLogo.GetStaticBox(), wx.ID_ANY, wx.Bitmap( u"static/logoCesumar.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizerLogo.Add( self.m_bitmap2, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )


		bSizerApp.Add( sbSizerLogo, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )

		bSizerMain = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 3, 1, 0, 0 )

		self.l_login = wx.StaticText( self, wx.ID_ANY, u"Insira Login e Senha", wx.Point( 2,1 ), wx.Size( -1,-1 ), 0 )
		self.l_login.Wrap( -1 )

		self.l_login.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Hack" ) )

		gSizer1.Add( self.l_login, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.txt_login = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.txt_login, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.ALL, 5 )

		self.txt_senha = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer1.Add( self.txt_senha, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		bSizerMain.Add( gSizer1, 0, wx.ALIGN_CENTER|wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 1, 1, 0, 0 )

		self.b_login = wx.Button( self, wx.ID_ANY, u"ACESSAR INTRANET", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.b_login, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizerMain.Add( gSizer2, 0, wx.EXPAND, 5 )


		bSizerApp.Add( bSizerMain, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerApp )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.b_login.Bind( wx.EVT_BUTTON, self.acessar_intranet )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def acessar_intranet( self, event ):
		event.Skip()


###########################################################################
## Class PyFeed
###########################################################################

class PyFeed ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Estrutura Banco de Questoes", pos = wx.DefaultPosition, size = wx.Size( 298,342 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 298,342 ), wx.Size( 298,342 ) )
		self.SetExtraStyle( wx.FRAME_EX_METAL )

		bSizerApp = wx.BoxSizer( wx.VERTICAL )

		sbSizerLogo = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Gerenciador Banco de Questoes" ), wx.VERTICAL )

		self.m_bitmap2 = wx.StaticBitmap( sbSizerLogo.GetStaticBox(), wx.ID_ANY, wx.Bitmap( u"static/logoCesumar.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizerLogo.Add( self.m_bitmap2, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )


		bSizerApp.Add( sbSizerLogo, 0, wx.ALIGN_CENTER, 0 )

		bSizerMain = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 2, 1, 0, 0 )

		self.l_buscaQuestao = wx.StaticText( self, wx.ID_ANY, u"Insira o código da Questão", wx.Point( 2,1 ), wx.DefaultSize, 0 )
		self.l_buscaQuestao.Wrap( -1 )

		self.l_buscaQuestao.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Hack" ) )

		gSizer1.Add( self.l_buscaQuestao, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.txt_idQuestao = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.txt_idQuestao, 0, wx.TOP|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizerMain.Add( gSizer1, 0, wx.ALIGN_CENTER|wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 1, 1, 0, 0 )

		self.b_estruturar = wx.Button( self, wx.ID_ANY, u"Estruturar Qustão", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.b_estruturar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizerMain.Add( gSizer2, 0, wx.EXPAND, 5 )

		gSizer7 = wx.GridSizer( 1, 4, 0, 0 )

		self.m_bpButton3 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( -1,-1 ), wx.BU_AUTODRAW|0 )

		self.m_bpButton3.SetBitmap( wx.Bitmap( u"static/icon-estrut.png", wx.BITMAP_TYPE_ANY ) )
		gSizer7.Add( self.m_bpButton3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 15 )

		self.m_bpButton5 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 60,40 ), wx.BU_AUTODRAW|0 )

		self.m_bpButton5.SetBitmap( wx.Bitmap( u"static/icon-arvore.png", wx.BITMAP_TYPE_ANY ) )
		gSizer7.Add( self.m_bpButton5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_bpButton4 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 60,40 ), wx.BU_AUTODRAW|0 )

		self.m_bpButton4.SetBitmap( wx.Bitmap( u"static/icon-txtQuestao.png", wx.BITMAP_TYPE_ANY ) )
		gSizer7.Add( self.m_bpButton4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_bpButton6 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		gSizer7.Add( self.m_bpButton6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )


		bSizerMain.Add( gSizer7, 1, wx.EXPAND, 5 )


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


