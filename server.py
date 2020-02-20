from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import model
import json
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
# database teste -> so1teste | user -> rocknguns | psw -> masterkey
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://rocknguns:masterkey@db4free.net:3306/so1teste'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
session = model.Session()

@app.route('/')
def index():
    user=''
    loja=''
    return render_template('index.html', user=user,loja=loja)

    
@app.route('/lista_db')
def lista_db():
     # instancia modelo de ocorrencia
    col_bios = ['Processador', 'Qtd Núcleos','Memo Total','Memo Disp.',
                'Nome Maquina','Data Ocorencia']
    
    # armazena dados do banco ref a bios
    dic_bios = session.query(model.Questao).all()
    titulo_pag = 'Servidor Id_Diag  -  Consulta banco de dados'

    return render_template('lista_db.html',
                           titlo_pag = titulo_pag,
                           col_bios=col_bios,
                           dic_bios=dic_bios)

@app.route('/lista_db/<ocor_id>')
def detalha_ocor(ocor_id):
    
    col_proc = ['Processo Nome','Consumo Memoria','Consumo CPU']
    dic_proc = {}
    #busca ocorrencia pelo id passado
    query = session.query(model.Questao).filter(model.Questao.idQuestao == ocor_id)
    det_ocor = query.one()     
    return render_template('detalha_ocor.html',col_proc=col_proc,
                           det_ocor=det_ocor,dic_proc=dic_proc)   

#@app.teardown_request
#def finaliza_sessao(exception=None):
#    db.session.remove()

if __name__ == '__main__':
    app.run(debug=True)
    
