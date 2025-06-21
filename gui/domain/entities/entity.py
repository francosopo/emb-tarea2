#import abc
from struct import unpack
from gui.domain.config_manager import  ConfigManager

class Entity():

    def __init__(self, format_identifier, size):
        self.lock = None
        self.config_manager = ConfigManager.make_obj()
        self.window_length = self.config_manager.get_window_length()
        self.data = [0] * self.window_length
        self.index = 0
        self.format_identifier = format_identifier
        self.size = size
    
    def get_size(self):
        return self.size
    
    def add_lock(self, lock):
        self.lock = lock

    def add_data(self, d):
        self.data[self.index % self.window_length] = d
    def get_data(self, index):
        if index > self.index:
            return self.data[self.index]
        return self.data[index]
    
    def notify_view(self, data, view):
        view.add_data(data)

    def get_window_length(self):
        return self.window_length

    def unpack(self, d):
        print(self.window_length, self.format_identifier, len(d))
        return unpack(f"{self.window_length}{self.format_identifier}", d)
    
    