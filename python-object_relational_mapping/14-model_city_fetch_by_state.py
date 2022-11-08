#!/usr/bin/python3
'''
Prints all City objects from the database hbtn_0e_14_usa
'''
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import sys
from model_state import State, Base
from sqlalchemy import update
from model_city import City


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

    for i, j in session.query(City, State).filter(
                            City.state_id == State.id).all():
        print(f"{j.name}: ({i.id}) {i.name}")
