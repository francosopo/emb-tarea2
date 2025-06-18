from gui.domain.entities.temperature import Temperature
from gui.infrastructure.controllers.serial_controller import SerialController

class TemperatureController(SerialController):

    def __init__(self, sensor):
        super().__init__(Temperature(), sensor)

    def add_data(self, d):
        self.entity.add_data(d)

    def retrieve_data(self):
        return self.entity.retrieve_data()
    
    def show_sensor_modes(self):
        return self.sensor.show_modes()
