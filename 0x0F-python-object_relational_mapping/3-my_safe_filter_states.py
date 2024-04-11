#!/usr/bin/python3
'''Script that filters states by the name entered in the command but safely'''
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
                WHERE states.name LIKE BINARY %s
                ORDER BY states.id;''', (argv[4], ))

    if not cur.rowcount:
        exit(1)

    for _ in range(cur.rowcount):
        print(cur.fetchone())

    db.close()
