<h1 align="center"> CadQuest </h1>
<p align="center">Otimiza cadastro no banco de questões via comunicação direta API-Rest da intranet.</p>

<br>
<div align="center">
![Python badge](https://img.shields.io/badge/-python-1572B6?style=flat-square&logo=python&logoColor=white)
</div>
<br>

Conteúdo
===========

<p align="center">
<a href="#descrição">Descrição</a> |
<a href="#instalação">Instalação</a> |
<a href="#compilação">Executável</a>
</p>

====================================
<br>
<div align="center">
<img src="https://and2carvalho.github.io/images/portfolio/cadQuest-1.jpg">
</div>
<br>

## Descrição

Programa desenvolvido para otimizar o processo de cadastro de questões de provas e atividades no banco de dados interno da Universidade.

### Problemas Solucionados 

- Lentidão para acessar o portal da instituição e realizar todo o “caminho” até o link de acesso ao banco de questões.

- Necessidade do usuário inserir a mesma informação mais de uma vez no processo de cadastro de questão.

- Falta de padronização no preenchimento de alternativas da questão (toda nova questão o usuário precisa adicionar o campo e digitar o valor de cada alternativa mesmo essas alternativas sendo padronizadas de acordo com o nível e tipo de questão cadastrada).

## Instalação

```shell
$ git clone https://and2carvalho/cadQuest
$ cd cadQuest
$ pipenv shell
$ python app.py
```

## Compilação


**ATENCAO** - pyinstaller não deve ser instalado globalmente para não incluir todos
os pacotes instalados no ambiente. Usar:
`pipenv install -d pyinstaller`

Utilizar função resource_path() para direcionar o load para pasta temp:

1. Ajustar caminhos de arquivos estaticos com apenas o nome do arquivo sendo passado como parâmetro da função, por exemplo: resource_path
("frequency_dictionary_pt_82_765.txt")

2. Conferir/adicionar arquivos estáticos no arquivo app.spec

3. `$ pipenv run pyinstaller --onefile app.spec`

<br>

### Autor
---

<div align="center">
<a href="https://and2carvalho.github.io">
 <img style="border-radius: 30%;" src="https://and2carvalho.github.io/images/profilepic.jpg" width="100px;" alt=""/>
 <br />
 <sub><b>and2carvalho</b></sub></a>

<br>

Feito com ❤️ por André C. A. de Carvalho.<br>
Entre em contato!

[![Gmail Badge](https://img.shields.io/badge/-and2carvalho@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:and2carvalho@gmail.com)](mailto:and2carvalho@gmail.com)
[![Linkedin Badge](https://img.shields.io/badge/-André_Carvalho-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/andré-carvalho-465ab664/)](https://www.linkedin.com/in/andré-carvalho-465ab664/)