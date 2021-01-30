import os
import yaml
import json
from typing import Dict
from cerberus import Validator, validator


def per_section(it, is_delimiter=lambda x: x.isspace()):
    ret = []
    for line in it:
        if is_delimiter(line):
            if ret:
                yield ret  # OR  ''.join(ret)
                ret = []
        else:
            ret.append(line.rstrip())  # OR  ret.append(line)
    if ret:
        yield ret


print()

with open ('multiservice.k8s-deployment.latest.yaml', 'r') as file:

    data = yaml.load_all(file, Loader=yaml.FullLoader)

    for d in data:

        strFolder = d["kind"] + "_" + d["metadata"]["name"] 
        print ("-- " + strFolder + " --")
        print ()
        files = [f for f in os.listdir(strFolder) ]
        for f in files:
            if "test_" in f:
                #print(" + " + f)

                strTestFileName = f

                with open (strFolder + "/" + strTestFileName, 'r') as schemafile:

                    my_dictionary = yaml.load(schemafile, Loader=yaml.FullLoader)
                    #print (yaml.dump(my_dictionary))
                    v=Validator()
                    v.schema = my_dictionary

                    if v.validate(d):
                        print( '+ ' + strTestFileName + ' PASSED ' + u'\u2713')
                    else:
                        print('+ ' + strTestFileName + ' FAILED ' + u'\u2717')
                        print('\n  *********************************************************')
                        print("   Error Details: " + json.dumps(v.errors))
                        print('  *********************************************************\n')
        print()
 

#with open('multiservice.k8s-deployment.latest.yaml') as f:
#    sections = list(per_section(f, lambda line: line.startswith('---'))) # comment
#
#x=1
#
#for y in sections:
#    print(str(x) + ' ------------------------------')
#    data = yaml.safe_load(str(y))
#    
#    #
#    #print(type(str(y)))
#    print ( data[3]   )
#    print (yaml.dump(data))
#    
#    x=x+1
#
print()
