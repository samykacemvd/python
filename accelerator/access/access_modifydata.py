#!/usr/bin/python
# tested on python 3.4
# author : Samy Kacem
# Only on PC!!!!!!
# Install first https://pypi.python.org/pypi/pypyodbc

import pypyodbc;

# update the path depending on your environement
conn = pypyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\base.accdb;Uid=Admin;Pwd=;');

cur = conn.cursor();

# Insert
cur.execute('''INSERT INTO users(fname,lname,email) VALUES(?,?,?)''',(u'Tom','Jerry','tom.jerry@gmail.com'));

cur.commit();

# Update
cur.execute('''UPDATE users SET lname = 'Cat' WHERE id = 2 ''');

cur.commit();

# Delete
cur.execute('''DELETE * FROM users WHERE lname = 'Tom' ''');

cur.commit();

# Don't forget to close connection
conn.close();
