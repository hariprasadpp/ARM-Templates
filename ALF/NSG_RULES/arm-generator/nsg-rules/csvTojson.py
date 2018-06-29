import csv
import json
import subprocess
import os

try:
    listOfCSVFilesToProcess = [files for files in os.listdir('.') if os.path.isfile(files)]
    listOfCSVFilesToProcess.remove('csvTojson.py')
    listOfCSVFilesToProcess.remove('armGenerator.py')

    for eachFiles in listOfCSVFilesToProcess:
        # Open the CSV
        f = open( eachFiles, 'rU' )
        ## removing header from a csv
        first_line = f.readline()
        # Change each fieldname to the      appropriate field name. I know, so difficult.
        reader = csv.DictReader( f, fieldnames = ( "name","sourceAddressPrefix","sourcePortRange","destinationAddressPrefix","destinationPortRange","protocol","direction","access","priority","description" ))
        # Parse the CSV into JSON
        out = json.dumps( [ row for row in reader ] )
        ##Formatting the security group
        unformatted_json = json.loads(out)
        formatted_json = []
        for eachElement in unformatted_json:
            formatElement = {}
            formatElement['name'] = eachElement['name']
            del eachElement['name']
            formatElement['properties'] = eachElement
            formatted_json.append(formatElement)
        formatted_output_json = json.dumps(formatted_json, indent=2)
        print "JSON parsed!"
        # Save the JSON
        outfilePath = "rulesConvertedToJson/" + eachFiles.split('.')[0] + ".json"
        f = open( outfilePath, 'w')
        f.write(formatted_output_json)
        print "JSON saved!"
    print "All CSV files are convereted to JSON Successfully !"
    
except Exception as e:
    print "Error captured : " + str(e)
