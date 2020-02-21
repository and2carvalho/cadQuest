# coding=utf-8

from api.usuario import Usuario
from api.util import loginApp, serializaRequest, addQuestao, viewQuestao, printLog
import wx
import gui


class Login(gui.Login):

    def __init__(self,parent):
        gui.Login.__init__(self, parent)

class PyFeed(gui.PyFeed):

    def __init__(self, parent):
        gui.PyFeed.__init__(self, parent)
        self.login_frame = Login(self)
        self.login_frame.Show()

        self.login_frame.btn_login.Bind( wx.EVT_BUTTON, self.acessar_intranet )

    def acessar_intranet(self, event):
        self.tutor = Usuario(self.login_frame.txt_login.GetValue(), self.login_frame.txt_senha.GetValue())
        loginApp(self.tutor)
        if (self.tutor.br.response().geturl() == "http://intranet.unicesumar.edu.br/?erro_login"):
            print("\nATENÇÃO! Não foi possivel realizar o acesso com os dados digitados")
            self.login_frame.txt_login.Clear()
            self.login_frame.txt_senha.Clear()
        else:
            self.login_frame.Hide()
            self.Show()
            self.tutor.acessaFrmQuestao()

    def estrutura_questao(self, event):
        codigo_questao = self.txt_idQuestao.GetValue()
        # busca questão pelo id informado
        if (codigo_questao != ""):
            dados_questao = self.tutor.requestQuestao(codigo_questao)
            result_questao = serializaRequest(dados_questao)
            if result_questao != '[]':
                # salva dados da questão no banco de dados interno
                addQuestao(result_questao)
                # aplica estruturação de questão
                # imagino que tera que criar uma api para questao que recebe os cryps
                estrutura_questao = self.tutor.requestAlternativa(codigo_questao)
                result_estrutura = serializaRequest(estrutura_questao)
                self.txt_idQuestao.Clear()
                #viewQuestao()
                return result_questao, result_estrutura
            else:
                print("\nOps, algo deu errado!\nOu essa questão não foi cadastrada pelo seu usuario "
                    "ou você não tem permissão para acessar essa funcionalidade.")
                self.txt_idQuestao.Clear()
        else:
            print("\nFavor preencher código da questao para realizar a estruturação")
            self.txt_idQuestao.Clear()

if __name__ == "__main__":
    
    app = wx.App(False)
    frame = PyFeed(None)

    app.MainLoop()