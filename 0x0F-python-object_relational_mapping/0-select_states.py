#!/usr/bin/python3
"""Script lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":

    conx = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    # Start cursor
    cursor = conx.cursor()

    # Query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cursor.fetchall()

    # Print query
    for row in query_rows:
        print(row)

    # Close cursor
    cursor.close()
    conx.close()
