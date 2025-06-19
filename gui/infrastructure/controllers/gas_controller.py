from serial_controller import SerialController
from gui.domain.entities.gas import Gas
class GasController(SerialController):

    def __init__(self, sensor, view):
        super().__init__(Gas(), sensor)
        self.view = view

    