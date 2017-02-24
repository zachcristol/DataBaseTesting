#!/usr/bin/python
# -*- coding: utf-8 -*-

# This script creates a Cars table and inserts 8 rows into the table.





import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con:

    cur = con.cursor()
    # creates a new Cars table. The table has three columns ?I think they are called ID,
    # Name, and Price and the INT and TEXT are the data types
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    # Inserts a new car row with the values(data for column1, data for column2, data for column3)
    cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
    cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
    cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
    cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
    cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
    cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
    cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
    cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")

    # Note** the 'with' keyword is allowing the changes are automatically committed. Otherwise, we would have to commit them manually
