import json

def deconstruction_var_json(file):
    with open(file, 'r') as json_file:
        return json.load(json_file)

