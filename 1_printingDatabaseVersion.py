#!/usr/bin/python
# -*- coding: utf-8 -*-


#The sqlite3 module is used to work with the SQLite database.
import sqlite3 as lite
import sys

con = None

try:
    # Here we connect to the test.db database. The connect() method returns a connection object.
    con = lite.connect('test.db')

    # From the connection, we get the cursor object. The cursor is used to traverse the records from the result set
    cur = con.cursor()
    # We call the execute() method of the cursor and execute the SQL statement
    cur.execute('SELECT SQLITE_VERSION()')

    # We fetch the data. Since we retrieve only one record, we call the fetchone() method.
    data = cur.fetchone()

    # We print the data that we have retrieved to the console.
    print "SQLite version: %s" % data

except lite.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()
