# coding=utf-8

from api.usuario import Usuario
from api.util import loginApp, serializaRequest, addQuestao
import wx
import gui


class PyFeed(gui.PyFeed):

    def __init__(self, parent):
        gui.PyFeed.__init__(self, parent)
        self.login_frame = gui.Login(self)
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
                from db.model import Session, Questao
                session = Session()
                query = session.query(Questao).filter(Questao.idQuestao == codigo_questao)
                result = query.one_or_none()
                url_questaoCompleta = "http://intranet.unicesumar.edu.br/sistemas/bancoDeQuestoes/action/"+result.urlVisualizar
                dados_completosQuestao = self.tutor.br.open(url_questaoCompleta).get_data().decode("latin1")
                # verifica se há alternativas cadastradas e se a questão é do tipo suportada pelo programa
                import json
                q_estruturaCompleta = json.loads(dados_completosQuestao)["data"]
                if (q_estruturaCompleta["tipoQuestao"].get("dsTipoQuestao") == "Objetiva de falso e verdadeiro"):
                    if (q_estruturaCompleta.get("alternativaList") == []):
                        # aplica estruturação de questão
                        self.tutor.requestAlternativa(codigo_questao)
                        self.txt_idQuestao.Clear()
                        return print("\nEstruturação de alternativas realizada com sucesso!")
                    else:
                        self.txt_idQuestao.Clear()
                        return print("\nAtenção! Essa questão já tem estrutura de alternativas cadastradas.\n\
                            Não foi possível realizar o processo.")
                self.txt_idQuestao.Clear()
                return print("\nEstruturação ainda não suportada para esse tipo de questão: {}".format(str(q_estruturaCompleta["tipoQuestao"].get("dsTipoQuestao"))))
            else:
                self.txt_idQuestao.Clear()
                return print("\nOps, algo deu errado!\nOu essa questão não foi cadastrada pelo seu usuario ou você não tem permissão para acessar essa funcionalidade.")
        else:
            self.txt_idQuestao.Clear()
            return print("\nFavor preencher código da questao para realizar a estruturação")

if __name__ == "__main__":
    
    app = wx.App(False)
    frame = PyFeed(None)

    app.MainLoop()