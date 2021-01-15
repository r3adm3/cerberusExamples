#!/usr/bin/env python3

#Import all dependencies
from typing import Dict
from cerberus import Validator
import yaml
import json
import os

#bit of formatting
print()



def runme ( strTestFileName, strYamlFileName ):

    #print ("  *DEBUG FN* In function" )
    #print ("  *DEBUG FN* File Name: " + strTestFileName)
    #print ("  *DEBUG FN* str3: " + strYamlFileName)

    # read the schema into the cerberus validator
    # convert the schema to a variable
    with open(strTestFileName, 'r') as file3:
        testschema = file3.read()

    v = Validator()
    v.schema = json.loads(testschema)

    # open the yaml we're going to cross check
    with open (strYamlFileName, 'r') as file:

        data = yaml.load(file, Loader=yaml.FullLoader)

       # print ("  *DEBUG FN* schema: " + testschema)
       # print ("  *DEBUG FN* Inside the Yaml: " + data['version'])
        
        # location of the value in the yaml
        #val1 = 'version'

        # getting the value we're testing for from the json
        jsonlist = testschema.split("{")
        val1 = ((jsonlist[1]).replace('":', ''))
        val1 = (val1.replace('"', ''))
        
        # here's the value we're testing for
        val1 = (val1.replace(' ', ''))
        print (len(jsonlist))
        print (jsonlist)
        print (val1)

        val4 = 0
   
        for x in range (0, len(jsonlist)):
            print (jsonlist[x])
            if "type" in jsonlist[x] :
                val4 = x


        print()
        #print("val4:" + val4)

        #this works in simplest case val2 = data[val1]
        #locator = "['services']['addsvc']['build']"
        #print(data[locator])

        #if v.validate({val1: val2}):
        #    print( ' ' + strTestFileName + ' PASSED ' + u'\u2713')
        #else:
        #    print(' ' + strTestFileName + ' FAILED ' + u'\u2717')
        #    print(" Error Details: " + json.dumps(v.errors))

        print()
    #print ("  *DEBUG FN* End function" )



#iterating loop getting all files with name starting test_
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    with open (f) as file2:
        if "test_" in file2.name:
            #print( " *DEBUG* File: " + os.path.basename(file2.name))
            runme(os.path.basename(file2.name), "docker-compose.yml")
            #print()


print()
