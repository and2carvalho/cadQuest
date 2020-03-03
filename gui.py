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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PyFeed - Unicesumar EAD", pos = wx.DefaultPosition, size = wx.Size( 298,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 298,350 ), wx.Size( 298,350 ) )
		self.SetExtraStyle( wx.FRAME_EX_METAL )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizerApp = wx.BoxSizer( wx.VERTICAL )

		sbSizerLogo = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.m = wx.StaticBitmap( sbSizerLogo.GetStaticBox(), wx.ID_ANY, wx.Bitmap( u"static/logoCesumar.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		sbSizerLogo.Add( self.m, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )


		bSizerApp.Add( sbSizerLogo, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )

		bSizerMain = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 3, 1, 0, 0 )

		self.lb_login = wx.StaticText( self, wx.ID_ANY, u"Insira Login e Senha", wx.Point( 2,1 ), wx.Size( -1,-1 ), 0 )
		self.lb_login.Wrap( -1 )

		self.lb_login.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Hack" ) )

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


		bSizerApp.Add( bSizerMain, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerApp )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.bt_login.Bind( wx.EVT_BUTTON, self.acessar_intranet )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def acessar_intranet( self, event ):
		event.Skip()


###########################################################################
## Class AddQuestao
###########################################################################

class AddQuestao ( wx.Frame ):

	def __init__( self, parent, tipo_questao_suportado ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PyFeed - Unicesumar EAD", pos = wx.DefaultPosition, size = wx.Size( 771,731 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.lb_modulo = wx.StaticText( self, wx.ID_ANY, u"Módulo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_modulo.Wrap( -1 )

		bSizer8.Add( self.lb_modulo, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.cb_mod51 = wx.CheckBox( self, wx.ID_ANY, u"51", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.cb_mod51, 0, wx.ALL, 5 )

		self.cb_mod52 = wx.CheckBox( self, wx.ID_ANY, u"52", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.cb_mod52, 0, wx.ALL, 5 )

		self.cb_mod53 = wx.CheckBox( self, wx.ID_ANY, u"53", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.cb_mod53, 0, wx.ALL, 5 )

		self.cb_mod54 = wx.CheckBox( self, wx.ID_ANY, u"54", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.cb_mod54, 0, wx.ALL, 5 )

		self.lb_curso = wx.StaticText( self, wx.ID_ANY, u"Curso", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_curso.Wrap( -1 )

		bSizer8.Add( self.lb_curso, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cb_cursoChoices = [ u"TEO", u"TEOL", u"AGRO", u"CCONT", u"GPUB", u"ENG. PROD.", u"ENG. SOFT.", u"EDU", u"GRH", u"ADS", u"SI", u"DM", u"DI", u"ADM", u"PGER", u"MKT", u"MAT", u"HIST", u"SEG. TRAB.", u"PED", u"GAMB", u"GEO", u"T.I", u"GPV", u"GFIN", u"GASTRO", u"GCOM", u"GIMOB", u"LET", u"LOG", u"SEC", u"GH", u"DP", u"SSOC", u"GC", u"GQ", u"GTS", u"ECON", u"CURSO DE ORIGEM", u"EMP", u"BEDU", u"ECIV", u"EELE", u"EMEC", u"EMCA", u"HEPROD", u"HÍBRIDO", u"FSCE", u"PROJETO DE ENSINO", u"SPRIV", u"ARTV", u"CBIO", u"PSICO", u"PCERV", u"SALI", u"FIL", u"SOCIO", u"ECOS", u"POD", u"TINT" ]
		self.cb_curso = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cb_cursoChoices, 0 )
		bSizer8.Add( self.cb_curso, 0, wx.ALL, 5 )

		self.lb_origem = wx.StaticText( self, wx.ID_ANY, u"Origem", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_origem.Wrap( -1 )

		bSizer8.Add( self.lb_origem, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		ch_origemChoices = [ u"LIVRO NÚCLEO ESPECÍFICO" ]
		self.ch_origem = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_origemChoices, 0 )
		self.ch_origem.SetSelection( 0 )
		bSizer8.Add( self.ch_origem, 0, wx.ALL, 5 )


		bSizer6.Add( bSizer8, 0, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.lb_disciplina = wx.StaticText( self, wx.ID_ANY, u"Disciplina", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_disciplina.Wrap( -1 )

		bSizer9.Add( self.lb_disciplina, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice2Choices = []
		self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		bSizer9.Add( self.m_choice2, 1, wx.ALL, 5 )

		self.lb_diretorioRaiz = wx.StaticText( self, wx.ID_ANY, u"Diretório Raiz", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_diretorioRaiz.Wrap( -1 )

		bSizer9.Add( self.lb_diretorioRaiz, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice5Choices = [ u"Unicesumar-EAD-GRAD" ]
		self.m_choice5 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice5Choices, 0 )
		self.m_choice5.SetSelection( 0 )
		bSizer9.Add( self.m_choice5, 0, wx.ALL, 5 )


		bSizer6.Add( bSizer9, 0, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.lb_tipoQuestao = wx.StaticText( self, wx.ID_ANY, u"Tipo de Questão", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_tipoQuestao.Wrap( -1 )

		bSizer10.Add( self.lb_tipoQuestao, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cb_tipoQuestaoChoices = tipo_questao_suportado
		self.cb_tipoQuestao = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cb_tipoQuestaoChoices, 0 )
		bSizer10.Add( self.cb_tipoQuestao, 1, wx.ALL, 5 )

		self.lb_complexidade = wx.StaticText( self, wx.ID_ANY, u"Complexidade", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_complexidade.Wrap( -1 )

		bSizer10.Add( self.lb_complexidade, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		ch_complexidadeChoices = [ u"Fácil", u"Médio", u"Difícil" ]
		self.ch_complexidade = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_complexidadeChoices, 0 )
		self.ch_complexidade.SetSelection( -1 )
		bSizer10.Add( self.ch_complexidade, 0, wx.ALL, 5 )

		self.lb_atividade = wx.StaticText( self, wx.ID_ANY, u"Atividade", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_atividade.Wrap( -1 )

		bSizer10.Add( self.lb_atividade, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.cb_prova = wx.CheckBox( self, wx.ID_ANY, u"Prova", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.cb_prova, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.cb_mapa = wx.CheckBox( self, wx.ID_ANY, u"Mapa", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.cb_mapa, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer6.Add( bSizer10, 0, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		cb_unLivroChoices = [ u"Capitulo I", u"Capitulo II", u"Capitulo III", u"Capitulo I", u"Capitulo IV", u"Capitulo V", u"Capitulo VI", u"Capitulo VII", u"Capitulo VIII", u"Capitulo IX" ]
		self.cb_unLivro = wx.RadioBox( self, wx.ID_ANY, u"Unidade do Livro", wx.DefaultPosition, wx.DefaultSize, cb_unLivroChoices, 7, wx.RA_SPECIFY_COLS )
		self.cb_unLivro.SetSelection( 0 )
		bSizer11.Add( self.cb_unLivro, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( bSizer11, 0, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.lb_enunciado = wx.StaticText( self, wx.ID_ANY, u"Texto Base / Enunciado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_enunciado.Wrap( -1 )

		bSizer12.Add( self.lb_enunciado, 0, wx.ALL, 5 )

		self.tx_enunciado = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,250 ), wx.TE_MULTILINE )
		bSizer12.Add( self.tx_enunciado, 0, wx.ALL|wx.EXPAND, 5 )

		self.lb_resposta = wx.StaticText( self, wx.ID_ANY, u"Resposta Esperada", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_resposta.Wrap( -1 )

		bSizer12.Add( self.lb_resposta, 0, wx.ALL, 5 )

		self.tx_resposta = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,100 ), wx.TE_MULTILINE )
		bSizer12.Add( self.tx_resposta, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( bSizer12, 0, wx.EXPAND, 5 )

		self.bt_salvarQuestao = wx.Button( self, wx.ID_ANY, u"Salvar Nova Questão", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.bt_salvarQuestao, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 11 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.bt_salvarQuestao.Bind( wx.EVT_BUTTON, self.addQuestao )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def addQuestao( self, event ):
		event.Skip()


###########################################################################
## Class PyFeed
###########################################################################

class PyFeed ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PyFeed - Unicesumar EAD", pos = wx.DefaultPosition, size = wx.Size( 298,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 298,350 ), wx.Size( 298,350 ) )
		self.SetExtraStyle( wx.FRAME_EX_METAL )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizerApp = wx.BoxSizer( wx.VERTICAL )

		sbSizerLogo = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.img_logo = wx.StaticBitmap( sbSizerLogo.GetStaticBox(), wx.ID_ANY, wx.Bitmap( u"static/logoCesumar.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizerLogo.Add( self.img_logo, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )


		bSizerApp.Add( sbSizerLogo, 0, wx.ALIGN_CENTER, 0 )

		bSizerMain = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 2, 1, 0, 0 )

		self.lb_main = wx.StaticText( self, wx.ID_ANY, u"Insira o código da Questão", wx.Point( 2,1 ), wx.DefaultSize, 0 )
		self.lb_main.Wrap( -1 )

		self.lb_main.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Hack" ) )

		gSizer1.Add( self.lb_main, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.txt_idQuestao = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.txt_idQuestao, 0, wx.TOP|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizerMain.Add( gSizer1, 0, wx.ALIGN_CENTER|wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 1, 1, 0, 0 )

		self.b_estruturar = wx.Button( self, wx.ID_ANY, u"Estruturar Questão", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.b_estruturar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizerMain.Add( gSizer2, 0, wx.EXPAND, 5 )

		gSizer7 = wx.GridSizer( 1, 4, 0, 0 )

		self.btn_novaQuestao = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 60,50 ), wx.BU_AUTODRAW|0 )

		self.btn_novaQuestao.SetBitmap( wx.Bitmap( u"static/icon-estrut.png", wx.BITMAP_TYPE_ANY ) )
		gSizer7.Add( self.btn_novaQuestao, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 8 )

		self.btn_configEstrutura = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 60,40 ), wx.BU_AUTODRAW|0 )

		self.btn_configEstrutura.SetBitmap( wx.Bitmap( u"static/icon-arvore.png", wx.BITMAP_TYPE_ANY ) )
		gSizer7.Add( self.btn_configEstrutura, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.btn_confereQuestao = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 60,40 ), wx.BU_AUTODRAW|0 )

		self.btn_confereQuestao.SetBitmap( wx.Bitmap( u"static/icon-txtQuestao.png", wx.BITMAP_TYPE_ANY ) )
		gSizer7.Add( self.btn_confereQuestao, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btn_configApp = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 60,50 ), wx.BU_AUTODRAW|0 )

		self.btn_configApp.SetBitmap( wx.Bitmap( u"static/icon-settings.png", wx.BITMAP_TYPE_ANY ) )
		gSizer7.Add( self.btn_configApp, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 8 )


		bSizerMain.Add( gSizer7, 0, 0, 5 )


		bSizerApp.Add( bSizerMain, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerApp )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.b_estruturar.Bind( wx.EVT_BUTTON, self.estrutura_questao )
		self.btn_novaQuestao.Bind( wx.EVT_BUTTON, self.form_novaQuestao )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def estrutura_questao( self, event ):
		event.Skip()

	def form_novaQuestao( self, event ):
		event.Skip()


###########################################################################
## Class AlternativaCorreta
###########################################################################

class AlternativaCorreta ( wx.Dialog ):

	def __init__( self, parent, alternativas ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Finaliza Estrutura Banco de Questoes", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer5.SetMinSize( wx.Size( 290,250 ) )
		self.lb_alt_correta = wx.StaticText( self, wx.ID_ANY, u"Selecione a alternativa correta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lb_alt_correta.Wrap( -1 )

		self.lb_alt_correta.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer5.Add( self.lb_alt_correta, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 12 )

		m_radioBox1Choices = alternativas
		self.m_radioBox1 = wx.RadioBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox1.SetSelection( 0 )
		bSizer5.Add( self.m_radioBox1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 12 )

		self.bt_alt_correta = wx.Button( self, wx.ID_ANY, u"Selecionar e cadastrar estrutura", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.bt_alt_correta, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 12 )


		self.SetSizer( bSizer5 )
		self.Layout()
		bSizer5.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.bt_alt_correta.Bind( wx.EVT_BUTTON, self.setAlternativaCorreta )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def setAlternativaCorreta( self, event ):
		event.Skip()


