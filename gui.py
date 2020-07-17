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


def resource_path(relative_path):  #necessário para inserir imagens no executável
	""" Get absolute path to resource, works for dev and for PyInstaller """
	import os
	import sys
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")

	return os.path.join(base_path, relative_path)


class Login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PyFeed - Unicesumar EAD", pos = wx.DefaultPosition, size = wx.Size( 298,339 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 298,339 ), wx.Size( 298,339 ) )
		self.SetExtraStyle( wx.FRAME_EX_METAL )
		self.SetBackgroundColour( wx.Colour( 0, 93, 126 ) )

		bSizerApp = wx.BoxSizer( wx.VERTICAL )

		sbSizerLogo = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.m = wx.StaticBitmap( sbSizerLogo.GetStaticBox(), wx.ID_ANY, wx.Bitmap( resource_path(u"logoCesumar.png"), wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		sbSizerLogo.Add( self.m, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )


		bSizerApp.Add( sbSizerLogo, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )

		bSizerMain = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 3, 1, 0, 0 )

		self.lb_login = wx.StaticText( self, wx.ID_ANY, u"Insira Login e Senha", wx.Point( 2,1 ), wx.Size( -1,-1 ), 0 )
		self.lb_login.Wrap( -1 )

		self.lb_login.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Hack" ) )
		self.lb_login.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		gSizer1.Add( self.lb_login, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.txt_login = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gSizer1.Add( self.txt_login, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txt_senha = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), wx.TE_PASSWORD )
		gSizer1.Add( self.txt_senha, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizerMain.Add( gSizer1, 0, wx.ALIGN_CENTER|wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 1, 1, 0, 0 )

		gSizer2.SetMinSize( wx.Size( -1,50 ) )
		self.bt_login = wx.Button( self, wx.ID_ANY, u"ACESSAR INTRANET", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.bt_login, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizerMain.Add( gSizer2, 0, wx.EXPAND, 5 )

		bSizerMain.Add( ( 0, 0), 1, 0, 5 )
		
		self.st_credits = wx.StaticText( self, wx.ID_ANY, u"Desenvolvido por André C. Antero de Carvalho", wx.DefaultPosition, wx.DefaultSize, 0)
		self.st_credits.Wrap(-1)
		self.st_credits.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

		bSizerMain.Add( self.st_credits, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizerApp.Add( bSizerMain, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerApp )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.bt_login.Bind( wx.EVT_BUTTON, self.acessar_intranet )
		self.txt_login.Bind(wx.EVT_KEY_DOWN, self.onTabEnter)
		self.txt_senha.Bind(wx.EVT_KEY_DOWN, self.onTabEnter)
		self.Bind(wx.EVT_CLOSE, self.fechaTela)

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def acessar_intranet( self, event ):
		event.Skip()

	def onTabEnter( self, event ):
		event.Skip()
	
	def fechaTela( self, event):
		event.Skip()

###########################################################################
## Class AddQuestao
###########################################################################

class AddQuestao ( wx.Frame ):

	def __init__( self, parent, tipo_questao_suportado ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PyFeed - Unicesumar EAD", pos = wx.DefaultPosition, size = wx.Size( 900,715 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.SetBackgroundColour( wx.Colour( 0, 93, 126 ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.lb_disciplina = wx.StaticText( self, wx.ID_ANY, u"Disciplina", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_disciplina.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Hack" ) )
		self.lb_disciplina.Wrap( -1 )

		self.lb_disciplina.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer9.Add( self.lb_disciplina, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice2Choices = []
		self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		self.m_choice2.Disable()
		bSizer9.Add( self.m_choice2, 1, wx.ALL, 5 )

		self.lb_diretorioRaiz = wx.StaticText( self, wx.ID_ANY, u"Diretório Raiz", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_diretorioRaiz.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Hack" ) )
		self.lb_diretorioRaiz.Wrap( -1 )

		self.lb_diretorioRaiz.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer9.Add( self.lb_diretorioRaiz, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice5Choices = [ u"Unicesumar-EAD-GRAD" ]
		self.m_choice5 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice5Choices, 0 )
		self.m_choice5.SetSelection( 0 )
		bSizer9.Add( self.m_choice5, 1, wx.ALL, 5 )

		self.lb_origem = wx.StaticText( self, wx.ID_ANY, u"Origem", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_origem.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Hack" ) )
		self.lb_origem.Wrap( -1 )

		self.lb_origem.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer9.Add( self.lb_origem, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		ch_origemChoices = [ u"LIVRO NÚCLEO ESPECÍFICO" ]
		self.ch_origem = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_origemChoices, 0 )
		self.ch_origem.SetSelection( 0 )
		bSizer8.Add( self.ch_origem, 1, wx.ALL, 5 )

		bSizer9.Add( self.ch_origem, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		bSizer6.Add( bSizer9, 0, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.lb_tipoQuestao = wx.StaticText( self, wx.ID_ANY, u"Tipo de Questão", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_tipoQuestao.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Hack" ) )
		self.lb_tipoQuestao.Wrap( -1 )

		self.lb_tipoQuestao.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer10.Add( self.lb_tipoQuestao, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cb_tipoQuestaoChoices = tipo_questao_suportado
		self.cb_tipoQuestao = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cb_tipoQuestaoChoices, 0 )
		bSizer10.Add( self.cb_tipoQuestao, 1, wx.ALL, 5 )

		self.lb_complexidade = wx.StaticText( self, wx.ID_ANY, u"Complexidade", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_complexidade.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Hack" ) )
		self.lb_complexidade.Wrap( -1 )

		self.lb_complexidade.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer10.Add( self.lb_complexidade, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		ch_complexidadeChoices = [ u"Fácil", u"Médio", u"Difícil" ]
		self.ch_complexidade = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_complexidadeChoices, 0 )
		self.ch_complexidade.SetSelection( -1 )
		bSizer10.Add( self.ch_complexidade, 0, wx.ALL, 5 )

		self.lb_destino = wx.StaticText( self, wx.ID_ANY, u"Destino", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_destino.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Hack" ) )
		self.lb_destino.Wrap( -1 )

		self.rb_5afirm = wx.RadioButton(self,wx.ID_ANY, '', style=wx.RB_GROUP)
		self.rb_4afirm = wx.RadioButton(self,wx.ID_ANY, '')
		self.lb_rb4afirm = wx.StaticText(self, wx.ID_ANY, u"4 afirmativas", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lb_rb4afirm.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Hack" ) )
		self.lb_rb4afirm.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))
		self.lb_rb4afirm.Wrap( -1 )
		self.lb_rb5afirm = wx.StaticText(self, wx.ID_ANY, u"5 afirmativas", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lb_rb5afirm.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Hack" ) )
		self.lb_rb5afirm.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))
		self.lb_rb5afirm.Wrap( -1 )
		bSizer10.Add( self.rb_4afirm, 0, wx.ALL|wx.ALIGN_CENTER, 5)
		bSizer10.Add( self.lb_rb4afirm, 0, wx.ALL|wx.ALIGN_CENTER, 5)
		bSizer10.Add( self.rb_5afirm, 0, wx.ALL|wx.ALIGN_CENTER, 5)
		bSizer10.Add( self.lb_rb5afirm, 0, wx.ALL|wx.ALIGN_CENTER, 5)
		
		self.lb_destino.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer10.Add( self.lb_destino, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.cb_destinoProva = wx.CheckBox( self, wx.ID_ANY, u"Prova", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_destinoProva.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer10.Add( self.cb_destinoProva, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.cb_destinoAtv = wx.CheckBox( self, wx.ID_ANY, u"Atv. de Estudo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_destinoAtv.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer10.Add( self.cb_destinoAtv, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer6.Add( bSizer10, 0, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.lb_enunciado = wx.StaticText( self, wx.ID_ANY, u"Texto Base / Enunciado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_enunciado.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Hack" ) )
		self.lb_enunciado.Wrap( -1 )

		self.lb_enunciado.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer12.Add( self.lb_enunciado, 0, wx.ALL, 5 )

		self.tx_enunciado = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,250 ), wx.TE_MULTILINE|wx.TE_RICH2 )
		bSizer12.Add( self.tx_enunciado, 0, wx.ALL|wx.EXPAND, 5 )

		self.lb_resposta = wx.StaticText( self, wx.ID_ANY, u"Resposta Esperada", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_resposta.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Hack" ) )
		self.lb_resposta.Wrap( -1 )

		self.lb_resposta.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		self.lb_fileEnun = wx.StaticText( self, wx.ID_ANY, u"Selecione um arquivo de imagem para o Enunciado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_fileEnun.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Hack" ) )
		self.lb_fileEnun.Wrap( -1 )
		self.lb_fileEnun.SetForegroundColour( wx.Colour( 229, 229, 229 ) )
		row1 = wx.StaticBoxSizer(wx.HORIZONTAL , self, '')
		row1.Add(self.lb_fileEnun, 0, wx.ALL, 10)
		self.fileCtrlEnun = wx.FilePickerCtrl(self, message="Upload de imagem", wildcard="Imagem png (.png)|*.png|Imagem jpg (.jpg)|*.jpg", style=wx.FLP_USE_TEXTCTRL, size=(390, 25))
		row1.Add(self.fileCtrlEnun, 0, wx.ALL, 8)
		bSizer12.Add(row1, 1, wx.ALL|wx.EXPAND, 0)
		bSizer12.Add( self.lb_resposta, 0, wx.ALL, 5 )

		self.tx_resposta = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,100 ), wx.TE_MULTILINE|wx.TE_RICH2 )
		bSizer12.Add( self.tx_resposta, 0, wx.ALL|wx.EXPAND, 5 )

		self.lb_fileFeedback = wx.StaticText( self, wx.ID_ANY, u"Selecione um arquivo de imagem para o FeedBack", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_fileFeedback.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Hack" ) )
		self.lb_fileFeedback.Wrap( -1 )
		self.lb_fileFeedback.SetForegroundColour( wx.Colour( 229, 229, 229 ) )
		row2 = wx.StaticBoxSizer(wx.HORIZONTAL , self, '')
		self.fileCtrlFeedback = wx.FilePickerCtrl(self, message="Upload de imagem", wildcard="Imagem png (.png)|*.png|Imagem jpg (.jpg)|*.jpg", style=wx.FLP_USE_TEXTCTRL, size=(390, 25))
		row2.Add(self.lb_fileFeedback, 0, wx.ALL, 10)
		row2.Add(self.fileCtrlFeedback, 0, wx.ALL, 8)
		bSizer12.Add(row2, 1, wx.ALL|wx.EXPAND, 0)

		bSizer6.Add( bSizer12, 0, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.bt_corretorOrt = wx.Button( self, wx.ID_ANY, u"Corretor Ortográfico", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bt_salvarQuestao = wx.Button( self, wx.ID_ANY, u"Salvar Nova Questão", wx.DefaultPosition, wx.DefaultSize, 0 )

		bSizer13.Add( self.bt_corretorOrt, 0, wx.ALL|wx.ALIGN_LEFT, 10 )
		bSizer13.Add( self.bt_salvarQuestao, 0, wx.ALL|wx.ALIGN_RIGHT, 10 )

		bSizer6.Add(bSizer13,0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL,15)

		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.bt_salvarQuestao.Bind( wx.EVT_BUTTON, self.addQuestao )
		self.bt_corretorOrt.Bind( wx.EVT_BUTTON, self.corrigeTxt )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def addQuestao( self, event ):
		event.Skip()

	def corrigeTxt( self, event ):
		event.Skip()

###########################################################################
## Class PyFeed
###########################################################################

class PyFeed ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PyFeed - Unicesumar EAD", pos = wx.DefaultPosition, size = wx.Size( 298,325 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 298,325 ), wx.Size( 298,325 ) )
		self.SetExtraStyle( wx.FRAME_EX_METAL )
		self.SetBackgroundColour( wx.Colour( 0, 93, 126 ) )

		bSizerApp = wx.BoxSizer( wx.VERTICAL )

		sbSizerLogo = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.img_logo = wx.StaticBitmap( sbSizerLogo.GetStaticBox(), wx.ID_ANY, wx.Bitmap( resource_path(u"logoCesumar.png"), wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizerLogo.Add( self.img_logo, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )


		bSizerApp.Add( sbSizerLogo, 0, wx.ALIGN_CENTER, 0 )

		bSizerMain = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 2, 1, 0, 0 )

		self.lb_main = wx.StaticText( self, wx.ID_ANY, u"Insira o código da Questão", wx.Point( 2,1 ), wx.DefaultSize, 0 )
		self.lb_main.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Hack" ) )
		self.lb_main.Wrap( -1 )

		self.lb_main.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Hack" ) )
		self.lb_main.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		gSizer1.Add( self.lb_main, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.txt_idQuestao = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.txt_idQuestao, 0, wx.TOP|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizerMain.Add( gSizer1, 0, wx.ALIGN_CENTER|wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 1, 1, 0, 0 )

		self.b_estruturar = wx.Button( self, wx.ID_ANY, u"Estruturar Questão", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.b_estruturar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizerMain.Add( gSizer2, 0, wx.EXPAND, 5 )

		gSizer7 = wx.GridSizer( 1, 4, 0, 0 )

		self.btn_novaQuestao = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 60,50 ), 0 )

		self.btn_novaQuestao.SetBitmap( wx.Bitmap( resource_path(u"icon-estrut.png"), wx.BITMAP_TYPE_ANY ) )
		gSizer7.Add( self.btn_novaQuestao, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.btn_configEstrutura = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 60,50 ), 0 )

		self.btn_configEstrutura.SetBitmap( wx.Bitmap( resource_path(u"icon-arvore.png"), wx.BITMAP_TYPE_ANY ) )
		gSizer7.Add( self.btn_configEstrutura, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.btn_confereQuestao = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 60,50 ), 0 )

		self.btn_confereQuestao.SetBitmap( wx.Bitmap( resource_path(u"icon-txtQuestao.png"), wx.BITMAP_TYPE_ANY ) )
		gSizer7.Add( self.btn_confereQuestao, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btn_configApp = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 60,50 ), 0 )

		self.btn_configApp.SetBitmap( wx.Bitmap( resource_path(u"icon-settings.png"), wx.BITMAP_TYPE_ANY ) )
		gSizer7.Add( self.btn_configApp, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )


		bSizerMain.Add( gSizer7, 0, 0, 5 )


		bSizerApp.Add( bSizerMain, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerApp )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.b_estruturar.Bind( wx.EVT_BUTTON, self.estrutura_questao )
		self.btn_novaQuestao.Bind( wx.EVT_BUTTON, self.form_novaQuestao )
		self.btn_configEstrutura.Bind( wx.EVT_BUTTON, self.form_editaEstrutura)
		self.Bind(wx.EVT_CLOSE, self.fechaTela)

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def estrutura_questao( self, event ):
		event.Skip()

	def form_novaQuestao( self, event ):
		event.Skip()

	def form_editaEstrutura( self, event):
		event.Skip()
	
	def fechaTela(self,event):
		event.Skip()



###########################################################################
## Class AlternativaTag
###########################################################################

class AlternativaTag ( wx.Dialog ):

	def __init__( self, parent, alternativas ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Finaliza Estrutura Banco de Questoes", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 93, 126 ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.lb_alt_correta = wx.StaticText( self, wx.ID_ANY, u"Selecione a alternativa correta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_alt_correta.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Hack" ) )
		self.lb_alt_correta.Wrap( -1 )

		self.lb_alt_correta.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer5.Add( self.lb_alt_correta, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 12 )

		rb_alt_corretaChoices = alternativas
		self.rb_alt_correta = wx.RadioBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, rb_alt_corretaChoices, 1, wx.RA_SPECIFY_COLS )
		self.rb_alt_correta.SetSelection( 0 )

		bSizer5.Add( self.rb_alt_correta, 0, wx.ALL|wx.EXPAND, 15 )
		self.rb_alt_correta.SetBackgroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.lb_modulo = wx.StaticText( self, wx.ID_ANY, u"Módulo ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_modulo.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Hack" ) )
		self.lb_modulo.Wrap( -1 )

		self.lb_modulo.SetForegroundColour( wx.Colour( 229, 229, 229 ) )
		bSizer5.Add( self.lb_modulo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.cb_mod51 = wx.CheckBox( self, wx.ID_ANY, u"51", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_mod51.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer15.Add( self.cb_mod51, 1, wx.ALL, 5 )

		self.cb_mod52 = wx.CheckBox( self, wx.ID_ANY, u"52", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_mod52.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer15.Add( self.cb_mod52, 1, wx.ALL, 5 )

		self.cb_mod53 = wx.CheckBox( self, wx.ID_ANY, u"53", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_mod53.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer15.Add( self.cb_mod53, 1, wx.ALL, 5 )

		self.cb_mod54 = wx.CheckBox( self, wx.ID_ANY, u"54", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_mod54.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer15.Add( self.cb_mod54, 1, wx.ALL, 5 )


		bSizer5.Add( bSizer15, 0, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.lb_curso = wx.StaticText(self, wx.ID_ANY, u"Curso ", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lb_curso.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Hack" ) )
		self.lb_curso.Wrap(-1)

		self.lb_curso.SetForegroundColour(wx.Colour(229, 229, 229))

		bSizer17.Add(self.lb_curso, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		cb_cursoChoices = [ u"TEO", u"TEOL", u"AGRO", u"CCONT", u"GPUB", u"ENG. PROD.", u"ENG. SOFT.", u"EDU", u"GRH", u"ADS", u"SI", u"DM", u"DI", u"ADM", u"PGER", u"MKT", u"MAT", u"HIST", u"SEG. TRAB.", u"PED", u"GAMB", u"GEO", u"T.I", u"GPV", u"GFIN", u"GASTRO", u"GCOM", u"GIMOB", u"LET", u"LOG", u"SEC", u"GH", u"DP", u"SSOC", u"GC", u"GQ", u"GTS", u"ECON", u"CURSO DE ORIGEM", u"EMP", u"BEDU", u"ECIV", u"EELE", u"EMEC", u"EMCA", u"HEPROD", u"HÍBRIDO", u"FSCE", u"PROJETO DE ENSINO", u"SPRIV", u"ARTV", u"CBIO", u"PSICO", u"PCERV", u"SALI", u"FIL", u"SOCIO", u"ECOS", u"POD", u"TINT" ]
		self.cb_curso = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cb_cursoChoices, 0 )
		bSizer17.Add( self.cb_curso, 1, wx.ALL, 5 )


		bSizer5.Add( bSizer17, 0, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.lb_atividade = wx.StaticText(self, wx.ID_ANY, u"Atividade", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lb_atividade.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Hack" ) )
		self.lb_atividade.Wrap(-1)

		self.lb_atividade.SetForegroundColour(wx.Colour(229, 229, 229))

		bSizer20.Add(self.lb_atividade, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.cb_prova = wx.CheckBox( self, wx.ID_ANY, u"Prova", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_prova.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer21.Add( self.cb_prova, 0, wx.ALL, 5 )

		self.cb_atv1 = wx.CheckBox( self, wx.ID_ANY, u"Atv2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_atv1.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer21.Add( self.cb_atv1, 1, wx.ALL, 5 )

		self.cb_atv2 = wx.CheckBox( self, wx.ID_ANY, u"Atv3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_atv2.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer21.Add( self.cb_atv2, 1, wx.ALL, 5 )

		self.cb_atv3 = wx.CheckBox( self, wx.ID_ANY, u"Atv4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_atv3.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer21.Add( self.cb_atv3, 1, wx.ALL, 5 )

		bSizer20.Add( bSizer21, 1, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		self.cb_atv4 = wx.CheckBox( self, wx.ID_ANY, u"Atv1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_atv4.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer21.Add( self.cb_atv4, 1, wx.ALL, 5 )

		bSizer5.Add( bSizer20, 0, wx.EXPAND, 5 )

		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		self.lb_unLivro = wx.StaticText(self, wx.ID_ANY, u"Un. Livro: ", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lb_unLivro.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Hack" ) )
		self.lb_unLivro.Wrap(-1)

		self.lb_unLivro.SetForegroundColour(wx.Colour(229, 229, 229))

		cb_unLivroChoices = [ u"Unidade I", u"Unidade II", u"Unidade III", u"Unidade IV", u"Unidade V", u"Unidade VI", u"Unidade VII" ]
		self.cb_unLivro = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cb_unLivroChoices, 0 )
		self.cb_unLivro.SetSelection( -1 )

		bSizer23.Add(self.lb_unLivro, 0, wx.ALL, 5)
		bSizer23.Add( self.cb_unLivro, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer5.Add( bSizer23, 1, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.bt_alt_tag = wx.Button( self, wx.ID_ANY, u"Selecionar e cadastrar estrutura", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.bt_alt_tag, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 12 )


		bSizer5.Add( bSizer16, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()
		bSizer5.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.bt_alt_tag.Bind( wx.EVT_BUTTON, self.setAlternativaTag )
		self.Bind(wx.EVT_CLOSE, self.fechaTela)

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def setAlternativaTag( self, event ):
		event.Skip()

	def fechaTela(self, event):
		event.Skip()


###########################################################################
## Class EditaEstrutura
###########################################################################

class EditaEstrutura ( wx.Frame ):

	def __init__( self, parent, tipo_questao_suportado, resp5Alternativas, resp4Alternativas ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CadQuest - Unicesumar EAD", pos = wx.DefaultPosition, size = wx.Size( 507,358 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 507,358 ), wx.Size( 507,358 ) )
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.SetBackgroundColour( wx.Colour( 0, 93, 126 ) )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		bSizer311 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Tipo de Questão", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		self.m_staticText25.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText25.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer311.Add( self.m_staticText25, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		m_comboBox5Choices = tipo_questao_suportado
		self.cb_tipoQuestao = wx.Choice( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( 180,-1 ), m_comboBox5Choices, 0 )
		self.cb_tipoQuestao.SetSelection( 1 )
		bSizer311.Add( self.cb_tipoQuestao, 0, wx.ALL, 5 )


		bSizer311.Add( ( 20, 0), 0, wx.EXPAND, 5 )

		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Dificuldade", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		self.m_staticText26.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText26.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer311.Add( self.m_staticText26, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		m_choice6Choices = [ u"Fácil", u"Médio", u"Difícil" ]
		self.ch_dificuldade = wx.Choice( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( 80,-1 ), m_choice6Choices, 0 )
		self.ch_dificuldade.SetSelection( 2)
		bSizer311.Add( self.ch_dificuldade, 0, wx.ALL, 5 )


		bSizer27.Add( bSizer311, 1, wx.EXPAND, 5 )

		bSizer321 = wx.BoxSizer( wx.VERTICAL )

		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer37 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Questões com 5 Alternativas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		self.m_staticText33.SetForegroundColour( wx.Colour( 229, 229, 229 ) )
		self.m_staticText33.SetMinSize( wx.Size( 222,-1 ) )

		bSizer37.Add( self.m_staticText33, 0, wx.ALL, 5 )


		bSizer30.Add( bSizer37, 1, wx.EXPAND, 5 )


		bSizer30.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer38 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Questões com 4 Alternativas", wx.DefaultPosition, wx.Size( 222,-1 ), 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )
		self.m_staticText34.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer38.Add( self.m_staticText34, 0, wx.ALL, 5 )


		bSizer30.Add( bSizer38, 1, wx.EXPAND, 5 )


		bSizer321.Add( bSizer30, 0, wx.ALL, 6 )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u" Novo Cadastro", wx.Point( -1,-1 ), wx.Size( 110,-1 ), 0|wx.BORDER_SUNKEN )
		self.m_staticText27.Wrap( -1 )

		self.m_staticText27.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText27.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer31.Add( self.m_staticText27, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_textCtrl36 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_textCtrl36, 0, wx.ALL, 5 )

		self.m_textCtrl37 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_textCtrl37, 0, wx.ALL, 5 )

		self.m_textCtrl38 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_textCtrl38, 0, wx.ALL, 5 )

		self.m_textCtrl39 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_textCtrl39, 0, wx.ALL, 5 )

		self.m_textCtrl40 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_textCtrl40, 0, wx.ALL, 5 )


		gbSizer2.Add( bSizer31, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u" Registro Atual", wx.DefaultPosition, wx.Size( 110,-1 ), 0|wx.BORDER_SUNKEN )
		self.m_staticText28.Wrap( -1 )

		self.m_staticText28.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText28.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer32.Add( self.m_staticText28, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		if (self.cb_tipoQuestao.StringSelection == 'Objetiva de resposta múltipla') & (self.ch_dificuldade.StringSelection == 'Difícil'):
			
			self.txt_primeiraResp5Alt = wx.TextCtrl( self, wx.ID_ANY, resp5Alternativas[self.cb_tipoQuestao.StringSelection][self.ch_dificuldade.StringSelection]['payload_1']['dsAlternativa'], wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY )
			bSizer32.Add( self.txt_primeiraResp5Alt, 0, wx.ALL, 5 )
			self.txt_segundaResp5Alt = wx.TextCtrl( self, wx.ID_ANY, resp5Alternativas[self.cb_tipoQuestao.StringSelection][self.ch_dificuldade.StringSelection]['payload_2']['dsAlternativa'], wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY )
			bSizer32.Add( self.txt_segundaResp5Alt, 0, wx.ALL, 5)
			self.txt_terceiraResp5Alt = wx.TextCtrl( self, wx.ID_ANY, resp5Alternativas[self.cb_tipoQuestao.StringSelection][self.ch_dificuldade.StringSelection]['payload_3']['dsAlternativa'], wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY )
			bSizer32.Add( self.txt_terceiraResp5Alt, 0, wx.ALL, 5)
			self.txt_quartaResp5Alt = wx.TextCtrl( self, wx.ID_ANY, resp5Alternativas[self.cb_tipoQuestao.StringSelection][self.ch_dificuldade.StringSelection]['payload_4']['dsAlternativa'], wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY )
			bSizer32.Add( self.txt_quartaResp5Alt, 0, wx.ALL, 5 )
			self.txt_quintaResp5Alt = wx.TextCtrl( self, wx.ID_ANY, resp5Alternativas[self.cb_tipoQuestao.StringSelection][self.ch_dificuldade.StringSelection]['payload_5']['dsAlternativa'], wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY )
			bSizer32.Add( self.txt_quintaResp5Alt, 0, wx.ALL, 5)

		else:
			self.txt_primeiraResp4Alt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
			bSizer32.Add( self.txt_primeiraResp4Alt, 0, wx.ALL, 5 )	
			self.txt_segundaResp4Alt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
			bSizer32.Add( self.txt_segundaResp4Alt, 0, wx.ALL, 5 )
			self.txt_terceiraResp4Alt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
			bSizer32.Add( self.txt_terceiraResp4Alt, 0, wx.ALL, 5 )
			self.txt_quartaResp4Alt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
			bSizer32.Add( self.txt_quartaResp4Alt, 0, wx.ALL, 5 )
			self.txt_quintaResp4Alt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
			bSizer32.Add( self.txt_quintaResp4Alt, 0, wx.ALL, 5 )


		gbSizer2.Add( bSizer32, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		gbSizer2.Add( ( 12, 0 ), wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u" Registro Atual", wx.DefaultPosition, wx.Size( 110,-1 ), 0|wx.BORDER_SUNKEN )
		self.m_staticText29.Wrap( -1 )

		self.m_staticText29.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText29.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer34.Add( self.m_staticText29, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
			
		self.txt_primeiraResp4Alt = wx.TextCtrl( self, wx.ID_ANY, resp4Alternativas[self.cb_tipoQuestao.StringSelection][self.ch_dificuldade.StringSelection]['payload_1']['dsAlternativa'], wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY )
		bSizer34.Add( self.txt_primeiraResp4Alt, 0, wx.ALL, 5 )			
		self.txt_segundaResp4Alt = wx.TextCtrl( self, wx.ID_ANY, resp4Alternativas[self.cb_tipoQuestao.StringSelection][self.ch_dificuldade.StringSelection]['payload_2']['dsAlternativa'], wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY )
		bSizer34.Add( self.txt_segundaResp4Alt, 0, wx.ALL, 5 )
		self.txt_terceiraResp4Alt = wx.TextCtrl( self, wx.ID_ANY, resp4Alternativas[self.cb_tipoQuestao.StringSelection][self.ch_dificuldade.StringSelection]['payload_3']['dsAlternativa'], wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY )
		bSizer34.Add( self.txt_terceiraResp4Alt, 0, wx.ALL, 5 )
		self.txt_quartaResp4Alt = wx.TextCtrl( self, wx.ID_ANY, resp4Alternativas[self.cb_tipoQuestao.StringSelection][self.ch_dificuldade.StringSelection]['payload_4']['dsAlternativa'], wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY )	
		bSizer34.Add( self.txt_quartaResp4Alt, 0, wx.ALL, 5 )
		self.txt_quintaResp4Alt = wx.TextCtrl( self, wx.ID_ANY, resp4Alternativas[self.cb_tipoQuestao.StringSelection][self.ch_dificuldade.StringSelection]['payload_5']['dsAlternativa'], wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY )
		bSizer34.Add( self.txt_quintaResp4Alt, 0, wx.ALL, 5 )
		gbSizer2.Add( bSizer34, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u" Novo Cadastro", wx.DefaultPosition, wx.Size( 110,-1 ), 0|wx.BORDER_SUNKEN )
		self.m_staticText30.Wrap( -1 )

		self.m_staticText30.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText30.SetForegroundColour( wx.Colour( 229, 229, 229 ) )

		bSizer35.Add( self.m_staticText30, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_textCtrl51 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.m_textCtrl51, 0, wx.ALL, 5 )

		self.m_textCtrl52 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.m_textCtrl52, 0, wx.ALL, 5 )

		self.m_textCtrl53 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.m_textCtrl53, 0, wx.ALL, 5 )

		self.m_textCtrl54 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.m_textCtrl54, 0, wx.ALL, 5 )

		self.m_textCtrl55 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.m_textCtrl55, 0, wx.ALL, 5 )


		gbSizer2.Add( bSizer35, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


		bSizer321.Add( gbSizer2, 1, wx.EXPAND, 5 )

		bSizer39 = wx.BoxSizer( wx.HORIZONTAL )

		self.bt_carregaDic = wx.Button( self, wx.ID_ANY, u"Carregar Valores do Dicionário", wx.DefaultPosition, wx.Size( 227,60 ), 0 )
		bSizer39.Add( self.bt_carregaDic, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer39.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.bt_salvar = wx.Button( self, wx.ID_ANY, u"Salvar", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		bSizer39.Add( self.bt_salvar, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.bt_cancelar = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		bSizer39.Add( self.bt_cancelar, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer321.Add( bSizer39, 1, wx.EXPAND, 5 )


		bSizer27.Add( bSizer321, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer27 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.bt_carregaDic.Bind( wx.EVT_BUTTON, self.carrega_dic )
		self.bt_salvar.Bind( wx.EVT_BUTTON, self.salva_estrutura )
		self.bt_cancelar.Bind( wx.EVT_BUTTON, self.cancelar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def carrega_dic( self, event ):
		event.Skip()

	def salva_estrutura( self, event ):
		event.Skip()

	def cancelar( self, event ):
		self.Destroy()


###########################################################################
## Class DialogQtdAfirmativas
###########################################################################

class DialogQtdAfirmativas ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 293,185 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.SetBackgroundColour( wx.Colour( 0, 93, 126 ) )

		gSizer7 = wx.GridSizer( 2, 1, 0, 0 )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Quantidade de Alternativas da Questão", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		self.m_staticText29.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText29.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer33.Add( self.m_staticText29, 0, wx.ALL, 5 )


		bSizer33.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		self.rb_4afirmativas = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, 0 )

		bSizer34.Add( self.rb_4afirmativas, 0, wx.ALL, 5 )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"4 Afirmativas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		self.m_staticText27.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText27.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer34.Add( self.m_staticText27, 0, wx.ALL, 5 )
		
		bSizer34.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.rb_5afirmativas = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		bSizer34.Add( self.rb_5afirmativas, 0, wx.ALL, 5 )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"5 Afirmativas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		self.m_staticText28.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText28.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer34.Add( self.m_staticText28, 0, wx.ALL, 5 )


		bSizer33.Add( bSizer34, 1, wx.EXPAND, 5 )


		gSizer7.Add( bSizer33, 1, wx.EXPAND, 5 )

		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		self.bt_confNumAfirm = wx.Button( self, wx.ID_ANY, u"Confirmar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.bt_confNumAfirm, 0, wx.ALIGN_CENTER, 5 )


		gSizer7.Add( bSizer24, 1, wx.ALIGN_CENTER, 5 )


		self.SetSizer( gSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.bt_confNumAfirm.Bind( wx.EVT_BUTTON, self.setQtdAfirmativas )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def setQtdAfirmativas( self, event ):
		event.Skip()
