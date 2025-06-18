#import abc
from struct import unpack

from gui.domain.config_manager import  ConfigManager

class Entity():

    def __init__(self, format_identifier, size):
        self.data = []
        self.config_manager = ConfigManager.make_obj()
        self.window_length = self.config_manager.get_window_length()
        self.format_identifier = format_identifier
        self.size = size
    
    def get_size(self):
        return self.size

    def add_data(self, d):
        self.data.append(d)

    def retrieve_data(self):
        return self.data
    
    def unpack(self, d):
        return unpack(f"{self.window_length}{self.format_identifier}", d)[0]
    
    