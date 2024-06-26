#!/usr/bin/python3
'''Script that gets all cities in a certain state (entered as arg)'''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()
    cur.execute('''SELECT cities.name
                 FROM cities
                LEFT JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id;''', (argv[4], ))

    print(", ".join(map(lambda t: t[0], cur.fetchall())))

    db.close()
