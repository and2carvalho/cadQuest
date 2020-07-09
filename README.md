# CadQuest
Otimiza cadastro no banco de questões via comunicação direta API-Rest da intranet.


## Compilar executável:

Utilizar função resource_path() para direcionar o load para pasta temp:

1. Ajustar caminhos de arquivos estaticos com apenas o nome do arquivo sendo passado como parâmetro da função, por exemplo: resource_path("frequency_dictionary_pt_82_765.txt")
2. Conferir/adicionar arquivos estáticos no arquivo app.spec
3. `$ pyinstaller --onefile app.spec`

