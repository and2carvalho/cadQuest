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

def dbQuestao(request_args):
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
      "payload_1": {
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
# apesar desse dic buscar seguir o padrão da api
# algumas chaves foram adaptadas para os widget 
#encaixarem melhor nas dim. do app.
dic_tags = {
    "idNodeMacro34" : {
        "SIM" : "131",
        "NÃO" : "132"
    },
    "idNodeMacro8" : {
        "Atv1" : "52",
        "Atv2" : "53",
        "Atv3" : "54",
        "Mapa" : "58",
        "ATIVIDADE INTEGRADA" : "62",
        "FÓRUM" : "63",
        "Atv4" : "70",
        "Atv5" : "90",
        "Atv6" : "139",
        "Atv7" : "140",
        "QUIZ" : "146",
        "EAD GIRO" : "147",
        "PROVA" : "161",
        "MAPA SUB" : "163",
    },
    "idNodeMacro30" : {
        "TEO" : "91",
        "TEOL" : "92",
        "AGRO" : "93",
        "CCONT" : "94",
        "GPUB" : "95",
        "ENG. PROD." : "96",
        "ENG. SOFT." : "97",
        "EDU" : "98",
        "GRH" : "99",
        "ADS" : "100",
        "SI" : "101",
        "DM" : "102",
        "DI" : "103",
        "ADM" : "104",
        "PGER" : "105",
        "MKT" : "106",
        "MAT" : "107",
        "HIST" : "108",
        "SEG. TRAB." : "109",
        "PED" : "110",
        "GAMB" : "111",
        "GEO" : "112",
        "T.I" : "113",
        "GPV" : "114",
        "GFIN" : "115",
        "GASTRO" : "116",
        "GCOM" : "117",
        "GIMOB" : "118",
        "LET" : "119",
        "LOG" : "120",
        "SEC" : "121",
        "GH" : "122",
        "DP" : "123",
        "SSOC" : "124",
        "GC" : "125",
        "GQ" : "126",
        "GTS" : "127",
        "ECON" : "128",
        "CURSO DE ORIGEM" : "129",
        "EMP" : "130",
        "BEDU" : "133",
        "ECIV" : "134",
        "EELE" : "135",
        "EMEC" : "136",
        "EMCA" : "137",
        "HEPROD" : "138",
        "HÍBRIDO" : "143",
        "FSCE" : "144",
        "PROJETO DE ENSINO" : "145",
        "SPRIV" : "148",
        "ARTV" : "149",
        "CBIO" : "150",
        "PSICO" : "151",
        "PCERV" : "152",
        "SALI" : "153",
        "FIL" : "154",
        "SOCIO" : "155",
        "ECOS" : "156",
        "POD" : "157",
        "TINT" : "158"
    },
    "idMacroNode1" : {
        "MÓDULO 51" : "1",
        "MÓDULO 52" : "2",
        "MÓDULO 53" : "3",
        "MÓDULO 54" : "4"
    },
    "idMacroNode2" : {
        "Unidade I" : "10",
        "Unidade II" : "11",
        "Unidade III" : "12",
        "Unidade IV" : "13",
        "Unidade V" : "14",
        "Unidade VI" : "32",
        "Unidade VII" : "33",
        "Unidade VIII" : "141",
        "Unidade IX" : "142"
    },
    "idMacroOrigem" : {
        "LIVRO NÚCLEO COMUM" : "1",
        "AULA AO VIVO - NÚCLEO ESPECÍFICO" : "3",
        "AULA CONCEITUAL - NÚCLEO ESPECÍFICO" : "4",
        "MATERIAL EXTRA - NÚCLEO ESPECÍFICO" : "5",
        "ESTUDO DE CASO - NÚCLEO ESPECÍFICO" : "6",
        "COLETÂNEA - NÚCLEO ESPECÍFICO" : "7",
        "APOSTILA - NÚCLEO ESPECÍFICO" : "8",
        "AULA PRESENCIAL" : "9",
        "LIVRO NÚCLEO ESPECÍFICO" : "10",
        "DESAFIO PRESENCIAL" : "12"
    },
    "idMacroTipoQuestao" : {
        "Objetiva de resposta única" : "1",
        "Objetiva de resposta única com afirmação incompleta" : "2",
        "Objetiva de resposta múltipla" : "3",
        "Objetiva de falso ou verdadeiro" : "4",
        "Objetiva de completar lacuna" : "5",
        "Objetiva de associação" : "6",
        "Objetiva de interpretação" : "7",
        "Objetiva de asserção e razão" : "8"
    }
}