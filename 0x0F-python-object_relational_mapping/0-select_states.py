#!/usr/bin/python3
'''This script prints a list of all states in the given database'''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY states.id;')

    for _ in range(cur.rowcount):
        print(cur.fetchone())

    db.close()
