import json

file = 'test_original.json'

def write_json(info, filename):
    with open(filename, "w") as f:
        json.dump(info, f, indent=4)
