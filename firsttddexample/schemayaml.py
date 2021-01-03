#!/usr/bin/env python3

from cerberus import Validator
import yaml
import json

print()

with open('IsDockerComposeAtVersion3.json', 'r') as file:
    schema = file.read()

v = Validator()
v.schema = json.loads(schema)

print(" *DEBUG* Schema: " + schema)

with open('docker-compose.yml') as f:

    data = yaml.load(f, Loader=yaml.FullLoader)
    print(" *DEBUG* Yaml: " + data['version'])

    if v.validate({'version': data['version']}):
        print(' TEST PASSED')
    else:
        print(' TEST FAILED')
        print(v.errors)


print()




