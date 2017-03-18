# DataBaseTesting
Using [this website](https://goo.gl/j1Oril) to make these files.                                                                 
[Here](https://goo.gl/QS6FHO) is the python reference to sqlite3.

###Creating a new database in terminal
~~~~
$ sqlite3 test.db
SQLite version 3.7.13 2012-06-11 02:05:22
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
~~~~
Here, we provide a parameter to the sqlite3 tool; test.db is a database name. It is a file on our disk. If it is present, it is opened. If not, it is created.
~~~~
sqlite> .tables
sqlite> .exit
$ ls
test.db
~~~~
The .tables command gives a list of tables in the test.db database. There are currently no tables. The .exit command terminates the interactive session of the sqlite3 command line tool.
