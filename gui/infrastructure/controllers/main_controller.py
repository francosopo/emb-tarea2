class MainController(object):

    def __init__(self, sensor, view):
        self.sensor = sensor
        self.view = view
        
    def show_sensor_modes(self):
        return self.sensor.show_modes()

    def show_sensor_classification_data(self):
        return self.sensor.show_classification_data()
    
    def selection_changed(self, index):
        selected_text = self.view.dropdown.currentText()
        self.view.selected_mode = selected_text

    def selection_data_changed(self, index):
        selected_text = self.view.dropdownDataToShow.currentText()
        self.view.selected_data = selected_text
        if selected_text == "Temperature":
            self.view.controller = self.view.temperature_controller
        elif selected_text == "Humidity":
            self.view.controller = self.view.humidity_controller
        elif selected_text == "Gas":
            self.view.controller = self.view.gas_controller
        elif selected_text == "Pressure":
            self.view.controller = self.view.pressure_controller
        print(self.view.controller)


    