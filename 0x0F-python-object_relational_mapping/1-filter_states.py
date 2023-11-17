#!/usr/bin/python3
"""
Lists all the states starting with N from the database hbtn_0e_0_usa
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
            WHERE CONVERT(`name` USING Latin1) 
            COLLATE Latin1_General_CS 
            LIKE 'N%';
            """
    cursor.execute(query)

    states = cursor.fetchall()
    for row in states:
        print(row)

    cursor.close()
    db.close()
