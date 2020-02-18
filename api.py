def loginApp(Usuario):
    try:
        Usuario.loginIntranet()
    except Exception as e:
        print("Não foi possível fazer login no sistema\nVerificar dados de usuario e senha.")
        print("\ne")

def serializaRequest(payload):
    # TODO colocar filtro de variaveis reservadas, para usuario nao ter acesso 
    import json
    dados_questao = json.loads(payload)
    dados_questao = json.dumps(dados_questao.get("data"))
    return dados_questao

def printLog(browser_response):
    from bs4 import BeautifulSoup
    ''' gera arq com respelho da resposta html'''
    from bs4 import BeautifulSoup
    bs = BeautifulSoup(browser_response.read(),'lxml')
    with open('log.html','w') as f:
        f.writelines(bs.prettify())


def _cadastraUSUARIO():
    '''O SISTEMA DE GESTAO DE BANCO DE QUESTOES NÃO FAZ CADASTRO DE USUARIO NEM FAZ QUALQUER TIPO
    DE CONTROLE DE PERMISSAO AO ACESSO DAS INFORMACOES DO SISTEMA DA UNICESUMAR. A UNICA FUNCAO
    DESEMPENHADA É O ACESSO À API DE CADASTRO DE QUESTOES PARA ENVIAR AS INFORMACOES AO SISTEMA
    DE FORMA MAIS EFICIENTE'''
    pass

def addQuestao(request_args):
    ''' os argumentos precisam vir como dicionario ou lista de dicionaro
    do requesta de consulta de questao '''
    from model import Questao, Session
    import json
    #TODO Colocar condição para nao adicionar caso o idQuestao já exista 
    consulta = json.loads(request_args)
    atributos = dict(consulta[0])
    #TODO Colocar loop para consultas de mais de uma questao
    result = Questao(**atributos)
    print("\n")
    session = Session()
    session.add(result)
    session.commit()
    return result

def viewQuestao(id=None):
    from model import Questao, Session
    session = Session()
    if not id:
        query = session.query(Questao).all()
        for result in query:
            print(result)
    else:
        query = session.query(Questao).filter(Questao.codigo)
        for result in query:
            print(result)
def addOcorrencia():
    #TODO Pegar os dados de tutor, id questao e horario para registro
    pass


