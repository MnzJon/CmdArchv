import json
import os
from datetime import datetime

#
#
#   { recent: {IDO: --cmd--},
#     past: { "ID0": { CMD }, "ID0": {CMD}}
#   
#   }
#
#
#


class HistoryStorage():
    def __init__(self, path):
        self.path = path

    def setup(self):
        if os.path.exists(self.path) == False:
            f = open(self.path, "w")
            # Empty JSON 
            f.write('{ "recent": {}, "past": {}}')
            f.close()

        return True

    def store_cmd(self,cmd):
        now = datetime.now()
        cmd_id = now.strftime("%Y-%m-%d_%H-%M-%S")

        with open(self.path, "r+") as jsonFile:
            data = json.load(jsonFile)

            data["recent"] = {}

        # Update dictionary
            data["past"][cmd_id] = cmd.to_dictionary()
            data["recent"][cmd_id] = cmd.to_dictionary()

            jsonFile.seek(0)  # rewind
            json.dump(data, jsonFile)
            jsonFile.truncate()

    def get_history(self):
        json_history = {}
        with open(self.path, "r") as jsonFile:
            data = json.load(jsonFile)

            json_history = data["past"]

        return json_history

    def get_recent_cmd(self):
        json_cmd = {}
        with open(self.path, "r") as jsonFile:
            data = json.load(jsonFile)

            json_cmd = data["recent"]

        # get command ID
        cmd_id = ""
        for k in json_cmd.keys():
            
            cmd_id = k
        return json_cmd[k]

    def select_cmd(self, index):
        pass
