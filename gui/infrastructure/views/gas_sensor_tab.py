from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel, QComboBox
)
from gui.domain.gas_sensor import GasSensor
from gui.infrastructure.controllers.temperature_controller import TemperatureController


class GasSensorTab(QWidget):

    def __init__(self):
        super().__init__()
        self.sensor = GasSensor("BME688")
        self.temperature_controller = TemperatureController(self.sensor)
        layout = QVBoxLayout()
        label = QLabel(self.sensor.name)
        dropdown = QComboBox()
        dropdown.addItems(self.temperature_controller.show_sensor_modes())
        layout.addWidget(label)
        layout.addWidget(dropdown)
        self.setLayout(layout)

