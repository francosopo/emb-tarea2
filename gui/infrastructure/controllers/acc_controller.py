from gui.domain.entities.acceletation import Acceleration
from gui.infrastructure.controllers.serial_controller import SerialController

class AccelerationController(SerialController):

    def __init__(self, sensor):
        super().__init__(Acceleration(), sensor)

    def add_x(self, x):
        self.entity.add_x(x)

    def add_y(self, x):
        self.entity.add_y(x)
    
    def add_z(self, x):
        self.entity.add_z(x)

    def show_sensor_modes(self):
        return self.sensor.show_modes()
    
    

    