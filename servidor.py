from usuario import Usuario


def loginApp(Usuario):
    try:
        Usuario.loginIntranet()
    except Exception as e:
        print("Não foi possível fazer login no sistema\nVerificar dados de usuario e senha.")
        print("\ne")


def cadastraTutor():
    pass

def consultaQuestao():
    pass

def cadastraQuestao():
    pass


def printLog(browser_response):
    from bs4 import BeautifulSoup
    ''' gera arq com respelho da resposta html'''
    from bs4 import BeautifulSoup
    bs = BeautifulSoup(browser_response.read(),'lxml')
    with open('log.html','w') as f:
        f.writelines(bs.prettify())

def serializaRequest(payload):
    import json
    dados_questao = json.loads(payload)
    dados_questao = json.dumps(dados_questao.get("data"))
    return dados_questao