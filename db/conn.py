# coding=utf-8

import sqlalchemy
import os

# necessário criar uma pasta no %userprofile%/appdata para que o executável
# consiga localizar o banco de dados.
dir_path = os.path.join(os.environ['APPDATA'], 'CadQuest')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
file_path = os.path.join(dir_path, 'db_questoes.db')
print(file_path)

try:
    db = sqlalchemy.create_engine("sqlite:///" + file_path )#mysql+pymysql://pyFeed:masterkey@localhost:3306/pyFeed
    print("Conexão com banco de dados realizada com sucesso!")
except Exception as e:
    print(e)