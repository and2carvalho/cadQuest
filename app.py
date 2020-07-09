# coding=utf-8

from db.conn import dir_path
from api.usuario import Usuario
from api.utils import loginApp, serializaRequest, dbQuestao, dic_alternativas, dic_5afirmativas, dic_tags
from datetime import datetime
import wx
import gui
import time
#import wx.lib.inspection


class AddQuestao(gui.AddQuestao):

    def __init__(self, parent, tipo_questao_suportado):
        gui.AddQuestao.__init__(self, parent, tipo_questao_suportado)

'''
TODO
class DialogQtdAfirmativas (gui.DialogQtdAfirmativas):

    def __init__(self, parent):
        gui.DialogQtdAfirmativas.__init__(self, parent)

    def setQtdAfirmativas(self, event):
        if self.rb_4afirmativas.GetValue():
            self.alt == "4"
        else:
            self.alt == "5"
        event.StopPropagation()
        return self.alt
'''

class AlternativaTag(gui.AlternativaTag):

    def __init__(self, parent, alternativas):
        gui.AlternativaTag.__init__(self, parent, alternativas)

    def fechaTela(self, event):
        dialog = wx.MessageDialog(self, message = "Tem certeza que deseja sair?", caption = "Caption", style = wx.YES_NO, pos = wx.DefaultPosition)
        response = dialog.ShowModal()
        if (response == wx.ID_YES):
            self.rb_alt_correta.Destroy()
            self.Destroy()
        else:
            event.StopPropagation()

    def validaCampos(self):
        stg1 = False
        stg2 = False
        if not (self.cb_mod51.GetValue() == "") | (self.cb_mod52.GetValue() == "") | \
        (self.cb_mod53.GetValue() == "") | (self.cb_mod54.GetValue() == "") | \
        (self.cb_curso.GetValue() == "") | (self.cb_unLivro.GetValue() == ""):
            stg1 = True
        if stg1:
            if self.cb_atv1.GetValue() != False or self.cb_atv2.GetValue() != False or \
            self.cb_atv3.GetValue() != False or self.cb_atv4.GetValue() != False or \
            self.cb_prova.GetValue() != False:
                stg2 = True
        if stg1 & stg2:
            return True
        else:
            return False

    def setAlternativaTag(self, event):
        if not self.validaCampos():
            self.warn(self,"Todos os campos devem ser preenchidos")
            event.StopPropagation()
        else:
            self.Destroy()

    # msg de aviso disponível no frame
    def warn(self, parent, message, caption = 'ATENÇÃO!'):
        dlg = wx.MessageDialog(parent, message, caption, wx.OK | wx.ICON_WARNING)
        dlg.ShowModal()
        dlg.Destroy()

