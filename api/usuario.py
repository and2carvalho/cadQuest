# coding=utf-8

import mechanize
from http.cookiejar import LWPCookieJar
from api.util import printLog

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
        from urllib import parse
        data = parse.urlencode(payload)
        request_form_questao = mechanize.Request(url_api,data)
        response = self.br.open(request_form_questao)
        dados_questao = response.get_data().decode("latin1")
        return dados_questao

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
            "idNodeRaiz": 1,
            "idOrigem":idOrigem,
            "idTipoQuestao":idTipoQuestao
        }
        from urllib import parse
        data = parse.urlencode(payload)
        request_form_questao = mechanize.Request(url_api,data)
        response = self.br.open(request_form_questao)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.read(), "lxml")
        idQuestao = soup.find("input", {"id":"idQuestao"}).get("value")
        return idQuestao

    def requestAlternativa(self, idQuestao, op_correta, dic_alternativas):
        
        ''' Envia cadastro de alternativas para API. As estruturas a serem
        enviadas são definidas tendo como base a dificuldade e o tipo de questão. '''
        from urllib import parse
        try:
            url_api = "http://intranet.unicesumar.edu.br/sistemas/bancoDeQuestoes/action/alternativaAction.php"
            # insere o id da questao no dicionario de alternativas
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
            return "{ Status : Success}"
        except Exception as e:
            return "Erro de conexao com o servidor Intranet\n{}".format(e)