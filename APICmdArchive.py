from CmdArchive import CmdArchive, to_command, command_modifier
from StateHolder import SessionStateHolder

HOME_DIRECTORY="~/.local/share/cmd_archive/"

class APICmdArchive():
    def __init__(self, directory=HOME_DIRECTORY):
        self.cmdArchv = CmdArchive(directory)
        self.cmdArchv.setup_environment()
        print(directory)
        self.global_session_state = SessionStateHolder("global", directory)

    def get_global_session(self):
        return self.global_session_state

    def show_history(self, session_state):
        history_data = session_state.get_history()
        self.history_log(history_data) 

    def show_favourites(self):
        print(self.cmdArchv.get_favourites())

    def show_flags(self):
        print(self.cmdArchv.get_parameter_flag())

    def show_parameters(self):
        parameters = self.cmdArchv.parameterized_flags.get_parameters()
        print(parameters)

    def run_previous_cmd(self, session_state):
        prev_cmd_dictionary = session_state.get_recent_cmd()
        cmd = to_command(prev_cmd_dictionary)

        self.store_cmd(cmd, session_state)
        self.cmdArchv.run_cmd(cmd) 

    def run_favourite(self, cmd_id, session_state):
        favs = self.cmdArchv.get_favourites()

        if cmd_id in favs:
            cmd = to_command(favs[cmd_id])
            self.store_cmd(cmd, session_state)
            self.cmdArchv.run_cmd(cmd)

    def store_cmd(self, cmd, session_state):
        session_state.record_cmd(cmd)
        if session_state.state_id != "global":
            self.global_session_state.record_cmd(cmd)

    def history_log(self, history_data):
        index = 0
        # Sort dictionary
        history = dict(sorted(history_data.items()))
        for cmd_id in history.keys(): 
            cmd = history[cmd_id]
            print(str(index) + " => " + str(to_command(cmd)) + " : " + cmd_id)

            index += 1

        return index

    def add_favourite_prompt(self, session_state):
        history = session_state.get_history()
        history_max = self.history_log()

        option = input("Choose Command as Favourite : ")
        option = int(option)

        if option > history_max:
            print("Invalid input")
        else:
            # store 
            cmd_id = input("Enter ID for Favourite : ")
            cmd = history[option][0]

            self.cmdArchv.favourites_storage.set_element(cmd_id, cmd)

    def run_cmd_from_history(self, session_state):
        index = self.history_log(session_state.get_history())
        history = session_state.get_history()

        option = input("Choose Command: ")
        if type(int(option)) is int:
            option = int(option)
            if option > index:
                print("Invalid option")
            else:
                # Run command
                cmd = history[option][0]

                session_state.record_cmd(cmd)
                # Add to global session state
                if session_state.state_id != "global":
                    self.global_session_state.record_cmd(cmd)

                self.cmdArchv.run_cmd(cmd)

                # Store command to specific session
        else:
            print("Did not enter an integer")

    def clear_history(self, session_state):
        session_state.clear()

    def run_new_cmd(self, cmd, session_state):
        self.store_cmd(cmd, session_state)
        self.cmdArchv.run_cmd(cmd)
        print("running new command")
