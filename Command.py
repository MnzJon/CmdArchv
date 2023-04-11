from CommandToken import ScriptToken, EpilogueToken, BuildCommandToken, FlagToken

class Command():
    def __init__(self, script="", token_flags=[], build_cmd="", epilogue=""):
        self.script=ScriptToken(script)
        self.token_flags = []
        # setup Flags
        for flags in token_flags:
            self.token_flags.append(FlagToken(flags[0],flags[1]))

        self.build_cmd=BuildCommandToken(build_cmd)
        self.epilogue = EpilogueToken(epilogue)

    def set_build_cmd(self, build_cmd):
        self.build_cmd.set_cmd(build_cmd)

    def set_script(self, script):
        self.script.set_script(script)

    def set_epilogue(self, epilogue):
        self.epilogue.set_cmd(epilogue)

    def get_script(self):
        return self.script.get_script()

    def get_build_cmd(self):
        return self.build_cmd.get_cmd()

    def get_epilogue(self):
        return self.epilogue.get_cmd()

    def append_token_flag(self, flag_value):
        new_flag_token = FlagToken(flag_value[0],flag_value[1])
        self.token_flags.append(new_flag_token)

    def set_token_flag(self, token_flags):
        self.token_flags = token_flags

    def get_flags(self):
        return self.token_flags

    def cmd(self):
        cmd_string = str(self.script) + " "
        for flag_value in self.token_flags:
            flag = flag_value[0]
            value = flag_value[1]
            cmd_string += str(flag) + "=" + str(value) + " "
        
        cmd_string += str(self.build_cmd) + " ; "
        cmd_string += str(self.epilogue)


        return cmd_string

    def __str__(self):
        return self.cmd()

    def to_dictionary(self):
        # Get array of flag dictionaries
        d_flags = []
        for flag in self.token_flags:
            d_flag = {
                        "flag": flag.get_flag(),
                        "value": flag.get_value()
                    }
            d_flags.append(d_flag)
        
        d = {
                "script": self.script.get_script(),
                "flags": d_flags,
                "build": self.build_cmd.get_cmd(),
                "epilogue": self.epilogue.get_cmd()
            }

        return d

    def has_token_flag(self, flag):
        pass



class CommandBuilder():
    def __init__(self):
        self.cmd = Command()

    def from_string(self, str_script):
        tokens = str_script.split(' ')
        index = 0

        # Find all tokens to build the script
        while("=" not in tokens[index] and index < len(tokens)):
            index += 1

        # Construct script string
        script = ""
        for i in range(0, index):
            script += tokens[i] + " "

        flag_start_index = index
        # Find flags
        while("=" in tokens[index] and index < len(tokens)):
            index += 1

        # Construct the flag tokens
        flag_tokens = []
        for i in range(flag_start_index, index):
            flag_value = tokens[i].split('=')
            flag_tokens.append(flag_value)

        # Find build script
        if index + 1 == len(tokens):
            print("ERROR: no more tokens. Expected a build command")
            return None

        build_start_index = index
        build_str = tokens[build_start_index]

        # Get Epilogues
        index += 1
        epilogue_str = ""
        for i in range(index, len(tokens)):
            epilogue_str += tokens[i] + " "


        print("BUILDING COMMAND")
        self.set_script(script)
        self.set_token_flag(flag_tokens)
        print(flag_tokens)
        self.set_build_cmd(build_str)
        self.set_epilogue(epilogue_str)

        return self.build()






    def set_script(self, script):
        self.cmd.set_script(script)

        return self

    def set_token_flag(self, token_flags):
        self.cmd.set_token_flag(token_flags)

    def append_token_flag(self, flag_value):
        self.cmd.append_token_flag(flag_value)

        return self

    def set_build_cmd(self, build_cmd):
        self.cmd.set_build_cmd(build_cmd)

        return self

    def set_epilogue(self, epilogue):
        self.cmd.set_epilogue(epilogue)

        return self

    def build(self):
        old_cmd = self.cmd

        self.cmd = Command()

        return old_cmd
