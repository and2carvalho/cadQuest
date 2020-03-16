# CadQuest
Otimiza cadastro no banco de questões via comunicação direta API-Rest da intranet.


## Compilar executável:

1. Adicionar função resource_path() para direcionar o load para pasta temp;

2. Ajustar caminhos de arquivos estaticos com apenas o nome do arquivo sendo passado como parâmetro da função, por exemplo: resource_path("frequency_dictionary_pt_82_765.txt")

3. Adicionar arquivos estáticos no arquivo app.spec

4. `$ pyinstaller --onefile app.spec`

Inserir banco de dados na mesma pasta do executável
