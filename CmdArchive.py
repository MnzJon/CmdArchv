# Three main files to store info:
# History.json
#   { commands:[{ cmd: "", description: "", info: ""},...,{}] }
# TemplateFlags.json -> Stores flags pertaining to certain Options
# RequiredFlags.json -> Stores the flags that are required, but need to be entered everytime.
# TemplateCommands.json -> Stores commands that are useful for the user later on
import os
import subprocess

from Command import Command, CommandBuilder

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



class CmdArchive():
    def __init__(self, directory=HOME_DIRECTORY):
        self.home_directory = os.path.expanduser(directory)

        self.favourites_storage = FileStateStorage(self.home_directory + FAVOURITES_FILE)
        self.parameterized_flags = FileStateStorages(self.home_directory + PARAMETER_FILE)

    def setup_environment(self):
        if os.path.exists(self.home_directory) == False:
            os.mkdir(self.home_directory)

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

        ## OLD METHOD
        # parameters = self.parameterized_flags.get_parameters()
        # cmd = command_modifier(cmd, False, parameters)
        # self.hist_storage.store_cmd(cmd)

        subprocess.call(str(cmd),shell=True)

    def get_history(self, session_state):
        return session_state.get_history()

    # Favourite Section
    def get_favourites(self):
        favs_dict = self.favourites_storage.get_state()

        return favs_dict
