# CadQuest
Otimiza cadastro no banco de questões via comunicação direta API-Rest da intranet.

Problemas Solucionados: Lentidão para acessar o portal da instituição e realizar todo o “caminho” até o link de acesso ao banco de questões;
Falta de padronização no preenchimento de alternativas da questão (toda nova questão o usuário precisava adicionar o campo referente a cada alternativa no portal e digitar o valor, mesmo essas alternativas sendo padronizadas).

O programa fornece a possibilidade de padronizar cadastro de alternativas de forma automática, variando de acordo com as opções de tipo de questão preenchidas incialmente pelo usuário.

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

