import json
from utils import read_json, write_json

class StateHolder():
    def __init__(self, filepath):
        self.filepath = filepath

    def get_state(self):
        json_data = read_json(self.filepath)

        return json_data

    def get_element(self, element):
        json_data = read_json(self.filepath)

        return json_data[element]

    def set_element(self, element, value):
        json_data = self.get_state
        json_data[element] = value
        self.write_data(json_data)

    def remove_element(self, element):
        json_data = self.get_state()

        json_data.pop(element)

        self.write_data(json_data)

        

    def write_data(self, data):
        write_json(self.filepath, data)

