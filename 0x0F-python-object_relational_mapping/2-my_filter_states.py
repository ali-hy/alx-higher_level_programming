#!/usr/bin/python3
'''Script that selects all states matching a name entered in the command'''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()
    cur.execute('SELECT * FROM states '
                + f'WHERE states.name = "{argv[4]}" '
                + 'ORDER BY states.id;')

    if not cur.rowcount:
        exit(1)

    for _ in range(cur.rowcount):
        print(cur.fetchone())

    db.close()
