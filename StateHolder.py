import json
import subprocess
from datetime import datetime
from io import StringIO # Python3 use: from io import StringIO
import sys

class SessionStateHolder():
    def __init__(self, state_id, directory):
        self.state_id = state_id
        self.directory = directory
        self.history = FileStateHolder(self.directory + "history.json")
        self.recent = FileStateHolder(self.directory + "recent.json")

        self.history.setup_path()
        self.recent.setup_path()

    def setup_environment(self):
        if os.path.exists(self.directory) == false:
            os.mkdir(self.directory)


    def sanity_check(self):
        if os.path.exists(self.directory):
            print("Directory exists")


    def get_history(self):
        return self.history.get_state()

    def get_recent_cmd(self):
        return self.recent.get_state()
        recent_cmd_data = self.recent.get_element("recent") 
        # get command ID

        cmd_id = ""
        for k in recent_cmd_data.keys():
            
            cmd_id = k
            break

        return recent_cmd_data[cmd_id]

    def record_cmd(self, cmd):
        self.insert_to_history(cmd)
        self.insert_to_recent(cmd)

    def insert_to_history(self, cmd):
        now = datetime.now()
        cmd_id = now.strftime("%Y-%m-%d_%H-%M-%S")

        self.history.set_element(cmd_id, cmd)

    def insert_to_recent(self, cmd):
        self.recent.set_element("recent",cmd)


class StateHolder():

    def get_state(self):
        json_data = read_json(self.filepath)

        return json_data

    def get_element(self, element):
        json_data = read_json(self.filepath)

        return json_data[element]

    def set_element(self, element, value):
        json_data = self.get_state
        json_data[element] = value
        self.write_data(json_data)

    def remove_element(self, element):
        json_data = self.get_state()

        json_data.pop(element)

        self.write_data(json_data)


    def write_data(self, data):
        write_json(self.filepath, data)

class FileStateHolder(StateHolder):
    def __init__(self, filepath):
        self.filepath = filepath

    def setup_path(self):
        if os.path.exists(self.filepath) == false:
            f = open(self.filepath, "w")
            f.write('{}')
            f.close()

    def get_path(self):
        return filepath


























########### LEGACY ##############

class TmuxStateHolder(FileStateHolder):


    def get_path(self):
        my_str = subprocess.run("tmux display-message -p '#S'",shell=True,capture_output=True)
        print(my_str.stdout)
        #.decode("utf-8")

        return self.filepath + (my_str.stdout.decode("utf-8").strip()) +".json"


    def buffer_paste(self):
        subprocess.run("tmux set-buffer -b cmdArch {asdaw}", shell=True)
        my_str = subprocess.run("tmux paste-buffer -b cmdArch", shell=True, capture_output=True)
        #print(my_str)


    def session_id(self):
        #old_stdout = sys.stdout
        #sys.stdout = mystdout = StringIO()
        my_str = subprocess.run("tmux display-message -p '#S'",shell=True,capture_output=True)

        print(my_str.stdout)
        #print(mystdout.getvalue())
        #sys.stdout = old_stdout

    
    def setup(self):
        if os.path.exists(self.get_path()) == False:
            f = open(self.get_path(), "w")
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
        return self.get_element("past")

    def get_recent_cmd(self):
        recent_data = self.get_element("recent")
        # get command ID

        cmd_id = ""
        for k in recent_data.keys():
            
            cmd_id = k
            break

        return recent_data[cmd_id]

