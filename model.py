import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base



def cria_banco(db):
    db = db
    try:
        metadata.create_all(db)
        print('Bando de Dados Criado')
    except:
        print('Não foi posssivel comunicar com o banco dados')

db = create_engine('sqlite:///db_questoes.db')
metadata = MetaData(bind=db)

usuario = Table('usuario', metadata,
        Column('codigo', Integer, primary_key=True),
        Column('nome', String(50)),
        Column('matricula', Integer),
        Column('ativo', Boolean, default=True))

questao = Table('questao', metadata,
        Column('id_registro', Integer, primary_key=True),
        Column('codigo', Integer),
        Column('tipo', String(100)),
        Column('origem', String(100)),
        Column('complexidade', String(100)),
        Column('destino', String(100)),
        Column('tema', String(100)),
        Column('pergunta', String(500)),
        Column('resposta', String(500)),
        Column('usuario_codigo', ForeignKey('usuario.codigo')))

#TODO if not db_questoes.db in __name__ directory: 
#cria_banco(db)
