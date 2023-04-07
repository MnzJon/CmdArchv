import json

def read_json(filepath):
    json_data = {}
    with open(filepath, "r") as jsonFile:
        data = json.load(jsonFile)

        json_data = data
    return json_data

def write_json(filepath, dictionary):
    with open(filepath, "r+") as jsonFile:
        jsonFile.seek(0)
        json.dump(dictionary, jsonFile)
        jsonFile.truncate()


