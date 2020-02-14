import mechanize
from http.cookiejar import LWPCookieJar

def printLog(browser_response):
    ''' gera arq com respelho da resposta html'''
    from bs4 import BeautifulSoup
    bs = BeautifulSoup(browser_response.read(),'lxml')
    with open('log.html','w') as f:
        f.writelines(bs.prettify())

def loginIntranet(browser):
    usuario = str(input("Insira seu login do sistema: "))
    from getpass import getpass
    senha = getpass()
    tela_main = 'http://intranet.unicesumar.edu.br/'
    browser.open(tela_main)
    browser.select_form(nr=0)
    browser['login'] = usuario
    browser['senha'] = senha
    browser.add_password(tela_main, usuario, senha)
    browser.submit()

def acessaFrmQuestao():
    # primeira tela
    url_cadastro_questao = 'http://intranet.unicesumar.edu.br/sistemas/bancoDeQuestoes/action/questaoAction.php'
    br.open(url_cadastro_questao)
    try:
        l_dbQuestao = br.find_link(nr=16)
        br.follow_link(l_dbQuestao)
        l_formQuestao = br.find_link(nr=16)
        br.follow_link(l_formQuestao)
        #br.select_form(nr=0)
    except Exception as e:
        print(e)
    
def mapeiaQuestao(codigo_questao):
    url_api = "http://intranet.unicesumar.edu.br/sistemas/bancoDeQuestoes/action/questaoAction.php"
    payload = {
        "action" : "filtrar",
        "data[filtroJSON][idQuestao]" :	codigo_questao,
        "data[filtroJSON][temaAleatorio]" :	0,	
        "data[filtroJSON][tagAndOr]" : "tagAnd",
        "data[filtroJSON][destinoAndOr]" :	"destinoAnd",
        "data[filtroJSON][tipoRequest]" : "questaoListRequest"
    }
    from urllib import parse
    import json
    data = parse.urlencode(payload)
    request_form_questao = mechanize.Request(url_api,data)
    response = br.open(request_form_questao)
    #query = parse.parse_qs(response.get_data(),encoding="latin1")
    #conv = json.dumps(query)
    dados_questao = response.get_data().decode("latin1")
    print(type(dados_questao))

    return dados_questao

if __name__ == "__main__":
    #TODO passar parametros como argumentos
    br = mechanize.Browser()
    #br.set_debug_http(True)
    cookiejar = LWPCookieJar()
    br.set_cookiejar(cookiejar)
    # Broser options 
    br.set_handle_equiv( False ) 
    br.set_handle_gzip( False ) 
    br.set_handle_redirect( True ) 
    br.set_handle_referer( False ) 
    br.set_handle_robots( False )
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    #br.set_debug_http(True)
    #br.set_debug_redirects(True)
    #br.set_debug_responses(True)
    br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ]
    loginIntranet(br)
    acessaFrmQuestao()
    codigo_questao = input("\n\nDigite o(s) código(s) da(s) questao(oes).\nse nao souber digite 208454\n\n"+9*"-"+">  ")
    import json
    dados_questao = json.loads(mapeiaQuestao(codigo_questao))
    # form de pesquisa de questoes
    for item in dados_questao.get("data"):
        for ocor in item.items():
            print(ocor)
        print("\n")
    input("Aperte uma tecla para finalizar")
    # link para novo cadastro de questoes
    #l_formNovoCadatro = br.find_link(nr=17)
