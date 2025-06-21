from gui.domain.entities.humidity import Humidity
from gui.infrastructure.controllers.serial_controller import SerialController

class HumidityController(SerialController):

    def __init__(self, sensor, view):
        super().__init__(Humidity(), sensor, view)
    
    def show_sensor_modes(self):
        return self.sensor.show_modes()
    
    def add_data_to_view(self, data):
        self.view.add_humidity_data(data)
        