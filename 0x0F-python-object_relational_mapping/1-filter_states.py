#!/usr/bin/python3
'''script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa'''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()
    cur.execute('''SELECT * FROM states
                WHERE states.name LIKE BINARY "N%"
                ORDER BY states.id;''')

    for _ in range(cur.rowcount):
        print(cur.fetchone())

    cur.close()
    db.close()
