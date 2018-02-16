#!bin/python3

import ruamel.yaml as yaml
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open("resources.yaml") as stream:
    try:
        yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

with open("resources.yaml") as stream:
    resources_file = yaml.safe_load(stream)

resources = resources_file['Resources']
attributes = resources_file['Attributes']

for resource in resources:
    print(resource)

#pprint.pprint(resources)
