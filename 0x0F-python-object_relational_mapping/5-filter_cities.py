#!/usr/bin/python3
"""
    Script that gets all data from a table that matches
    with an argument from other table.
    and print all states that  matches with other table.
    Now the SELECT instruction is safe.
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
    cur.execute("SELECT cities.name\
                 FROM cities INNER JOIN states \
                 ON cities.state_id = states.id \
                 WHERE states.name = %s \
                 ORDER BY cities.id", (nm,))

    rows = cur.fetchall()  # get all the rows.
    print(", ".join(row[0] for row in rows))
    cur.close()  # Close all cursors.
    db.close()  # Close all databases.
