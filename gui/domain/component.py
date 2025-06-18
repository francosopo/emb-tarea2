from gui.domain.exceptions.mode_not_allowed import ModeNotAllowed

class Component(object):

    def __init__(self, name):
        self.name = name
        self.ALLOWED_MODES = []
        self.mode = ""


    def set_mode(self, mode):
        if mode not in self.ALLOWED_MODES:
            raise ModeNotAllowed("")
        self.mode = mode

    def show_modes(self):
        return self.ALLOWED_MODES

    def get_mode(self):
        return self.mode