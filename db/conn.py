# coding=utf-8

from sqlalchemy import create_engine

try:
    db = create_engine('mysql+pymysql://rocknguns:masterkey@db4free.net:3306/so1teste')#'mysql+pymysql://pyFeed:masterkey@localhost:3306/pyFeed'))
    print("Conexão com banco de dados realizada com sucesso!")
except Exception as e:
    print(e)