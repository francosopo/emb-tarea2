from gui.domain.component import Component

class InertialSensor(Component):
    def __init__(self, name):
        super().__init__(name)
        self.ALLOWED_MODES = [
            "low",
            "mid",
            "high",
            "sleep"
        ]

        