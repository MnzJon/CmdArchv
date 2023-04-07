
import json
import os

class FavouritesStorage():
    def __init__(self, path):
        self.path = path

    def setup(self):
        if os.path.exists(self.path) == False:
            f = open(self.path, "w")
            # Empty JSON 
            f.write('{}')
            f.close()

        return True

    def store_favourite(self,cmd, f_id):
        with open(self.path, "r+") as jsonFile:
            data = json.load(jsonFile)

            data[f_id] = cmd.to_dictionary()

            jsonFile.seek(0)  # rewind
            json.dump(data, jsonFile)
            jsonFile.truncate()

    def select_favourite(self, f_id):
        json_favourite = {}
        with open(self.path, "r") as jsonFile:
            data = json.load(jsonFile)

            json_favourites = data[f_id]

        return json_favourite

    def get_favourites(self):
        json_favourites = {}
        with open(self.path, "r") as jsonFile:
            data = json.load(jsonFile)

            json_favourites = data

        return json_favourites

