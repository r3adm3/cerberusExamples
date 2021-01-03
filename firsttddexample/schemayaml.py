#!/usr/bin/env python3

#Import all dependencies
from cerberus import Validator
import yaml
import json

#bit of formatting
print()

#I want an iterative loop to build a list of json files to read through
with open('test_IsDockerComposeAtVersion3.json', 'r') as file:
    schema = file.read()

#setup a cerberus validator
v = Validator()
#convert json schema to a python dict (cerberus req)
v.schema = json.loads(schema)

#some debug info. 
print(" *DEBUG* Schema: " + schema)

#open the file we want to test. 
with open('docker-compose.yml') as f:

    #load up an dict that contains all of our yaml data
    data = yaml.load(f, Loader=yaml.FullLoader)
    
    #bit more debug info, shows actual data in the part we're testing
    print(" *DEBUG* Inside the Yaml: " + data['version'])

    #and I want to some how functionalise this to iteratively test my yml file. 
    #TODO check the logic here, not convinced its actually testing what I want it to
    if v.validate({'version': data['version']}):
        print(' TEST PASSED')
    else:
        print(' TEST FAILED')
        print(v.errors)


print()




