import os
from StateHolder import StateHolder 

class ParameterizedFlags(StateHolder):
    def setup(self):
        if os.path.exists(self.path) == False:
            f = open(self.path, "w")
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

