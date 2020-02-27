# coding=utf-8

from sqlalchemy import create_engine

try:
    db = create_engine('sqlite:///db_questoes.db')#mysql+pymysql://pyFeed:masterkey@localhost:3306/pyFeed
    print("Conexão com banco de dados realizada com sucesso!")
except Exception as e:
    print(e)