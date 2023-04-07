import json
import os
from StateHolder import FileStateHolder

class FavouritesStorage(FileStateHolder):
    def setup(self):
        if os.path.exists(self.filepath) == False:
            f = open(self.filepath, "w")
            # Empty JSON 
            f.write('{}')
            f.close()

        return True

    def store_favourite(self,cmd, f_id):
        self.set_element(f_id, cmd.to_dictionary)

    def get_favourite(self, f_id):
        return self.get_element(f_id)
