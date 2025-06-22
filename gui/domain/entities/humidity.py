from gui.domain.entities.entity import Entity

class Humidity(Entity):

    def __init__(self):
        super().__init__("i", 4, "Humidity")
        