#import abc
from struct import unpack
from gui.domain.config_manager import  ConfigManager

class Entity():

    def __init__(self, format_identifier, size, name):
        self.lock = None
        self.config_manager = ConfigManager.make_obj()
        self.window_length = self.config_manager.get_window_length()
        self.data = [0] * self.window_length
        self.top_index = 0
        self.bottom_index = 0
        self.index = 0
        self.format_identifier = format_identifier
        self.size = size
        self.buffer_size = 0 
        self.name = name
    
    def get_size(self):
        return self.size
    
    def add_lock(self, lock):
        self.lock = lock

    def add_data(self, d):
        self.lock.acquire()
        while (self.buffer_size == self.window_length):
            self.lock.wait()
        self.data[self.top_index % self.window_length] = d
        self.top_index = (self.top_index + 1) % self.window_length
        self.buffer_size += 1
        self.lock.notify()
        self.lock.release()

    def get_data(self):
        self.lock.acquire()
        while(self.buffer_size == 0):
            self.lock.wait()
        d = self.data[self.bottom_index]
        self.bottom_index = (self.bottom_index + 1) % self.window_length
        self.lock.notify()
        self.lock.release()
        return d

    def get_window_length(self):
        return self.window_length

    def unpack(self, d):
        print(self.window_length, self.format_identifier, len(d))
        return unpack(f"{self.window_length}{self.format_identifier}", d)

    def get_name(self):
        return self.name
    
    