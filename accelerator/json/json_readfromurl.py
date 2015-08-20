#!/usr/bin/python
# tested on python 3.4
# author : Samy Kacem

# Need to install https://github.com/kennethreitz/requests
# 1. download package
# 2. run install commend "setup.sy install"

# Using this public API http://coinabul.com/api.php

import requests;
import json;

response = requests.get('http://coinabul.com/api.php',auth=('user', 'password'));
data = response.json();

# Print the json content
print (data);

# Print more human readable
print (json.dumps(data, sort_keys=True, indent=4));

# Get all Gold data
print ("Get Gold values: ", data['Gold']);

# Get USD price of Gold
print ("Get Gold values in USD: ", data['Gold']['USD']);
