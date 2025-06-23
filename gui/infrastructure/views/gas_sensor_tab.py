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

        self.pen = pg.mkPen(color=(255, 255, 255), width=5, style=QtCore.Qt.DashLine)
        self.temp_line = None
        self.gas_line = None


        layout.addWidget(self.label)
        layout.addWidget(self.dropdown)
        layout.addWidget(self.dropdownDataToShow)
        layout.addWidget(self.buttonStart)
        layout.addWidget(self.buttonStop)
        layout.addWidget(self.temp_graph)
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
        print(self.time_data)
        print(self.temperature.get_data())
        if self.temp_line is None:
            print("printing data...")
            self.temp_line = self.temp_graph.plot(self.time_data, self.temperature.get_data(), pen=self.pen)
        else:
            self.temp_line.setData(self.time_data, self.temperature.get_data(), pen=self.pen)


    def add_humidity_data(self, d):
        #self.graph.clear()
        self.humdity_data.append(d)
        self.graph.setTitle("Humidity vs Time")
        styles = {
            "color": "yellow",
            "font-size": "18px"
        }
        self.graph.setLabel("left", "Humidity (%)", **styles)
        self.graph.setLabel("bottom", "Time", **styles)
        if self.line is None:
            self.line = self.graph.plot(self.humidity_data_time, self.humidity_data, pen=self.pen)
        else:
            self.line.setData(self.humidity_data_time, self.humidity_data, pen=self.pen)

    def add_gas_data(self, d):
        self.gas.add_data(d)
        self.gas_graph.setTitle("Gas vs time")
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
