#!/usr/bin/python
# tested on python 3.4
# author : Samy Kacem

import datetime;
import time;

i = datetime.datetime.now();

# 'a' = append  'w' = overide the current content
f = open('text.txt', 'a');

f.write("test " + str(i) + "\n");

f.close();
