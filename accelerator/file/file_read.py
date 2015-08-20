#!/usr/bin/python
# tested on python 3.4
# author : Samy Kacem

#'r' = read only
f = open('text.txt', 'r');

read_data = f.read();

print (read_data);
	
f.closed;
