from typing import Dict
from cerberus import Validator, validator
import yaml
import json
import os

strTestFileName = 'test_frontendDefinedProperly.yml'

with open (strTestFileName, 'r') as schemafile:

    my_dictionary = yaml.load(schemafile, Loader=yaml.FullLoader)

raw_schema_yaml = """
version:
  type: string
services:
  type: dict
  schema:
    addsvc:
      type: dict
      schema:
        build:
          type: string
        ports:
          allowed: ['18081:80']
        environment:
          allowed: ['ASPNETCORE_ENVIRONMENT=Development']
    frontend:
      type: dict
      nullable: true
    minussvc:
      type: dict
      nullable: true
    multiplysvc:
      type: dict
      nullable: true
"""

#my_dictionary = yaml.load(raw_schema_yaml, Loader=yaml.FullLoader)

with open ('docker-compose.yml', 'r') as file:

    data = yaml.load(file, Loader=yaml.FullLoader)

v=Validator()
v.schema = my_dictionary

if v.validate(data):
    print( '+ ' + strTestFileName + ' PASSED ' + u'\u2713')
else:
    print('+ ' + strTestFileName + ' FAILED ' + u'\u2717')
    print('\n  *********************************************************')
    print("   Error Details: " + json.dumps(v.errors))
    print('  *********************************************************\n')
print()

#result = v.validate(data)

#print(result)
#print(json.dumps(v.errors, indent=2))