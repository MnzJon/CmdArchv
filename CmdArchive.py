# Three main files to store info:
# History.json
#   { commands:[{ cmd: "", description: "", info: ""},...,{}] }
# TemplateFlags.json -> Stores flags pertaining to certain Options
# RequiredFlags.json -> Stores the flags that are required, but need to be entered everytime.
# TemplateCommands.json -> Stores commands that are useful for the user later on
import os
import subprocess

HOME_DIRECTORY="~/.local/share/cmd_archive/"
HISTORY_FILE="history.json"


class CmdArchive():
    def __init__(self, directory=HOME_DIRECTORY):
        self.home_directory = os.path.expanduser(directory)

    def setup_environment(self):
        if os.path.exists(self.home_directory) == False:
            os.mkdir(self.home_directory)

        history_file_path = self.home_directory + HISTORY_FILE

        if os.path.exists(history_file_path) == False:
            f = open(history_file_path, "w")
            # Empty JSON 
            f.write("{}")
            f.close()

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
        subprocess.call(str(cmd),shell=True)

