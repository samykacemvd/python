#!/usr/bin/python
# tested on python 3.4
# author : Samy Kacem
# Only on PC!!!!!!
# Install first https://pypi.python.org/pypi/pypyodbc

import pypyodbc;

# update the path depending on your environement
conn = pypyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\base.accdb;Uid=Admin;Pwd=;');

cur = conn.cursor();

cur.execute('''SELECT * FROM users ''');

# Display column name
print ("\n\nColumn list :");
for d in cur.description:
    print (d[0]);

# Display the full list of users
print ("\n\nData full list :");	
for row in cur.fetchall():
    for field in row: 
        print (field); # , print ('');

# Display the frist row		
cur.execute('''SELECT * FROM users WHERE id = 1 ''');
print ("\n\nShow 1 row :");
for row in cur.fetchall():
	id = row [0];
	fname = row [1];
	lname = row[2];
	email = row[3];
	print (id, fname, lname, email );

# Don't forget to close the connection
conn.close();

