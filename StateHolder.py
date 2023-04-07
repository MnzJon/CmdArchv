import json
import subprocess
from subprocess import PIPE, Popen
from utils import read_json, write_json
from io import StringIO # Python3 use: from io import StringIO
import sys


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

class TmuxStateHolder(StateHolder):
    def __init__(self):
        pass

    def session_id(self):
        #old_stdout = sys.stdout
        #sys.stdout = mystdout = StringIO()
        my_str = subprocess.run("tmux display-message -p '#S'",shell=True,capture_output=True)
        print(my_str.stdout)
        #print(mystdout.getvalue())
        #sys.stdout = old_stdout

    

