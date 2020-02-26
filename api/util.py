# coding=utf-8

def loginApp(Usuario):
    try:
        Usuario.loginIntranet()
    except Exception as e:
        print("Nao foi possivel fazer login no sistema\nVerificar dados de usuario e senha.\n")
        print(e)

def serializaRequest(payload):
    # TODO colocar filtro de variaveis reservadas, para usuario nao ter acesso 
    import json
    try:
        dados_questao = json.loads(payload)
        dados_questao = json.dumps(dados_questao.get("data"))
        return dados_questao
    except Exception as e:
        print(e)

def printLog(browser_response):
    from bs4 import BeautifulSoup
    ''' Gera arq com respelho da resposta html.
    ex. printLog( BROWSER.response() ) '''
    from bs4 import BeautifulSoup
    bs = BeautifulSoup(browser_response.read(),'lxml')
    with open('log.html','w') as f:
        f.writelines(bs.prettify())

def _cadastraUSUARIO():
    '''O SISTEMA DE GESTAO DE BANCO DE QUESTOES NÃƒO FAZ CADASTRO DE USUARIO NEM FAZ QUALQUER TIPO
    DE CONTROLE DE PERMISSAO AO ACESSO DAS INFORMACOES DO SISTEMA DA UNICESUMAR. A UNICA FUNCAO
    DESEMPENHADA E O ACESSO A API DE CADASTRO DE QUESTOES PARA ENVIAR AS INFORMACOES AO SISTEMA
    DE FORMA MAIS EFICIENTE'''
    pass

def addQuestao(request_args):
    ''' os argumentos precisam vir como dicionario ou lista de dicionaro
    do requesta de consulta de questao '''
    from db.model import Questao, Session
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
    from db.model import Questao, Session
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

dic_alternativas = {
  "Objetiva de resposta múltipla": {
    "Fácil": {
      "payload_1": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "I, apenas.",
        "correta": 0
      },
      "payload_2": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "III, apenas.",
        "correta": 0
      },
      "payload_3": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "I e II, apenas.",
        "correta": 0
      },
      "payload_4": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "II e III, apenas.",
        "correta": 0
      },
      "payload_5": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "I, II e III.",
        "correta": 0
      }
    },
    "Médio": {
      " payload_1": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "I, apenas.",
        "correta": 0
      },
      "payload_2": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "II e IV, apenas.",
        "correta": 0
      },
      "payload_3": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "III e IV, apenas.",
        "correta": 0
      },
      "payload_4": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "I, II e III, apenas.",
        "correta": 0
      },
      "payload_5": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "I, II, III e IV.",
        "correta": 0
      }
    },
    "Difícil": {
      "payload_1": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "II e III.",
        "correta": 0
      },
      "payload_2": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "I e IV.",
        "correta": 0
      },
      "payload_3": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "II e III.",
        "correta": 0
      },
      "payload_4": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "I, II e IV.",
        "correta": 0
      },
      "payload_5": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "II, III e IV.",
        "correta": 0
      }
    }
  },
  "Objetiva de resposta única": {
    "Fácil": {
      "payload_1": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "I, apenas.",
        "correta": 0
      },
      "payload_2": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "III, apenas.",
        "correta": 0
      },
      "payload_3": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "I e II, apenas.",
        "correta": 0
      },
      "payload_4": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "II e III, apenas.",
        "correta": 0
      },
      "payload_5": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "I, II e III.",
        "correta": 0
      }
    },
    "Médio": {
      "payload_1": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "I, apenas.",
        "correta": 0
      },
      "payload_2": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "III, apenas.",
        "correta": 0
      },
      "payload_3": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "I e II, apenas.",
        "correta": 0
      },
      "payload_4": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "II e III, apenas.",
        "correta": 0
      },
      "payload_5": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "I, II e III.",
        "correta": 0
      }
    },
    "Difícil": {
      "payload_1": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "I, apenas.",
        "correta": 0
      },
      "payload_2": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "III, apenas.",
        "correta": 0
      },
      "payload_3": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "I e II, apenas.",
        "correta": 0
      },
      "payload_4": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "II e III, apenas.",
        "correta": 0
      },
      "payload_5": {
        "action": "inserir",
        "idQuestao": None,
        "dsAlternativa": "I, II e III.",
        "correta": 0
      }
    }
}}
