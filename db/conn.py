# coding=utf-8

import sqlalchemy
import os
from datetime import datetime

# necessário criar uma pasta no %userprofile%/appdata para que o executável
# consiga localizar o banco de dados.
#dir_path = os.path.join(os.path.join(os.environ['APPDATA'], 'CadQuest')
dir_path = '~/Documents/code_projetos/pyFeed'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
file_path = os.path.join(dir_path, 'db_questoes.db')
print(file_path)

try:
    db = sqlalchemy.create_engine("sqlite:///" + file_path )#mysql+pymysql://pyFeed:masterkey@localhost:3306/pyFeed
    print("Conexão com banco de dados realizada com sucesso!")
except Exception as e:
    now = datetime.now()
    logf = open(dir_path+"log.txt","a+")
    logf.write(now.strftime("%H:%M:%S") + " - " + str(e) + "\n")
    logf.close()