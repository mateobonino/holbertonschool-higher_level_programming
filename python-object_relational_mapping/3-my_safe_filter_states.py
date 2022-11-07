#!/usr/bin/python3
'''
Script safe from SQL injections

'''


import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host="localhost", port=3306)
    cursor = db.cursor()
    arg4 = sys.argv[4]
    cursor.execute(f"SELECT * FROM states WHERE BINARY name = %s" % (arg4,))
    for i in cursor.fetchall():
        print(i)
