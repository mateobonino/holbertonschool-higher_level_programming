#!/usr/bin/python3
'''
Defines a City class and an instance
Base = declarative_base().
Creates a link to the cities table
'''
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    '''
    Defines a State class and creates a link
    to the states table
    '''
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
