# Three main files to store info:
# History.json
#   { commands:[{ cmd: "", description: "", info: ""},...,{}] }
# TemplateFlags.json -> Stores flags pertaining to certain Options
# RequiredFlags.json -> Stores the flags that are required, but need to be entered everytime.
# TemplateCommands.json -> Stores commands that are useful for the user later on
import os
import subprocess

from HistoryStorage import HistoryStorage
from Command import Command

HOME_DIRECTORY="~/.local/share/cmd_archive/"
HISTORY_FILE="history.json"

def to_command(dictionary):
    script = dictionary["script"]
    build = dictionary["build"]
    epilogue = dictionary["epilogue"]
    flags = []
    for flag in dictionary["flags"]:
        flag_tuple = []
        flag_tuple.append(flag["flag"])
        flag_tuple.append(flag["value"])

        flags.append(flag_tuple)

    cmd = Command(script, flags, build, epilogue)

    return cmd

class CmdArchive():
    def __init__(self, directory=HOME_DIRECTORY):
        self.home_directory = os.path.expanduser(directory)
        self.hist_storage = HistoryStorage(self.home_directory + HISTORY_FILE)

    def setup_environment(self):
        if os.path.exists(self.home_directory) == False:
            os.mkdir(self.home_directory)

        self.hist_storage.setup()


        return self

    def environment_test(self):
        if os.path.exists(self.home_directory):
            print("Home Directory -> PASS")
        else:
            print("Home Directory not setup -> FAIL")

        if os.path.exists(self.home_directory + HISTORY_FILE):
            print("History File -> PASS")
        else:
            print("History File not setup -> FAIL")

    def run_cmd(self,cmd):
        # Store command
        self.hist_storage.store_cmd(cmd)

        subprocess.call(str(cmd),shell=True)

    def get_history(self):
        cmd_history = self.hist_storage.get_history()
        history = []
        for cmd_id in cmd_history.keys():
            cmd = to_command(cmd_history[cmd_id])
            single_history = [cmd, cmd_id]

            history.append(single_history)
        # Parse the history into an array

        return history

    def select_history_cmd(self, debug=False):

        index = 0
        history = self.get_history()
        for (cmd, cmd_id) in history: 
            print(str(index) + " => " + str(cmd) + " : " + cmd_id)

            index += 1

        option = input("Choose Command: ")
        if type(int(option)) is int:
            option = int(option)
            if option > index:
                print("Invalid option")
            else:
                # Run command
                cmd = history[option][0]
                self.run_cmd(cmd)
        else:
            print("Did not enter an integer")

    def run_previous_cmd(self):
        prev_cmd_dictionary = self.hist_storage.get_recent_cmd()
        cmd = to_command(prev_cmd_dictionary)

        self.run_cmd(cmd) 
