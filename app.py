# coding=utf-8

from usuario import Usuario
from api import loginApp, serializaRequest, addQuestao, viewQuestao
import wx
import gui


class Login(gui.Login):
    
    def __init__(self,parent):
        gui.Login.__init__(self, parent)     

class PyFeed(gui.PyFeed):

    def __init__(self, parent):
        gui.PyFeed.__init__(self, parent)

        self.tutor = Usuario()
        self.login_frame = Login(self)
        self.login_frame.Show()

        self.login_frame.b_login.Bind( wx.EVT_BUTTON, self.acessar_intranet )

    def acessar_intranet(self, event):
        loginApp(self.tutor)
        self.login_frame.Hide()
        self.Show()
        self.tutor.acessaFrmQuestao()

    def estrutura_questao(self, event):
        codigo_questao = self.txt_idQuestao.GetValue()
        dados_questao = self.tutor.requestQuestao(codigo_questao)
        result = serializaRequest(dados_questao)
        addQuestao(result)
        self.txt_idQuestao.Clear()
        viewQuestao()

if __name__ == "__main__":
    
    app = wx.App(False)
    frame = PyFeed(None)

    app.MainLoop()