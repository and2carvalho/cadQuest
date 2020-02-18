# coding=utf-8

def loginApp(Usuario):
    try:
        Usuario.loginIntranet()
    except Exception as e:
        print("NÃ£o foi possÃ­vel fazer login no sistema\nVerificar dados de usuario e senha.")
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
    '''O SISTEMA DE GESTAO DE BANCO DE QUESTOES NÃƒO FAZ CADASTRO DE USUARIO NEM FAZ QUALQUER TIPO
    DE CONTROLE DE PERMISSAO AO ACESSO DAS INFORMACOES DO SISTEMA DA UNICESUMAR. A UNICA FUNCAO
    DESEMPENHADA Ã‰ O ACESSO Ã€ API DE CADASTRO DE QUESTOES PARA ENVIAR AS INFORMACOES AO SISTEMA
    DE FORMA MAIS EFICIENTE'''
    pass

def addQuestao(request_args):
    ''' os argumentos precisam vir como dicionario ou lista de dicionaro
    do requesta de consulta de questao '''
    from model import Questao, Session
    import json
    consulta = json.loads(request_args)
    for i in range(len(consulta)):
        atributos = dict(consulta[i]) 
        session = Session()
        questao = Questao(**atributos)
        query = session.query(Questao).filter(Questao.idQuestao == questao.idQuestao)
        result = query.one_or_none()
        if result:   # verifica se já exite o cadastro da questao
            print("\nQuestao {} ja cadastrada".format(questao.idQuestao))
            try:
                session.merge(result)
                session.commit()
                print("Questao {} atualizada com sucesso\n".format(questao.idQuestao))
            except Exception as e:
                print(e)
        else:
            try:
                session.add(questao)
                session.commit()
                print("\nQuestao {} adicionado ao banco de dados".format(questao.idQuestao))
            except Exception as e:
                print(e)

def viewQuestao(id=None):
    from model import Questao, Session
    session = Session()
    if not id:
        try:
            query = session.query(Questao)
            result = query.all()
            for questao in result:
                print(questao)
        except Exception as e:
            print(e)
    else:
        try:
            query = session.query(Questao).filter(Questao.idQuestao == id )
            result = query.one()
            print(result)
        except Exception as e:
            print(e)
            
def addOcorrencia():
    #TODO Pegar os dados de tutor, id questao e horario para registro
    pass
