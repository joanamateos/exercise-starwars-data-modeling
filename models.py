import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    population = Column(Integer)
    gravity = Column(String(40))
    

    def to_dict(self):
        return {}

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    eye_color = Column(String(10))
    height = Column(Integer)

    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(40), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    def to_dict(self):
        return {}

class Favorites_pl(Base):
    __tablename__ = 'favorites_pl'
    user_id = Column(Integer, ForeignKey(User.id))
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    planet_name = Column(String(40), ForeignKey(Planet.name))

    def to_dict(self):
        return {}

class Favorites_pr(Base):
    __tablename__ = 'favorites_pr'
    user_id = Column(Integer, ForeignKey(User.id))
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    person_name = Column(String(25), ForeignKey(Person.name))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e