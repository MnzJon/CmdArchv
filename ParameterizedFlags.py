import os
import json

class ParameterizedFlags():
    def __init__(self, path):
        self.path = path

    def setup(self):
        if os.path.exists(self.path) == False:
            f = open(self.path, "w")
            # Empty JSON 
            f.write('{}')
            f.close()

        return True

    def add_parameter(self, param):
        with open(self.path, "r+") as jsonFile:
            data = json.load(jsonFile)
            
            data[param] = True

            jsonFile.seek(0)  # rewind
            json.dump(data, jsonFile)
            jsonFile.truncate()

    def remove_parameter(self,param):
        with open(self.path, "r+") as jsonFile:
            data = json.load(jsonFile)
            
            data.pop(param)

            jsonFile.seek(0)  # rewind
            json.dump(data, jsonFile)
            jsonFile.truncate()

    def get_parameters(self):
        json_parameters = {}
        with open(self.path, "r") as jsonFile:
            data = json.load(jsonFile)
            json_parameters = data

        return json_parameters

