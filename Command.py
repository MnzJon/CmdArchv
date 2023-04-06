from CommandToken import ScriptToken, EpilogueToken, BuildCommandToken, FlagToken

class Command():
    def __init__(self, script="", token_flags=[], build_cmd="", epilogue=""):
        self.script=ScriptToken(script)
        self.token_flags = []
        # setup Flags
        for flags in token_flags:
            self.token_flags.append(FlagToken(flags[0],flags[1]))

        self.build_cmd=BuildCommandToken(build_cmd)
        self.epilogue_token = EpilogueToken(epilogue)

    def set_build_cmd(self, build_cmd):
        self.build_cmd.set_cmd(build_cmd)

    def set_script(self, script):
        self.script.set_script(script)

    def set_epilogue(self, epilogue):
        self.epilogue.set_cmd(epilogue)

    def append_token_flag(self, flag_value):
        new_flag_token = FlagToken(flag_value[0],flag_value[1])
        self.token_flags.append(new_flag_token)

    def cmd(self):
        cmd_string = str(self.script) + " "
        for flag in self.token_flags:
            cmd_string += str(flag) + " "
        
        cmd_string += str(self.build_cmd) + " ; "
        cmd_string += str(self.epilogue_token)


        return cmd_string

    def __str__(self):
        return self.cmd()



    def has_token_flag(self, flag):
        pass
