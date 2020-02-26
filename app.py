# coding=utf-8

from api.usuario import Usuario
from api.util import loginApp, serializaRequest, addQuestao, dic_alternativas
import wx
import gui


class AlternativaCorreta(gui.AlternativaCorreta):

    def __init__(self, parent, alternativas):
        gui.AlternativaCorreta.__init__(self, parent, alternativas)
    
    def setAlternativaCorreta(self, event):
        self.Destroy()

class PyFeed(gui.PyFeed):

    def __init__(self, parent):
        gui.PyFeed.__init__(self, parent)
        self.login_frame = gui.Login(self)
        self.login_frame.Show()

        self.login_frame.btn_login.Bind( wx.EVT_BUTTON, self.acessar_intranet )
    
    def info(self, parent, message, caption = 'INFORMAÇÃO!'):
        dlg = wx.MessageDialog(parent, message, caption, wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def warn(self, parent, message, caption = 'ATENÇÃO!'):
        dlg = wx.MessageDialog(parent, message, caption, wx.OK | wx.ICON_WARNING)
        dlg.ShowModal()
        dlg.Destroy()

    def acessar_intranet(self, event):

        self.tutor = Usuario("luciana.tavone","31415*Pi")#self.login_frame.txt_login.GetValue(), self.login_frame.txt_senha.GetValue())
        loginApp(self.tutor)
        if (self.tutor.br.response().geturl() == "http://intranet.unicesumar.edu.br/?erro_login"):
            self.warn(self, "Não foi possivel realizar o acesso com os dados digitados")
            self.login_frame.txt_login.Clear()
            self.login_frame.txt_senha.Clear()
        else:
            self.login_frame.Hide()
            self.Show()
            self.tutor.acessaFrmQuestao()

    def estrutura_questao(self, event):

        import json
        from db.model import Session, Questao

        codigo_questao = self.txt_idQuestao.GetValue()
        # lista de tipo de questões suportadas pelo progama para interação
        tipo_questao_suportado = ["Objetiva de resposta única", "Objetiva de resposta múltipla"]
        alternativas = [] # será adicionada as alternativas conforme cada tipo de questão
        # busca questão pelo id informado
        if (codigo_questao != ""):
            dados_questao = self.tutor.requestQuestao(codigo_questao)
            result_questao = serializaRequest(dados_questao)
            if result_questao != '[]':
                # salva/atualiza dados da questão no banco de dados interno
                addQuestao(result_questao)
                session = Session()
                query = session.query(Questao).filter(Questao.idQuestao == codigo_questao)
                result = query.one_or_none()
                url_questaoCompleta = "http://intranet.unicesumar.edu.br/sistemas/bancoDeQuestoes/action/"+result.urlVisualizar
                dados_completosQuestao = self.tutor.br.open(url_questaoCompleta).get_data().decode("latin1")
                q_estruturaCompleta = json.loads(dados_completosQuestao)["data"]
                if result.dsTipoQuestao in tipo_questao_suportado:
                    # verifica se há alternativas já cadastadas
                    if (q_estruturaCompleta.get("alternativaList") == []):
                        # aplica estruturação de questão
                        dicionario = dic_alternativas[result.dsTipoQuestao][result.dsComplexidade]
                        for payload in dicionario.items():
                            alternativas.append(payload[1].get("dsAlternativa"))
                        self.alternativa_panel = AlternativaCorreta(self, alternativas)
                        self.alternativa_panel.ShowModal()
                        op_correta = self.alternativa_panel.m_radioBox1.GetSelection()
                        self.tutor.requestAlternativa(codigo_questao, op_correta, dicionario)
                        self.txt_idQuestao.Clear()
                        return self.info(self,"Estruturação de alternativas realizada com sucesso!")
                    else:
                        self.txt_idQuestao.Clear()
                        return self.warn(self, "Atenção! Essa questão já tem estrutura de alternativas cadastradas.\n\
                            Não foi possível realizar o processo.")
                self.txt_idQuestao.Clear()
                return self.info(self, "Estruturação ainda não suportada para esse tipo de questão: {}".format(str(q_estruturaCompleta["tipoQuestao"].get("dsTipoQuestao"))))
            else:
                self.txt_idQuestao.Clear()
                return self.warn(self, "Ops, algo deu errado!\nOu essa questão não foi cadastrada pelo seu usuario ou você não tem permissão para acessar essa funcionalidade.")
        else:
            self.txt_idQuestao.Clear()
            return self.warn(self, "Favor preencher código da questão para prosseguir")

if __name__ == "__main__":
    
    app = wx.App(False)
    frame = PyFeed(None)

    app.MainLoop()