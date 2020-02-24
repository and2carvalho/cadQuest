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
            
    def requestQuestao(self, id_questao):

        #TODO ajustar tela dialog para trazer informações dinâmicas
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
        # TODO já vincular o cadastro das informações no banco de dados interno
        # seguindo o link de edição de questao que vem como resposta do request
        return dados_questao

    def requestAlternativa(self, idQuestao, op_correta):
        
        ''' Envia cadastro de alternativas para API. As estruturas a serem
        enviadas são definidas tendo como base a dificuldade e o tipo de questão. '''

        from urllib import parse
        from db.model import Questao, Session
        try:
            session = Session()
            query = session.query(Questao).filter(Questao.idQuestao == idQuestao)
            result = query.one_or_none()
            #insere alternativas
            if (result.dsComplexidade == "Fácil") & (result.dsTipoQuestao == "Objetiva de falso e verdadeiro"):
                url_api = "http://intranet.unicesumar.edu.br/sistemas/bancoDeQuestoes/action/alternativaAction.php"
                payload_1 = {
                    "action": "inserir",
                    "idQuestao": idQuestao,
                    "dsAlternativa": "F, F, V, V, F",
                    "correta" : 0
                }
                payload_2 = {
                    "action": "inserir",
                    "idQuestao": idQuestao,
                    "dsAlternativa": "V, F, V, F, V",
                    "correta" : 0
                }
                payload_3 = {
                    "action": "inserir",
                    "idQuestao": idQuestao,
                    "dsAlternativa": "F, F, V, F, F",
                    "correta" : 0
                }
                payload_4 = {
                    "action": "inserir",
                    "idQuestao": idQuestao,
                    "dsAlternativa": "V, V, V, F, V",
                    "correta" : 0
                }
                payload_5 = {
                    "action": "inserir",
                    "idQuestao": idQuestao,
                    "dsAlternativa": "F, V, F, F, V",
                    "correta" : 0
                }
                # seleciona alternativa correta
                if op_correta == 0:
                    payload_1["correta"] = 1
                elif op_correta == 1:
                    payload_2["correta"] = 1
                elif op_correta == 2:
                    payload_3["correta"] = 1
                elif op_correta == 3:
                    payload_4["correta"] = 1
                elif op_correta == 4:
                    payload_5["correta"] = 1
                else:
                    pass
                data_1 = parse.urlencode(payload_1)
                data_2 = parse.urlencode(payload_2)
                data_3 = parse.urlencode(payload_3)
                data_4 = parse.urlencode(payload_4)
                data_5 = parse.urlencode(payload_5)
                request_insereAlternativa_1 = mechanize.Request(url_api, data_1)
                request_insereAlternativa_2 = mechanize.Request(url_api, data_2)
                request_insereAlternativa_3 = mechanize.Request(url_api, data_3)
                request_insereAlternativa_4 = mechanize.Request(url_api, data_4)
                request_insereAlternativa_5 = mechanize.Request(url_api, data_5)
                self.br.open(request_insereAlternativa_1)
                self.br.open(request_insereAlternativa_2)
                self.br.open(request_insereAlternativa_3)
                self.br.open(request_insereAlternativa_4)
                self.br.open(request_insereAlternativa_5)
                return "{Status : OK}"
            else:
                return "{Status : Fail}"
        except Exception as e:
            return "Erro de conexao com o banco de dados\n{}".format(e)