from gui.domain.component import Component

class GasSensor(Component):

    def __init__(self, name):
        super().__init__(name)
        self.ALLOWED_MODES = [
            "forced",
            "parallel",
            "sleep"
        ]

        self.CLASSIFICATION_DATA = [
            "Temperature",
            "Gas",
            "Humidity",
            "Pressure"
        ]

    