class PyFeed(gui.PyFeed):

    def __init__(self, parent):
        gui.PyFeed.__init__(self, parent)
        #wx.lib.inspection.InspectionTool().Show()
        self.login_frame = gui.Login(self)
        self.login_frame.Show()
        
        # lista de tipo de questoes suportados pelo programa; necessário adicionar um dicionario de alternativas
        # em 'api.util.dic_alternativas' para novos tipos de questões.
        self.tipo_questao_suportado = ["Objetiva de resposta única", "Objetiva de resposta múltipla"]
        self.btn_novaQuestao.ToolTip = wx.ToolTip("Cria Nova Questão")
        self.btn_configEstrutura.ToolTip = wx.ToolTip("Configura Estrutura de Alternativas")
        self.btn_confereQuestao.ToolTip = wx.ToolTip("Revisa Questão")
        self.btn_configApp.ToolTip = wx.ToolTip("Configurações")

        self.login_frame.bt_login.Bind(wx.EVT_BUTTON, self.acessar_intranet)
        self.login_frame.txt_login.Bind(wx.EVT_KEY_DOWN, self.onTabEnter)
        self.login_frame.txt_senha.Bind(wx.EVT_KEY_DOWN, self.onTabEnter)

    def onTabEnter(self, event):
        ''' Atalho para tecla TAB direcionar o cursor para o próximo campo'''

        keycode = event.GetKeyCode()
        if keycode == wx.WXK_TAB or keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
            event.EventObject.Navigate()
        event.Skip()

    def fechaTela(self, event):
        dialog = wx.MessageDialog(self, message = "Tem certeza que deseja sair?", caption = "Caption", style = wx.YES_NO, pos = wx.DefaultPosition)
        response = dialog.ShowModal()
        if (response == wx.ID_YES):
            wx.GetApp().ExitMainLoop()
        else:
            event.StopPropagation()
    # modal de msg disponíveis no frame
    def info(self, parent, message, caption = 'INFORMAÇÃO!'):
        dlg = wx.MessageDialog(parent, message, caption, wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def warn(self, parent, message, caption = 'ATENÇÃO!'):
        dlg = wx.MessageDialog(parent, message, caption, wx.OK | wx.ICON_WARNING)
        dlg.ShowModal()
        dlg.Destroy()

    def acessar_intranet(self, event):

        ''' Realiza login na intranet unicesumar e acessa o Formulário
        de busca das questões. '''

        self.tutor = Usuario("andre.antero","Shabala1234.")#self.login_frame.txt_login.GetValue(), self.login_frame.txt_senha.GetValue()
        loginApp(self.tutor)
        if (self.tutor.br.response().geturl() == "http://intranet.unicesumar.edu.br/?erro_login"):
            self.warn(self, "Não foi possivel realizar o acesso com os dados digitados")
            self.login_frame.txt_login.Clear()
            self.login_frame.txt_senha.Clear()
        else:
            self.tutor.acessaFrmQuestao()
            wx.SafeYield() # espera a próxima ação ser executada
            self.login_frame.Hide()
            self.Show()

    def corrigeTxt(self, event):
        from symspellpy import SymSpell
        #TODO entender porque o corretor não ilumina as mesmas palavras após a primeira ocorrência
        sym_spell = SymSpell()
        sym_spell.load_dictionary("static/frequency_dictionary_pt_82_765.txt", 0, 1,encoding="windows-1252")
        import re
        input_term = self.add_questao_frame.tx_enunciado.GetValue().lower()
        # retira caracteres usando `translate` e separa texto em lista de palavras
        ignorar = r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~1234567890“”–'
        texto = sym_spell.word_segmentation(input_term.translate(str.maketrans("","",ignorar)), max_edit_distance=2 ).segmented_string.split()
        sugestao = sym_spell.word_segmentation(input_term.translate(str.maketrans("","",ignorar)), max_edit_distance=2 ).corrected_string.split()
        # referencia: https://stackoverflow.com/questions/41592759/python-textctrl-search-and-highlight-functionality
        for i in range(self.add_questao_frame.tx_enunciado.GetNumberOfLines()):
            line = self.add_questao_frame.tx_enunciado.GetLineText(i)
            for palavra in texto:
                if palavra in line and palavra not in sugestao:
                    startPos = [i for i in range(len(texto)) if palavra.startswith(palavra, i)]
                    for ocor in startPos:
                        endPos = ocor + len(palavra)
                        self.add_questao_frame.tx_enunciado.SetStyle(ocor, endPos, wx.TextAttr("red", "white"))
        # retoma formatação correta do campo de texto
        self.add_questao_frame.SetForegroundColour(wx.BLACK)
        for i in range(len(texto)):
            if texto[i] != sugestao[i]:
                self.warn(self, "`" + texto[i] + "`" + " você quis dizer " + "`" + sugestao[i] + "` ?")

    def addQuestao(self, event):
        # cria condição para fazer necessário o preenchimento de um dos 2 checkbox do campo 'destino'
        destino = False
        self.acessar_intranet(event)

        if (self.add_questao_frame.cb_destinoProva.GetValue() is False) & (self.add_questao_frame.cb_destinoAtv.GetValue() is False):
            pass
        else:
            destino = True

        if (self.add_questao_frame.tx_enunciado.GetValue() != "") & (self.add_questao_frame.tx_resposta.GetValue() != "") \
                & (self.add_questao_frame.ch_complexidade.GetStringSelection() != "") & (self.add_questao_frame.cb_tipoQuestao.GetStringSelection() != "")\
                & (destino == True):
            try:
                enunciado = self.add_questao_frame.tx_enunciado.GetValue().replace("\n","<br>").translate(str.maketrans({'“':'"', '”':'"', '–':'-','—':'-'})).encode("windows-1252")
                feedback = self.add_questao_frame.tx_resposta.GetValue().replace("\n","<br>").translate(str.maketrans({'“':'"', '”':'"', '–':'-','—':'-'})).encode("windows-1252")
                complexidade = self.add_questao_frame.ch_complexidade.GetStringSelection()
                alternativas = self.add_questao_frame.cb_qtdAfirmativas.GetStringSelection()
                if complexidade == "Fácil":
                    idComplexidade = 1
                elif complexidade == "Médio":
                    idComplexidade = 2
                else:
                    idComplexidade = 3
                if alternativas == "4":
                    self.tutor.dic_temp['idAlternativas'] = "4"
                else:
                    self.tutor.dic_temp['idAlternativas'] = "5"
                if self.add_questao_frame.cb_destinoProva.GetValue() == True:
                    destino_prova = 1
                else:
                    destino_prova = None
                if self.add_questao_frame.cb_destinoAtv.GetValue() == True:
                    destino_atv = 4
                else:
                    destino_atv = None
                origem = self.add_questao_frame.ch_origem.GetStringSelection()
                idOrigem = dic_tags["idMacroOrigem"].get(origem)
                tipoQuestao = self.add_questao_frame.cb_tipoQuestao.GetStringSelection()
                idTipoQuestao = dic_tags["idMacroTipoQuestao"].get(tipoQuestao)
                imagemEnunciado = self.add_questao_frame.fileCtrlEnun.GetPath()
                if imagemEnunciado != "":
                    import base64
                    with open(imagemEnunciado,"rb") as img:
                        img_encoded = base64.b64encode(img.read())
                        enunciado += '&lt;br /&gt;&lt;img alt="" border="0" hspace="0" src="data:image/jpeg;base64,'  #referencia tirada da api da intranet
                        enunciado += str(img_encoded, 'utf-8') + '"'
                        enunciado += 'style="border:0px solid black; height:946px; margin-bottom:0px; margin-left:0px; margin-right:0px; margin-top:0px; width:1024px" vspace="0" /&gt;&lt;br /&gt;'
                else:
                    pass
                imagemFeedback = self.add_questao_frame.fileCtrlFeedback.GetPath()
                if imagemFeedback != "":
                    import base64
                    with open(imagemFeedback,"rb") as img:
                        img_encoded = base64.b64encode(img.read())
                        feedback += '&lt;br /&gt;&lt;img alt="" border="0" hspace="0" src="data:image/jpeg;base64,'   #referencia tirada da api da intranet
                        feedback += str(img_encoded, 'utf-8') + '"'
                        feedback += 'style="border:0px solid black; height:946px; margin-bottom:0px; margin-left:0px; margin-right:0px; margin-top:0px; width:1024px" vspace="0" /&gt;&lt;br /&gt;'
                else:
                    pass
                try:
                    idQuestao = self.tutor.requestPostQuestao(enunciado, feedback, idComplexidade, destino_prova,
                                                              destino_atv, idOrigem, idTipoQuestao)
                except Exception as e:
                    now = datetime.now()
                    logf = open(dir_path+"log.txt","a+")
                    logf.write(now.strftime("%d/%m/%Y, %H:%M:%S") + " - " + str(e) + "\n")
                    logf.close()
                self.txt_idQuestao.AppendText(idQuestao)
                self.add_questao_frame.Destroy()
                resp = "Retorno: Questão de número " + idQuestao + " adicionada com sucesso."
                logf = open(dir_path+"log.txt","a+")
                logf.write(datetime.today().strftime("%d/%m/%Y, %H:%M:%S") + " - " + str(resp) + "\n")
                logf.close()
            except Exception as e:
                now = datetime.now()
                logf = open(dir_path+"log.txt","a+")
                logf.write(now.strftime("%d/%m/%Y, %H:%M:%S") + " - " + str(e) + "\n")
                logf.close()
        else:
            return self.warn(self,"É necessário o preenchimento de todos os campos!")

    def form_novaQuestao( self, event ):
        self.add_questao_frame = gui.AddQuestao(self, self.tipo_questao_suportado)
        self.add_questao_frame.Show()
        #self.add_questao_frame.bt_corretorOrt.Bind( wx.EVT_BUTTON, self.corrigeTxt )
        self.add_questao_frame.bt_salvarQuestao.Bind( wx.EVT_BUTTON, self.addQuestao )

    def form_qtdAfirmativas( self, event) :
        self.setQtdAfirmativas = DialogQtdAfirmativas(self)
        self.setQtdAfirmativas.Show()

    def estrutura_questao(self, event):

        ''' Realiza busca na base de dados da intranet pelo número da questão.
        Adiciona/atualiza informações no db interno e cadastra estrutura de alternativas
        e tags via requisição api '''

        import json
        from db.model import Session, Questao

        codigo_questao = self.txt_idQuestao.GetValue()
        alternativas = [] # será adicionada as alternativas conforme cada tipo de questão
        # busca questão pelo id informado
        if (codigo_questao != ""):
            dados_questao = self.tutor.requestGetQuestao(codigo_questao)
            result_questao = serializaRequest(dados_questao)
            if result_questao != '[]':
                # salva/atualiza dados da questão no banco de dados interno
                try:
                    dbQuestao(result_questao)
                    session = Session()
                    query = session.query(Questao).filter(Questao.idQuestao == codigo_questao)
                    result = query.one_or_none()
                    url_questaoCompleta = "http://intranet.unicesumar.edu.br/sistemas/bancoDeQuestoes/action/"+result.urlVisualizar
                    dados_completosQuestao = self.tutor.br.open(url_questaoCompleta).get_data().decode("latin-1")
                    q_estruturaCompleta = json.loads(dados_completosQuestao)["data"]
                    if result.dsTipoQuestao in self.tipo_questao_suportado:
                        # verifica se há alternativas já cadastadas
                        if (q_estruturaCompleta.get("alternativaList") == []):
                            # aplica estruturação de questão
                            # testa se são 4 ou 5 afirmações na pergunta
                            #if (result.dsTipoQuestao == "Objetiva de resposta múltipla") and \
                            #   (result.dsComplexidade == "Difícil") and not self.tutor.dic_temp:
                            if (result.dsTipoQuestao == "Objetiva de resposta múltipla") and \
                            (result.dsComplexidade == "Difícil") and not self.tutor.dic_temp:
                                return self.warn(self, "Atenção! Essa questão não tem definida a quantidade de afirmativas, \
                                por hora é necessário fazer o cadastro pela intranet")
                            if (result.dsTipoQuestao == "Objetiva de resposta múltipla") and \
                            (result.dsComplexidade == "Difícil") and (self.tutor.dic_temp['idAlternativas'] == "5"):
                                dicionario = dic_5afirmativas[result.dsTipoQuestao][result.dsComplexidade]
                            else:
                                dicionario = dic_alternativas[result.dsTipoQuestao][result.dsComplexidade]
                            for payload in dicionario.items():
                                alternativas.append(payload[1].get("dsAlternativa"))
                            self.alternativa_panel = AlternativaTag(self, alternativas)
                            self.alternativa_panel.ShowModal()
                            op_correta = self.alternativa_panel.rb_alt_correta.GetSelection()
                            self.tutor.requestAlternativa(codigo_questao, op_correta, dicionario)
                            curso = self.alternativa_panel.cb_curso.GetStringSelection()
                            unLivro = self.alternativa_panel.cb_unLivro.GetStringSelection()
                            self.tutor.compoeTempDict(curso, unLivro, self.alternativa_panel)
                            self.tutor.requestTags(self.txt_idQuestao.GetValue())
                            self.tutor.dic_temp.clear() # reinicializar dic_temp para permitir novo cadastro na msm sessao
                            self.txt_idQuestao.Clear()
                            resp = "Retorno: Estruturação de questão realizada com sucesso"
                            logf = open(dir_path+"log.txt","a+")
                            logf.write(datetime.today().strftime("%d/%m/%Y, %H:%M:%S") + " - " + str(resp) + "\n")
                            logf.close()
                            return self.info(self,"Estruturação de questão realizada com sucesso!")
                        else:
                            self.tutor.dic_temp.clear() # reinicializar dic_temp para permitir novo cadastro na msm sessao
                            self.txt_idQuestao.Clear()
                            return self.warn(self, "Atenção! Essa questão já tem estrutura de alternativas cadastradas.\n\
                                Não foi possível realizar o processo.")
                    self.txt_idQuestao.Clear()
                    return self.info(self, "Estruturação ainda não suportada para esse tipo de questão: {}".format(str(q_estruturaCompleta["tipoQuestao"].get("dsTipoQuestao"))))
                except Exception as e:
                    now = datetime.now()
                    logf = open(dir_path+"log.txt","a+")
                    logf.write(now.strftime("%d/%m/%Y, %H:%M:%S") + " - " + str(e) + "\n")
                    logf.close()
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