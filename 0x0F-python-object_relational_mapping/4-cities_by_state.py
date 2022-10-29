#!/usr/bin/python3
"""
    Script that gets all data from a table
    and print all states that  matches with other table.
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

    # create a connection with the DataBase
    db = MySQLdb.connect(**db_date)
    cur = db.cursor()  # Create an instance of database.
    cur.execute("SELECT cities.id, cities.name, states.name\
                 FROM cities INNER JOIN states\
                 ON cities.state_id = states.id \
                 ORDER BY cities.id")
    rows = cur.fetchall()  # get all the rows.
    for row in rows:
        print(row)
    cur.close()  # Close all cursors.
    db.close()  # Close all databases.
