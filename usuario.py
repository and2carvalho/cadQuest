# coding=utf-8

import mechanize
from http.cookiejar import LWPCookieJar


class Usuario():
    
    # TODO isso vai para o banco de dados e devera ser
    # feita uma api para o servidor para cuidar do cadastro de 
    # questoes e usuarios
    usuario = "luciana.tavone"#str(input("Insira seu login do sistema: "))#
    #from getpass import getpass
    senha = "31415*Pi"#getpass()#
    matricula = " "
    
    def __init__(self):

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
        #self.br.set_debug_http(True)
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
        url_api = "http://intranet.unicesumar.edu.br/sistemas/bancoDeQuestoes/action/questaoAction.php"
        payload = {
            "action" : "filtrar",
            "data[filtroJSON][idQuestao]" :	id_questao,
            "data[filtroJSON][temaAleatorio]" :	0,	
            "data[filtroJSON][tagAndOr]" : "tagAnd",
            "data[filtroJSON][destinoAndOr]" :	"destinoAnd",
            "data[filtroJSON][tipoRequest]" : "questaoListRequest"
        }
        from urllib import parse
        import json
        data = parse.urlencode(payload)
        request_form_questao = mechanize.Request(url_api,data)
        response = self.br.open(request_form_questao)
        dados_questao = response.get_data().decode("latin1")
        # TODO já vincular o cadastro das informações no banco de dados interno
        # seguindo o link de edição de questao que vem como resposta do request
        return dados_questao

    def estruturaQuestao(self):
        pass