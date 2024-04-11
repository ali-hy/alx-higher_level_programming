#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()
    cur.execute('''SELECT cities.id, cities.name, states.name
                 FROM cities
                LEFT JOIN states ON cities.state_id = states.id
                ORDER BY cities.id;''')

    for _ in range(cur.rowcount):
        print(cur.fetchone())

    db.close()
