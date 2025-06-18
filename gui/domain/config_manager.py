import os
import configparser
import pathlib


class Config():

    def __init__(self):
        self.ROOT_PROJECT = pathlib.Path(__file__).parent.parent
        self.config_parser = configparser.ConfigParser()
        self.config = self.config_parser.read(os.path.join(self.ROOT_PROJECT, "conf.ini"))



    def get_window_length(self):
        return  int(self.config_parser["DEFAULT"]["WINDOW_LENGTH"])
    
    def get_uart_port(self):
        return self.config_parser["SERIAL"]["PORT"]
    def get_baud_rate(self):
        return int(self.config_parser["SERIAL"]["BAUD_RATE"])
    def get_serial_timeout(self):
        return int(self.config_parser["SERIAL"]["TIMEOUT"])
    
class ConfigManager():

    obj = None

    @classmethod
    def make_obj(cls):
        if not cls.obj:
            cls.obj = Config()
        return cls.obj
    

