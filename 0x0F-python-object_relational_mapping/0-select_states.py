#!/usr/bin/python3
"""  Script that gets all data from a database."""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # create a connection with the DataBase
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()  # Create an instance of database.
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()  # get all the rows.
    for row in rows:
        print(row)
    cur.close()  # Close all cursors.
    db.close()  # Close all databases.
