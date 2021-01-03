#!/usr/bin/env python3

from cerberus import Validator
import yaml
import json
#v.schema = {'cities': {'type': 'list', 'schema': {'type': 'string'}}}
print()

with open('schema.json', 'r') as file:
    schema = file.read()

v = Validator()
v.schema = json.loads(schema)

print(" *DEBUG* Schema: " + schema)

with open('cities.yaml') as f:

    data = yaml.load(f, Loader=yaml.FullLoader)
    print(" *DEBUG* Yaml: " + data['cities'][0])

    if v.validate({'cities': data['cities']}):
        print('valid data')
    else:
        print('invalid data')
        print(v.errors)

print()




