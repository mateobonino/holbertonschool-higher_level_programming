#!/usr/bin/python3
'''
Print the first State object from
the database hbtn_0e_6_usa
'''
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import sys
from model_state import State, Base

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
    for j in session.query(State).order_by(State.id).all():
        print("{}; {}".format(j.id, j.name))
        break
