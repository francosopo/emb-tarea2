from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
QLabel, QComboBox, QPushButton
)
import pyqtgraph as pg

from gui.domain.gas_sensor import GasSensor
from gui.infrastructure.controllers.main_controller import MainController
from gui.infrastructure.controllers.temperature_controller import TemperatureController
from gui.infrastructure.controllers.humidity_controller import HumidityController

class GasSensorTab(QWidget):

    def __init__(self):
        super().__init__()
        self.sensor = GasSensor("BME688")
        self.main_controller = MainController(self.sensor, self)
        self.time = 0
        self.temperature_controller = TemperatureController(self.sensor, self)
        self.temp_data = []
        self.temp_data_time = []
        
        self.humidity_controller = HumidityController(self.sensor, self)
        self.humidity_data = []
        self.humidity_data_time = []
        
        #self.gas_controller = GasController(self.sensor, self)
        
        #self.pressure_controller = PressureController(self.sensor, self)
        self.controller = self.temperature_controller
        
        self.selected_mode = "forced"
        self.selected_data = "Temperature"
        layout = QVBoxLayout()
        self.label = QLabel(self.sensor.name)
        self.labelSelectedMode = QLabel(self.selected_mode)
        self.labelSelectedData = QLabel(self.selected_data)

        self.dropdown = QComboBox()
        self.dropdown.addItems(self.main_controller.show_sensor_modes())
        self.dropdown.currentIndexChanged.connect(self.main_controller.selection_changed)

        self.dropdownDataToShow = QComboBox()
        self.dropdownDataToShow.addItems(self.main_controller.show_sensor_classification_data())
        self.dropdownDataToShow.currentIndexChanged.connect(self.main_controller.selection_data_changed)
        self.buttonStart = QPushButton("Start")
        self.buttonStop = QPushButton("Stop")

        self.buttonStart.clicked.connect(self.controller.start_comm)
        self.buttonStop.clicked.connect(self.controller.stop_receiving)

        self.graph = pg.PlotWidget()

        layout.addWidget(self.label)
        layout.addWidget(self.dropdown)
        layout.addWidget(self.dropdownDataToShow)
        layout.addWidget(self.buttonStart)
        layout.addWidget(self.buttonStop)
        layout.addWidget(self.graph)
        self.setLayout(layout)

    def add_temperature_data(self, d):
        self.graph.clear()
        self.temp_data.append(d)
        self.time += 1
        self.temp_data_time.append(self.time)
        self.graph.plot(self.temp_data_time, self.temp_data)


    def add_humidity_data(self, d):
        self.graph.clear()
        self.humdity_data.append(d)
        self.time += 1
        self.humidity_data_time.append(self.time)
        self.graph.plot(self.humidity_data_time, self.humidity_data)