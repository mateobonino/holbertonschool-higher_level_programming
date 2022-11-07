#!/usr/bin/python3
'''
Defines a State class and an instance
Base = declarative_base().
Creates a link to the states table
'''
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    '''
    Defines a State class and creates a link
    to the states table
    '''
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
