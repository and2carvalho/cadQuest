# coding=utf-8
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
  
    
db = create_engine('sqlite:///db_questoes.db')
Session = sessionmaker(bind=db)

Base = declarative_base()

class Tutor(Base):
    __tablename__ = 'tutor'

    codigo = Column(Integer, primary_key=True)
    login = Column(String(50))
    dtAcesso = Column(Date)

class Questao(Base):
    
    __tablename__= 'questao'

    codigo = Column(Integer(), primary_key=True)
    idQuestao =  Column(Integer)
    tema = Column(String(100))
    dsComplexidade = Column(String(50))
    dsUsuario = Column(String(100))
    dtCriacao = Column(String(30))
    dsNodeRaiz = Column(String(50))
    idSituacao = Column(Integer())
    dsSituacao = Column(String(50))
    ativoDesc = Column(String(30))
    id_tema = Column(Integer)
    dsTipoQuestao = Column(String(100))
    dsOrigem = Column(String(50))
    urlVisualizar = Column(String(250))
    btnVisualizar = Column(String(250))
    cryp_editar = Column(String(250))
    btnEditar = Column(String(250))
    cryp_aprovar = Column(String(250))
    cryp_rejeitar = Column(String(250))
    cryp_publicar = Column(String(250))

class Ocorrencia(Base):
    __tablename__ = 'ocorrencia'

    ocor = Column(Integer, primary_key=True)
    #dtAcessoCodigo = Column(ForeignKey('tutor.dtAcesso'))
    dtOcor = Column(Date, nullable=False)
    idQuestaoCodigo = Column(ForeignKey('questao.idQuestao'))
    idQuestao = relationship(Questao)
    tutorCodigo = Column(ForeignKey('tutor.codigo'))
    tutor = relationship(Tutor)
    atividade = Column(String(100))


#TODO if not db_questoes.db in __name__ directory: 
#cria_banco(db)

#Base.metadata.create_all(db)