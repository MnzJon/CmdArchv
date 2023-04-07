import json
import os
from datetime import datetime
from StateHolder import StateHolder

class HistoryStorage(StateHolder):

    def setup(self):
        if os.path.exists(self.filepath) == False:
            f = open(self.path, "w")
            # Empty JSON 
            f.write('{ "recent": {}, "past": {}}')
            f.close()

        return True

    def store_cmd(self,cmd):
        now = datetime.now()
        cmd_id = now.strftime("%Y-%m-%d_%H-%M-%S")

        history_state = self.get_state()

        history_state["recent"] = {}

        history_state["past"][cmd_id] = cmd.to_dictionary()
        history_state["recent"][cmd_id] = cmd.to_dictionary()

        self.write_data(history_state)

    def get_history(self):
        return self.get_element("history")

    def get_recent_cmd(self):
        recent_data = self.get_element("recent")
        # get command ID

        cmd_id = ""
        for k in recent_data.keys():
            
            cmd_id = k
            break

        return recent_data[cmd_id]
