class ScriptToken():
    pass

class BuildCommandToken():
    pass

class TokenFlag():
    def __init__(self, flag, value):
        pass



class Command():
    def __init__(self, script, token_flags, build_cmd):
        self.script=script
        self.token_flags=token_flags
        self.build_cmd=build_cmd

    def set_build_cmd(self, build_cmd):
        self.build_cmd = build_cmd

    def set_script(self, script):
        self.script = script

    def append_token_flag(self, token_flag):
        self.token_flag.append(token_flag)


    def has_token_flag(self, token_flag):
        pass
