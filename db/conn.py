
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
  
    
db = create_engine('sqlite:///db_questoes.db')
Session = sessionmaker(bind=db)

Base = declarative_base()
