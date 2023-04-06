class ScriptToken():
    def __init__(self,p_script):
        self.script = p_script

    def set_script(self, cmd):
        self.script = cmd

    def __str__(self):
        return self.script

class EpilogueToken():
    def __init__(self, p_script):
        self.script = p_script

    def set_cmd(self, cmd):
        self.script = cmd

    def __str__(self):
        return self.script

class BuildCommandToken():
    def __init__(self, p_script):
        self.script = p_script

    def set_cmd(self, cmd):
        self.script = cmd

    def __str__(self):
        return self.script

class FlagToken():
    def __init__(self, flag, value):
        self.flag = flag
        self.value = value

    def get_flag(self):
        return self.flag

    def get_value(self):
        return self.value

    def __str__(self):
        return self.flag + "=" + self.value

