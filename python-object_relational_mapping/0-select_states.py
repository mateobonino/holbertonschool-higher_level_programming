#!/usr/bin/python3
'''
Lists the content of "states" table from "hbtn_0e_0_usa" database,
pass args via the command line to specify the user, password and database
'''
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host="localhost", port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * from states")
    states = cursor.fetchall()
    for i in states:
        print(i)
