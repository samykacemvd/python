#!/usr/bin/python
# tested on python 3.4
# author : Samy Kacem
# Only on PC!!!!!!
# Install first https://pypi.python.org/pypi/pypyodbc

import pypyodbc;

# create db
pypyodbc.win_create_mdb('C:\\base.accdb');

conn = pypyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\base.accdb;Uid=Admin;Pwd=;');

#create table
cur = conn.cursor();

cur.execute('''CREATE TABLE users (
id AUTOINCREMENT PRIMARY KEY, 
lname VARCHAR(255),
fname VARCHAR(255),
email VARCHAR(255) ); ''') ;

cur.commit();

#add first data
cur.execute('''INSERT INTO users(fname,lname,email) VALUES(?,?,?)''',(u'John','Do','John.Do@gmail.com'));

cur.commit();

# Don't forget to close the connection
conn.close();
