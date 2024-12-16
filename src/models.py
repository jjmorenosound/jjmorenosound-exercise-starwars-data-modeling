import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
  
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250), primary_key=True)

class Character(Base):
    __tablename__ = 'character'
  
    id = Column(Integer, primary_key=True)
    stars = Column(Integer)
    bio = Column(String(1000))
    character_by_user_id = Column(Integer, ForeignKey('user.id'))
  

class Planet(Base):
    __tablename__ = 'planet'
  
    id = Column(Integer, primary_key=True)
    stars = Column(Integer)
    description = Column(String(1000))
    planet_by_user_id = Column(Integer, ForeignKey('user.id'))
    
    
class Favorites(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    planet_by_id = Column(Integer, ForeignKey('planet.id'))
    character_by_id = Column(Integer, ForeignKey('character.id'))
    
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
