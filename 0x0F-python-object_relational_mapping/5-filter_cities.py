#!/usr/bin/python3
"""
script that takes the name of a state as an argument and lists all cities
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost'
    )
    cursor = db.cursor()
    query = """
            SELECT cities.name FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC;
            """
    cursor.execute(query, (sys.argv[4], ))

    cities = cursor.fetchall()

    i = 0
    for city in cities:
        if i != 0:
            print(", ", end="")
        print("%s" % city, end="")
        i += 1
    print("")

    cursor.close()
    db.close()
