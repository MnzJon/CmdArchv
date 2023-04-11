import os
import subprocess
import sys
from APICmdArchive import APICmdArchive, HOME_DIRECTORY
from StateHolder import SessionStateHolder
from Command import CommandBuilder


class ShellCmdArchAST():
    def __init__(self):
        self.options = {}
        self.commands = []
        pass

    def has_option(self, op):
        return op in self.options

    def get_options(self):
        return self.options

    def add_option(self, op):
        self.options[op] = True

    def add_command(self, cmd):
        self.commands.append(cmd)

    def get_commands(self):
        return self.commands

# Convert input to an object that can be used.
#  [options] [command] [sub-commands]
def parse_shell_input(s):
    tokens = s.split(" ")
    # Get options
    return to_ast(tokens)

def to_ast(tokens):
    ast = ShellCmdArchAST()
    for tok in tokens:
        if tok[0] == '-':
            ast.add_option(tok[1])
        else:
            ast.add_command(tok)

    return ast

def get_session_state(global_state=False):
    # If TMUX: return a tmux session state
    # Else return a global session state
    if "TMUX" in os.environ and global_state == False:
        # Get current session name
        my_out = subprocess.run("tmux display-message -p '#S'",shell=True,capture_output=True)
        tmux_session = my_out.stdout.decode("utf-8").strip()

        if os.path.exists(os.path.expanduser("~/.local/share/cmd_archive/tmux/")):
            print("TMUX PATH EXISTS")
        else:
            os.mkdir(os.path.expanduser("~/.local/share/cmd_archive/tmux/"))

        directory = "~/.local/share/cmd_archive/tmux/" + tmux_session
        directory = os.path.expanduser(directory)
        if os.path.exists(directory):
            print("Session Path Exists")
        else:
            os.mkdir(directory)

        session_state = SessionStateHolder(tmux_session, directory)

        return session_state

    else:
        directory = "~/.local/share/cmd_archive/"
        directory = os.path.expanduser(directory)

        session_state =SessionStateHolder("global",directory)
        return session_state

class ShellCmdArch():
    def __init__(self, ast, directory=HOME_DIRECTORY):
        self.cmdArch = APICmdArchive(directory)
        self.ast = ast

    def run_shell(self):
        commands = ast.get_commands()
        if self.ast.has_option("g"):
            session_state = get_session_state(True)
        else:
            session_state = get_session_state()

        if commands == []:
            print("No commands entered")
        elif commands == ["history","show"]:
            self.cmdArch.show_history(session_state)
        elif commands == ["history","select"]:
            self.cmdArch.run_cmd_from_history()
        elif commands == ["fav", "show"]:
            self.cmdArch.show_favourites()
        elif commands == ["fav","select"]:
            pass
        elif commands == ["fav","add"]:
            self.cmdArch.add_favourite_prompt()
        elif commands == ["params","show"]:
            pass
        elif commands == ["params","add"]:
            pass
        elif commands == ["history","clear"]:
            self.cmdArch.clear_history()
        else:
            if commands[0] == "new":
                # construct string to run
                commands.pop(0)
                cmd_str = ""
                for c in commands:
                    cmd_str += c + " "

                cmdBuilder = CommandBuilder()
                cmd = cmdBuilder.from_string(cmd_str)
                print(str(cmd))
                self.cmdArch.run_new_cmd(cmd, session_state)
            else:
                print("Invalid commands")




if __name__ == '__main__':
    sys.argv.pop(0)
    ast = to_ast(sys.argv)
    shell = ShellCmdArch(ast, os.path.abspath("./"))
    shell.run_shell()

