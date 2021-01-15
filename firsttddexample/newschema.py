from typing import Dict
from cerberus import Validator, validator
import yaml
import json

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
"""

my_dictionary = yaml.load(raw_schema_yaml, Loader=yaml.FullLoader)

with open ('docker-compose.yml', 'r') as file:

    data = yaml.load(file, Loader=yaml.FullLoader)

v=Validator()
v.schema = my_dictionary

result = v.validate(data)

print(result)
print(json.dumps(v.errors, indent=2))