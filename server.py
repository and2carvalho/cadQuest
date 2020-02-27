# coding=utf-8

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from db.model import Session, Questao
import json
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_questoes.db'#'mysql+pymysql://pyFeed:masterkey@localhost:3306/pyFeed'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
session = Session()

@app.route('/')
def index():
    user=''
    loja=''
    return render_template('index.html', user=user,loja=loja)

    
@app.route('/lista_db')
def lista_db():
     # instancia modelo de ocorrencia
    col_bios = ['Id Questao', 'Url Editar','Tema','dsUsuario',
                'dsComplexidade','dsSituacao','dsTipoDeQuestao', 'dtCriacao' ]

    # armazena dados do banco ref a bios
    dic_bios = session.query(Questao).all()
    titulo_pag = 'PyFeed - Consulta banco de dados'

    return render_template('lista_db.html',
                           titlo_pag = titulo_pag,
                           col_bios=col_bios,
                           dic_bios=dic_bios)

@app.route('/lista_db/<ocor_id>')
def detalha_ocor(ocor_id):
    
    col_proc = ['Processo Nome','Consumo Memoria','Consumo CPU']
    dic_proc = {}
    #busca ocorrencia pelo id passado
    query = session.query(Questao).filter(Questao.idQuestao == ocor_id)
    det_ocor = query.one()     
    return render_template('detalha_ocor.html',col_proc=col_proc,
                           det_ocor=det_ocor,dic_proc=dic_proc)   

#@app.teardown_request
#def finaliza_sessao(exception=None):
#    db.session.remove()

if __name__ == '__main__':
    app.run(debug=True)