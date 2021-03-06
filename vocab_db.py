from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Dict(Base):
    __tablename__ = 'Dict'
    id = Column(Integer, primary_key=True)
    word = Column(String(30), nullable=True)
    definition = Column(String(250), nullable=True)


    @property
    def serialize(self):
        return {
                'id': self.id,
                'word': self.word,
                'definition': self.definition,
               }

class Games(Base):
    __tablename__ == 'Games'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=True)

    def serialize(self):
        return {
              'id': self.id,
              'name': self.word,

        }

engine = create_engine('sqlite:///Dictionary.db')
Base.metadata.create_all(engine)