#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
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
            SELECT *
            FROM states
            WHERE name = %s
            ORDER BY id ASC;
            """

    cursor.execute(query, (sys.argv[4],))
    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close
