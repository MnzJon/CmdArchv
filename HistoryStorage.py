import json


class HistoryStorage():
    def __init__(self, path):
        self.path = path

    def store_cmd(self,cmd):
        print(str(cmd))
        pass

    def get_recent_cmd(self):
        pass

    def select_cmd(self):
        pass
