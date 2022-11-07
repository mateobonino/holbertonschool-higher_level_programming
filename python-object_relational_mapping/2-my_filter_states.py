#!/usr/bin/python3
'''
Takes an argument and displays all values in the states table where name
matches the argument
'''

import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host="localhost", port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name = '{}'"
                   .format(sys.argv[4]))
    result = cursor.fetchall()
    for i in result:
        print(i)
