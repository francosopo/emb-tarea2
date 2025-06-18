from struct import unpack

from gui.domain.entities.entity import Entity

class AxisEntity(Entity):

    def __init__(self):
        super().__init__("f", 4)
        self.data = {
            "x": [],
            "y": [],
            "z": [],
        }

    def __add_data(self, target, data):
        self.data[target].append(data)

    def add_x(self, x):
        self.__add_data("x", x)

    def add_y(self, y):
        self.__add_data("y", y)

    def add_z(self, z):
        self.__add_data("z", z)
        