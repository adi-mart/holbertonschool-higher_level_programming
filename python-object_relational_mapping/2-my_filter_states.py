#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server on localhost:3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name,
                         states=state_name)
    cur = db.cursor()

    # Execute query and fetch results sorted by id (ascending)
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC")
    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
