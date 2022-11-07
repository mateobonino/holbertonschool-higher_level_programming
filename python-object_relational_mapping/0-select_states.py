#!/usr/bin/python3
import MySQLdb
import sys

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], host="localhost", port=3306)

cursor = db.cursor()
cursor.execute("SELECT * from states")
states = cursor.fetchall()
for i in states:
    print(i)
