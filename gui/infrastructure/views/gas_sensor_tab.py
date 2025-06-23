from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
QLabel, QComboBox, QPushButton
)

from PyQt5 import QtCore
import pyqtgraph as pg

from gui.domain.gas_sensor import GasSensor
from gui.domain.entities.temperature import Temperature
from gui.domain.entities.pressure import Pressure
from gui.domain.entities.humidity import Humidity
from gui.domain.entities.gas import Gas

from gui.infrastructure.controllers.main_controller import MainController

class GasSensorTab(QWidget):

    def __init__(self):
        super().__init__()
        self.sensor = GasSensor("BME688")
        self.main_controller = MainController(self.sensor, self)
        self.time_data = []
        self.time = 0
        self.temperature = Temperature()
        self.pressure= Pressure()
        self.humidity = Humidity()
        self.gas = Gas()
        
        self.controller = self.main_controller
        
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

        self.temp_graph = pg.PlotWidget()
        self.gas_graph = pg.PlotWidget()
        self.pressure_graph = pg.PlotWidget()
        self.humidity_graph = pg.PlotWidget()


        self.pen = pg.mkPen(color=(255, 255, 255), width=5, style=QtCore.Qt.DashLine)
        self.temp_line = None
        self.gas_line = None
        self.pressure_line = None
        self.humidity_line = None


        layout.addWidget(self.label)
        layout.addWidget(self.dropdown)
        layout.addWidget(self.dropdownDataToShow)
        layout.addWidget(self.buttonStart)
        layout.addWidget(self.buttonStop)
        layout.addWidget(self.temp_graph)
        layout.addWidget(self.pressure_graph)
        layout.addWidget(self.humidity_graph)
        layout.addWidget(self.gas_graph)
        self.setLayout(layout)
    
    def add_time(self):
        self.time += 1
        self.time_data.append(self.time)

    def add_temperature_data(self, d):
        self.temperature.add_data(d)
        self.temp_graph.setTitle("Temperature vs Time")
        styles = {
            "color": "yellow",
            "font-size": "18px"
        }
        self.temp_graph.setLabel("left", "Temperature (ºC)", **styles)
        self.temp_graph.setLabel("bottom", "Time", **styles)
        if self.temp_line is None:
            print("printing data...")
            self.temp_line = self.temp_graph.plot(self.time_data, self.temperature.get_data(), pen=self.pen)
        else:
            self.temp_line.setData(self.time_data, self.temperature.get_data(), pen=self.pen)

    def add_gas_data(self, d):
        self.gas.add_data(d)
        self.gas_graph.setTitle("Gas vs Time")
        styles= {
            "color": "yellow",
            "font-size": "18px"
        }
        self.gas_graph.setLabel("left", "Gas (Ohm)", **styles)
        self.gas_graph.setLabel("bottom", "Time", **styles)
        if self.gas_line is None:
            self.gas_line = self.gas_graph.plot(self.time_data, self.gas.get_data(), pen=self.pen)
        else:
            self.gas_line.setData(self.time_data, self.gas.get_data(), pen=self.pen)

    def add_pressure_data(self, d):
        self.pressure.add_data(d)
        self.pressure_graph.setTitle("Pressure vs Time")
        styles= {
            "color": "yellow",
            "font-size": "18px"
        }
        self.pressure_graph.setLabel("left", "Pressure (Pa)", **styles)
        self.pressure_graph.setLabel("bottom", "Time", **styles)

        if self.pressure_line is None:
            self.pressure_line = self.pressure_graph.plot(self.time_data, self.pressure.get_data(), pen=self.pen)
        else:
            self.pressure_line.setData(self.time_data, self.pressure.get_data(), pen=self.pen)

    def add_humidity_data(self, d):
        self.humidity.add_data(d)
        self.humidity_graph.setTitle("Humidity vs Time")
        styles= {
            "color": "yellow",
            "font-size": "18px"
        }
        self.humidity_graph.setLabel("left", "Humidity (percentage)", **styles)
        self.humidity_graph.setLabel("bottom", "Time", **styles)

        if self.humidity_line is None:
            self.humidity_line = self.humidity_graph.plot(self.time_data, self.humidity.get_data(), pen=self.pen)
        else:
            self.humidity_line.setData(self.time_data, self.humidity.get_data(), pen=self.pen)


    

