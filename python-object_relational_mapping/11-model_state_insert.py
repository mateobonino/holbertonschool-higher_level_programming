#!/usr/bin/python3
'''
Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
'''
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import sys
from model_state import State, Base
from sqlalchemy import insert


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    host = "localhost"
    engine = sqlalchemy.create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, passwd, host, database),
                                      pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State(name="Louisiana")
    print(newState.id)
    session.add(newState)
    session.commit()
