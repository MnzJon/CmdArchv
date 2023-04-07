# Three main files to store info:
# History.json
#   { commands:[{ cmd: "", description: "", info: ""},...,{}] }
# TemplateFlags.json -> Stores flags pertaining to certain Options
# RequiredFlags.json -> Stores the flags that are required, but need to be entered everytime.
# TemplateCommands.json -> Stores commands that are useful for the user later on
import os
import subprocess

from HistoryStorage import HistoryStorage
from FavouritesStorage import FavouritesStorage
from Command import Command, CommandBuilder
from ParameterizedFlags import ParameterizedFlags

HOME_DIRECTORY="~/.local/share/cmd_archive/"
HISTORY_FILE="history.json"
FAVOURITES_FILE="favourites.json"
PARAMETER_FILE="parameter_flags.json"

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

def command_modifier(cmd, parameterized=False, parameters={}):
    if parameterized == False:
        return cmd
    else:
        # Build new command with parameterized values
        cmdBuilder = CommandBuilder()
        script_str = cmd.get_script()
        build_cmd_str = cmd.get_build_cmd()
        epilogue_str =cmd.get_epilogue()

        cmdBuilder = cmdBuilder.set_script(script_str).set_build_cmd(build_cmd_str).set_epilogue(epilogue_str)

        # Iterate through flags and prompt for new value if in parameter
        flags = cmd.get_flags()
        for flag_token in flags:
            flag = flag_token.get_flag()
            value = flag_token.get_value()

            if flag in parameters:
                value = input("Enter value for "+flag+" => ")

            new_flag_token = [flag, value]

            cmdBuilder = cmdBuilder.append_token_flag(new_flag_token)


        return cmdBuilder.build()

class APICmdArchive():
    def __init__(self):
        self.cmdArchv = CmdArchive()
        self.cmdArchv.setup_environment()

    def sanity_check(self):
        self.cmdArchv.environment_test()

    def show_history(self):
        self.history_log() 

    def show_favourites(self):
        print(self.cmdArchv.get_favourites())

    def show_flags(self):
        pass

    def show_parameters(self):
        parameters = self.cmdArchv.parameterized_flags.get_parameters()
        print(parameters)

    def run_previous_cmd(self):
        prev_cmd_dictionary = self.cmdArchv.hist_storage.get_recent_cmd()
        cmd = to_command(prev_cmd_dictionary)

        self.cmdArchv.run_cmd(cmd) 

    def run_favourite(self, cmd_id):
        favs = self.cmdArchv.get_favourites()

        if cmd_id in favs:
            cmd = to_command(favs[cmd_id])
            self.cmdArchv.run_cmd(cmd)

    def history_log(self):
        index = 0
        history = self.cmdArchv.get_history()
        for (cmd, cmd_id) in history: 
            print(str(index) + " => " + str(cmd) + " : " + cmd_id)

            index += 1

        return index

    def add_favourite_prompt(self):
        history = self.cmdArchv.get_history()
        history_max = self.history_log()

        option = input("Choose Command as Favourite : ")
        option = int(option)

        if option > history_max:
            print("Invalid input")
        else:
            # store 
            cmd_id = input("Enter ID for Favourite : ")
            cmd = history[option][0]

            self.cmdArchv.favourites_storage.store_favourite(cmd, cmd_id)

    def select_cmd_from_history(self):
        index = self.history_log()
        history = self.cmdArchv.get_history()

        option = input("Choose Command: ")
        if type(int(option)) is int:
            option = int(option)
            if option > index:
                print("Invalid option")
            else:
                # Run command
                cmd = history[option][0]
                self.cmdArchv.run_cmd(cmd)
        else:
            print("Did not enter an integer")

    def run_new_cmd(self):
        pass

class CmdArchive():
    def __init__(self, directory=HOME_DIRECTORY):
        self.home_directory = os.path.expanduser(directory)
        self.hist_storage = HistoryStorage(self.home_directory + HISTORY_FILE)
        self.favourites_storage = FavouritesStorage(self.home_directory + FAVOURITES_FILE)
        self.parameterized_flags = ParameterizedFlags(self.home_directory + PARAMETER_FILE)

    def setup_environment(self):
        if os.path.exists(self.home_directory) == False:
            os.mkdir(self.home_directory)

        self.hist_storage.setup()
        self.favourites_storage.setup()
        self.parameterized_flags.setup()

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

        if os.path.exists(self.home_directory + FAVOURITES_FILE):
            print("Favourites File -> PASS")
        else: 
            print("Favourites File not setup -> FAIL")

    def add_parameter_flag(self, param):
        self.parameterized_flags.add_parameter(param)

    def remove_parameter(self, param):
        self.parameterized_flags.remove_parameter(param)

    def run_cmd(self,cmd):
        # Store command
        parameters = self.parameterized_flags.get_parameters()
        cmd = command_modifier(cmd, False, parameters)
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


    def get_favourites(self):
        favs_dict = self.favourites_storage.get_state()

        return favs_dict
