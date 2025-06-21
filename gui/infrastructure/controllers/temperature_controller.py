from gui.domain.entities.temperature import Temperature
from gui.infrastructure.controllers.serial_controller import SerialController

class TemperatureController(SerialController):

    def __init__(self, sensor, view):
        super().__init__(Temperature(), sensor, view)
    
    def show_sensor_modes(self):
        return self.sensor.show_modes()

    def selection_changed(self, index):
        selected_text = self.view.dropdown.currentText()
        self.view.selected_mode = selected_text
        self.view.labelSelectedMode.setText(selected_text)
    
    def add_data_to_view(self, data):
        self.view.add_temperature_data(data)
