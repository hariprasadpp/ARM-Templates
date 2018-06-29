import json

try:
    print "Read NSG base template"
    armTemplate = json.load(open('template/template.json'))

    for eachResource in armTemplate['resources']:
        if "WAFSubnet" in eachResource['name']:
            gatewaySecurityRules = eachResource['properties']['securityRules']
            gatewayRules = json.load(open('rulesConvertedToJson/WAFSubnet_NSG.json'))
            eachResource['properties']['securityRules'] = gatewayRules

        if "DMZSubnet" in eachResource['name']:
            gatewaySecurityRules = eachResource['properties']['securityRules']
            gatewayRules = json.load(open('rulesConvertedToJson/DMZSubnet_NSG.json'))
            eachResource['properties']['securityRules'] = gatewayRules

        if "WebSubnet" in eachResource['name']:
            gatewaySecurityRules = eachResource['properties']['securityRules']
            gatewayRules = json.load(open('rulesConvertedToJson/WebSubnet_NSG.json'))
            eachResource['properties']['securityRules'] = gatewayRules

        if "DataSubnet" in eachResource['name']:
            gatewaySecurityRules = eachResource['properties']['securityRules']
            gatewayRules = json.load(open('rulesConvertedToJson/DataSubnet_NSG.json'))
            eachResource['properties']['securityRules'] = gatewayRules

        if "ManagementSubnet" in eachResource['name']:
            gatewaySecurityRules = eachResource['properties']['securityRules']
            gatewayRules = json.load(open('rulesConvertedToJson/ManagementSubnet_NSG.json'))
            eachResource['properties']['securityRules'] = gatewayRules

    with open('generatedArmTemplate/template.json', 'w') as outfile:
        json.dump(armTemplate, outfile, indent=2)

    print "Arm template for NSG is successfully generated !"

except Exception as e:
    print "Error captured : " + str(e)
