#!/usr/bin/env python3

from cerberus import Validator


schema = {'name': {'type': 'string'}}
v = Validator(schema)

document = {'name': 'john doe'}

if v.validate(document):
    print('data is valid')
else:
    print('invalid data')