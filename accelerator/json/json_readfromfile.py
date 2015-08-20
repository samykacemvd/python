#!/usr/bin/python
# tested on python 3.4
# author : Samy Kacem
# Need to install https://github.com/kennethreitz/requests
# 1. download package
# 2. run install commend "setup.sy install"

import json;
from pprint import pprint;

# Load from file
with open('json.txt') as data_file:    
    data = json.load(data_file);

pprint(data);

print (json.dumps(data, sort_keys=True, indent=4));

print ("Get Gold values: ", data['Gold']);

print ("Get Gold values in USD: ", data['Gold']['USD']);
