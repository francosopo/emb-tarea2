from gui.domain.exceptions.mode_not_allowed import ModeNotAllowed
from gui.domain.exceptions.data_not_allowed import DataNotAllowed

class Component(object):

    def __init__(self, name):
        self.name = name
        self.ALLOWED_MODES = []
        self.mode = ""
        self.CLASSIFICATION_DATA= []
        self.data_selected = ""

    def set_mode(self, mode):
        if mode not in self.ALLOWED_MODES:
            raise ModeNotAllowed("")
        self.mode = mode

    def show_modes(self):
        return self.ALLOWED_MODES

    def get_mode(self):
        return self.mode
    
    def show_classification_data(self):
        return self.CLASSIFICATION_DATA
    
    def set_classification_data(self, s):
        if s not in self.CLASSIFICATION_DATA:
            raise DataNotAllowed()
        self.data_selected = s
    