import os
from StateHolder import FileStateHolder 

class ParameterizedFlags(FileStateHolder):
    def get_path(self):
        return self.filepath

    def setup(self):
        if os.path.exists(self.get_path()) == False:
            f = open(self.get_path(), "w")
            # Empty JSON 
            f.write('{}')
            f.close()

        return True

    def add_parameter(self, param):
        self.set_element(param, True)

    def remove_parameter(self,param):
        self.remove_element(param)

    def get_parameters(self):
        return self.get_state()

