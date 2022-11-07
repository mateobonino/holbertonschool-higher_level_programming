#!/usr/bin/python3
'''
List all states with a name starting with N (upper)
'''

import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host="localhost", port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * from states WHERE name like 'N%'")
    result = cursor.fetchall()
    for i in result:
        print(i)
