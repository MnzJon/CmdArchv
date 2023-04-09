class ShellCommand():
    def __init__(self, scmd_id):
        self.scmd_id = scmd_id
        self.func=None
        self.commands = {}

    def is_base(self):
        return self.func != None

    def add_function(self, f):
        if not self.commands:
            self.func = f

            return True
        else:
            return False

    def run_cmd(self, arguments):
        if self.func != None:
            return self.func(arguments)
        else:
            return None

    def add_cmd(self, scmd):
        if self.func == None:
            self.commands[scmd.scmd_id] = scmd

            return True
        else:
            return False

    def get_cmd(self, scmd_id):
        if self.func != None:
            return None
        elif not self.commands:
            return None
        else:
            if scmd_id in self.commands:
                return self.commands[scmd_id]
            else:
                return None


