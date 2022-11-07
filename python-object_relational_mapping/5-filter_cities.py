#!/usr/bin/python3
'''
Takes in the name of a state as an argument and lists all cities of that state
using the atabase hbtn_0e_4_usa
'''


import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host="localhost", port=3306)
    cursor = db.cursor()
    arg4 = sys.argv[4]
    cursor.execute("""SELECT cities.name FROM cities, states WHERE
                   cities.state_id = states.id AND states.name = %s""",
                   (arg4,))
    states = []
    for i in cursor.fetchall():
        states.append(i[0])
    for i in range(0, len(states), 1):
        if i == len(states) or i == len(states) - 1:
            print(states[i])
        else:
            print(states[i], end=', ')
