#!/usr/bin/python3
'''
Lists all 'State' objects that contain the letter 'a'
from the database 'hbtn_0e_6_usa'
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
                                      pool_pre_engine=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id).all()
    for i in result:
        if "a" in i.name:
            print(f"{i.id}: {i.name}")
