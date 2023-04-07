import json
import os
from StateHolder import StateHolder

class FavouritesStorage():
    def setup(self):
        if os.path.exists(self.path) == False:
            f = open(self.path, "w")
            # Empty JSON 
            f.write('{}')
            f.close()

        return True

    def store_favourite(self,cmd, f_id):
        self.set_element(f_id, cmd.to_dictionary)

    def get_favourite(self, f_id):
        return self.get_element(f_id)
