from typing import Dict
from cerberus import Validator, validator
import yaml
import json
import os

print()
with open ('multiservice.k8s-deployment.latest.yaml', 'r') as file:

    data = yaml.load(file, Loader=yaml.FullLoader)

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    with open (f) as file2:
        if "test_" in file2.name:
            strTestFileName = file2.name

            with open (strTestFileName, 'r') as schemafile:

                my_dictionary = yaml.load(schemafile, Loader=yaml.FullLoader)

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
            
        





