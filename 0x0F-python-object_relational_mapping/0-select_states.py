#!/usr/bin/python3
import MySQLdb
from sys import argv

db:MySQLdb.Connection = MySQLdb.connect(user=argv[1],
                     passwd=argv[2],
                     db=argv[3]
)

cur = db.cursor()
cur.execute('SELECT * FROM states;')

for _ in range(cur.rowcount):
    print(cur.fetchone())
