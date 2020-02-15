
from usuario import Usuario
from servidor import loginApp, serializaRequest

if __name__ == "__main__":
    
    tutor = Usuario()
    loginApp(tutor)
    tutor.acessaFrmQuestao()
    codigo_questao = input("\n\nDigite o(s) código(s) da(s) questao(oes).\nse nao souber digite 208454\n\n"+9*"-"+">  \n")

    dados_questao = tutor.requestQuestao(codigo_questao)
    result = serializaRequest(dados_questao)
    import json
    consulta = json.loads(result)
    for questao in consulta:
        print(questao)
        print("\n")
    input("Aperte uma tecla para finalizar")
    # link para novo cadastro de questoes
    #l_formNovoCadatro = br.find_link(nr=17)
