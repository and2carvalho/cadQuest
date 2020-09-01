# CadQuest
Otimiza cadastro no banco de questões via comunicação direta API-Rest da intranet.


## Compilar executável:

Usar pipenv!
**ATENCAO** - pyinstaller não deve ser instalado globalmente para não incluir todos
os pacotes instalados no ambiente. Usar:
`pipenv install -d pyinstaller`

Utilizar função resource_path() para direcionar o load para pasta temp:

1. Ajustar caminhos de arquivos estaticos com apenas o nome do arquivo sendo passado como parâmetro da função, por exemplo: resource_path("frequency_dictionary_pt_82_765.txt")
2. Conferir/adicionar arquivos estáticos no arquivo app.spec
3. `$ pipenv run pyinstaller --onefile app.spec`
obs. O argumento `run` é utilizado para executar um comando à partir do ambiente virtual, isolando os demais pacotes do bounce

