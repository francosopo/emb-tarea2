from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
QLabel, QComboBox, QPushButton
)
import pyqtgraph as pg

from gui.domain.gas_sensor import GasSensor
from gui.infrastructure.controllers.temperature_controller import TemperatureController

class GasSensorTab(QWidget):

    def __init__(self):
        super().__init__()
        self.sensor = GasSensor("BME688")
        self.time = 0
        self.temperature_controller = TemperatureController(self.sensor, self)
        self.temp_data = []
        self.temp_data_time = []
        #self.gas_controller = GasController(self.sensor, self)
        #self.humidity_controller = HumidityController(self.sensor, self)
        #self.pressure_controller = PressureController(self.sensor, self)
        
        self.selected_mode = "forced"
        layout = QVBoxLayout()
        self.label = QLabel(self.sensor.name)
        self.labelSelectedMode = QLabel(self.selected_mode)
        self.dropdown = QComboBox()
        self.dropdown.addItems(self.temperature_controller.show_sensor_modes())
        self.dropdown.currentIndexChanged.connect(self.temperature_controller.selection_changed)
        self.buttonStart = QPushButton("Start")
        self.buttonStop = QPushButton("Stop")

        self.buttonStart.clicked.connect(self.temperature_controller.start_comm)
        self.buttonStop.clicked.connect(self.temperature_controller.stop_receiving)

        self.graph = pg.PlotWidget()

        layout.addWidget(self.label)
        layout.addWidget(self.dropdown)
        layout.addWidget(self.labelSelectedMode)
        layout.addWidget(self.buttonStart)
        layout.addWidget(self.buttonStop)
        layout.addWidget(self.graph)
        self.setLayout(layout)

    def add_temperature_data(self, d):
        self.temp_data.append(d)
        self.time += 1
        self.temp_data_time.append(self.time)
        self.graph.plot(self.temp_data_time, self.temp_data)


        