#!/usr/bin/python3
"""
    Script that gets all data that matches with an argument from a database.
    The argument is given in the Command Line.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Arguments to be used in the connetion with a database.
    db_date = {
        'host': "localhost",
        'port': 3306,
        'user': argv[1],
        'passwd': argv[2],
        'db': argv[3]
    }
    nm = argv[4]
    # create a connection with the DataBase
    db = MySQLdb.connect(**db_date)
    cur = db.cursor()  # Create an instance of database.
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY id".format(nm))
    # WHERE (name='{}') != (LIKE BINARY '{}' = ("name='{}'".format(nm) +"BY id"
    rows = cur.fetchall()  # get all the rows.
    for row in rows:
        print(row)
    cur.close()  # Close all cursors.
    db.close()  # Close all databases.
