# coding=utf-8

import mechanize
from http.cookiejar import LWPCookieJar
from urllib import parse

class Usuario():

    def __init__(self,usuario,senha):

        self.usuario = usuario
        self.senha = senha
        self.br = mechanize.Browser()
        cookiejar = LWPCookieJar()
        self.br.set_cookiejar(cookiejar)
        ##### Browser options #######
        self.br.set_handle_equiv( False )
        self.br.set_handle_gzip( False )
        self.br.set_handle_redirect( True ) 
        self.br.set_handle_referer( False ) 
        self.br.set_handle_robots( False )
        self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        self.br.set_debug_http(True)
        #self.br.set_debug_http(True)
        #self.br.set_debug_redirects(True)
        #self.br.set_debug_responses(True)
        ########----------###########
        self.br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ]
        #TODO buscar forma melhor de fazer o processo de cadastro das tags
        self.dic_temp = {} # necessario para guardar informações para cadastro de tags

    def loginIntranet(self):
        
        tela_main = 'http://intranet.unicesumar.edu.br/'
        self.br.open(tela_main)
        self.br.select_form(nr=0)
        self.br['login'] = self.usuario
        self.br['senha'] = self.senha
        self.br.add_password(tela_main, self.usuario, self.senha)
        self.br.submit()

    def acessaFrmQuestao(self):
        # primeira tela
        url_cadastro_questao = 'http://intranet.unicesumar.edu.br/sistemas/bancoDeQuestoes/action/questaoAction.php'
        self.br.open(url_cadastro_questao)
        try:
            l_dbQuestao = self.br.find_link(nr=16)
            self.br.follow_link(l_dbQuestao)
            l_formQuestao = self.br.find_link(nr=16)
            self.br.follow_link(l_formQuestao)
            #self.br.select_form(nr=0)
        except Exception as e:
            print(e)
            
    def requestGetQuestao(self, id_questao):

        ''' Recebe dados da API apartir de uma número de id de questão.'''

        url_api = "http://intranet.unicesumar.edu.br/sistemas/bancoDeQuestoes/action/questaoAction.php"
        payload = {
            "action" : "filtrar",
            "data[filtroJSON][idQuestao]" : id_questao,
            "data[filtroJSON][temaAleatorio]" : 0,
            "data[filtroJSON][tagAndOr]" : "tagAnd",
            "data[filtroJSON][destinoAndOr]" : "destinoAnd",
            "data[filtroJSON][tipoRequest]" : "questaoListRequest"
        }
        try:
            data = parse.urlencode(payload)
            request_form_questao = mechanize.Request(url_api,data)
            response = self.br.open(request_form_questao)
            dados_questao = response.get_data().decode("latin1")
            return dados_questao
        except Exception as e:
            print(e)

    def requestPostQuestao(self, enunciado, feedback, idComplexidade, idOrigem, idTipoQuestao):

        ''' Realiza primeiro cadastro da questão na API apartir do form do programa. '''

        url_api = "http://intranet.unicesumar.edu.br/sistemas/bancoDeQuestoes/action/questaoAction.php"
        payload = {
            "action" : "inserir",
            "ativo" : 1,
            "enunciado" : enunciado,
            "feedback" : feedback,
            "fileImgGabaritoBase64": None,
            "fileImgGabaritoNomeOriginal": None,
            "idComplexidade": idComplexidade,
            "idImgGabarito": None,
            "idNodeRaiz": 1,
            "idOrigem":idOrigem,
            "idTipoQuestao":idTipoQuestao
        }
        try:
            data = parse.urlencode(payload)
            request_form_questao = mechanize.Request(url_api,data)
            response = self.br.open(request_form_questao)
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(response.read(), "lxml")
            idQuestao = soup.find("input", {"id":"idQuestao"}).get("value")
            return idQuestao
        except Exception as e:
            print(e)

    def requestAlternativa(self, idQuestao, op_correta, dic_alternativas):
        
        ''' Envia cadastro de alternativas para API. As estruturas a serem
        enviadas são definidas tendo como base a dificuldade e o tipo de questão. '''
        #try:
        url_api = "http://intranet.unicesumar.edu.br/sistemas/bancoDeQuestoes/action/alternativaAction.php"
        # insere o id da questao no dicionario de alternativas
        try:
            for payload in dic_alternativas.items():
                payload[1]["idQuestao"] = idQuestao
            # seleciona alternativa correta
            if op_correta == 0:
                dic_alternativas["payload_1"]["correta"] = 1
            elif op_correta == 1:
                dic_alternativas["payload_2"]["correta"] = 1
            elif op_correta == 2:
                dic_alternativas["payload_3"]["correta"] = 1
            elif op_correta == 3:
                dic_alternativas["payload_4"]["correta"] = 1
            else:
                dic_alternativas["payload_5"]["correta"] = 1
            for payload in dic_alternativas.items():
                data = parse.urlencode(payload[1])
                request_insereAlternativa = mechanize.Request(url_api, data)
                self.br.open(request_insereAlternativa)
            return "{ Status : Success }"
        except Exception as e:
            print(e)
        #except Exception as e:
        #    return "Erro de conexao com o servidor Intranet\n{}".format(e)

    def requestTags(self, idQuestao):
        #TODO buscar forma de realizar request via payload tal como os outros.
        #request_data = "action=inserir&idNodeMacro=34&idNodeMacro=8&idNodeMacro=30&idNodeMacro=1&idNodeMacro=2&idQuestao=282497&idTagList%5B%5D="+dic_temp.get("34")+"&idTagList%5B%5D="+dic_temp.get("8")+"&idTagList%5B%5D="+dic_temp.get("30")+"&idTagList%5B%5D="+dic_temp.get("mod1")+"&idTagList%5B%5D="+dic_temp.get("mod2")+"&idTagList%5B%5D="+dic_temp.get("mod3")+"&idTagList%5B%5D="+dic_temp.get("mod4")+"&idTagList%5B%5D="+dic_temp.get("2")
        url_api = "http://intranet.unicesumar.edu.br/sistemas/bancoDeQuestoes/action/questaoTagAction.php"
        from urllib3._collections import HTTPHeaderDict
        payload = HTTPHeaderDict()
        try:
            payload.add("action", "inserir")
            payload.add("idNodeMacro","34")
            payload.add("idNodeMacro", "8")
            payload.add("idNodeMacro","30")
            payload.add("idNodeMacro", "1")
            payload.add("idNodeMacro", "2")
            payload.add("idQuestao", idQuestao)
            payload.add("idTagList[]", self.dic_temp.get("34"))
            payload.add("idTagList[]", self.dic_temp.get("atv1"))
            if self.dic_temp["atv2"]:
                payload.add("idTagList[]", self.dic_temp.get("atv2"))
            else:
                pass
            payload.add("idTagList[]", self.dic_temp.get("curso"))
            if self.dic_temp["mod1"]:
                payload.add("idTagList[]", self.dic_temp.get("mod1"))
            else:
                pass
            if self.dic_temp["mod2"]:
                payload.add("idTagList[]", self.dic_temp.get("mod2"))
            else:
                pass
            if self.dic_temp["mod3"]:
                payload.add("idTagList[]", self.dic_temp.get("mod3"))
            else:
                pass
            if self.dic_temp["mod4"]:
                payload.add("idTagList[]", self.dic_temp.get("mod4"))
            else:
                pass
            payload.add("idTagList[]", self.dic_temp.get("unLivro"))
            data = parse.urlencode(payload)
            request_form_questao = mechanize.Request(url_api,data)
            self.br.open(request_form_questao)
            return "{ Status : Success }"
        except Exception as e:
            print(e)

    def compoeTempDict(self, curso, unLivro, frame):
        # dicionario necessário para criar tags
        from api.util import dic_tags
        self.dic_temp = {
            "34": "131",
            "curso": dic_tags["idNodeMacro30"].get(curso),
            "unLivro": dic_tags["idMacroNode2"].get(unLivro),
            #TODO ajustar componente grafico do destino e pegar valor da seleção do usuario
        }
        if frame.cb_mod51.GetValue():
            self.dic_temp["mod1"] = "1"
        else:
            self.dic_temp["mod1"] = None
        if frame.cb_mod52.GetValue():
            self.dic_temp["mod2"] = "2"
        else:
            self.dic_temp["mod2"] = None
        if frame.cb_mod53.GetValue():
            self.dic_temp["mod3"] = "3"
        else:
            self.dic_temp["mod3"] = None
        if frame.cb_mod54.GetValue():
            self.dic_temp["mod4"] = "4"
        else:
            self.dic_temp["mod4"] = None
        # atividade prova é enviada como valor padrão para todos os cadastros
        self.dic_temp["atv1"] = dic_tags["idNodeMacro8"].get("PROVA")
        if frame.cb_atv1.GetValue():
            self.dic_temp["atv2"] = dic_tags["idNodeMacro8"].get("Atv1")
        elif frame.cb_atv2.GetValue():
            self.dic_temp["atv2"] = dic_tags["idNodeMacro8"].get("Atv2")
        elif frame.cb_atv3.GetValue():
            self.dic_temp["atv2"] = dic_tags["idNodeMacro8"].get("Atv3")
        elif frame.cb_atv4.GetValue():
            self.dic_temp["atv2"] = dic_tags["idNodeMacro8"].get("Atv4")
        elif frame.cb_atv5.GetValue():
            self.dic_temp["atv2"] = dic_tags["idNodeMacro8"].get("Atv5")
        elif frame.cb_atv6.GetValue():
            self.dic_temp["atv2"] = dic_tags["idNodeMacro8"].get("Atv6")
        elif frame.cb_atv7.GetValue():
            self.dic_temp["atv2"] = dic_tags["idNodeMacro8"].get("Atv7")
        else:
            self.dic_temp["atv2"] = None
