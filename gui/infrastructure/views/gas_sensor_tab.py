from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
QLabel, QComboBox, QPushButton
)
from gui.domain.gas_sensor import GasSensor
from gui.infrastructure.controllers.temperature_controller import TemperatureController


class GasSensorTab(QWidget):

    def __init__(self):
        super().__init__()
        self.sensor = GasSensor("BME688")
        self.temperature_controller = TemperatureController(self.sensor, self)
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

        self.buttonStart.clicked.connect(self.temperature_controller.start_receiving)
        self.buttonStop.clicked.connect(self.temperature_controller.stop_receiving)

        layout.addWidget(self.label)
        layout.addWidget(self.dropdown)
        layout.addWidget(self.labelSelectedMode)
        layout.addWidget(self.buttonStart)
        layout.addWidget(self.buttonStop)
        self.setLayout(layout)

