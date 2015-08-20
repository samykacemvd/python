#!/usr/bin/python
# tested on python 3.4
# author : Samy Kacem
# Only on PC!!!!!!
# Install first https://pypi.python.org/pypi/pypyodbc

import pypyodbc;

pypyodbc.win_compact_mdb('C:\\base.accdb','C:\\base_backup.accdb');
