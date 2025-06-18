from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel, QComboBox
)

from gui.infrastructure.controllers.acc_controller import AccelerationController 
from gui.domain.inertial_sensor import InertialSensor

class IntertialSensorTab(QWidget):

    def __init__(self):
        super().__init__()
        self.sensor = InertialSensor("BME270")
        self.controller = AccelerationController(self.sensor)
        layout = QVBoxLayout()
        label = QLabel(self.sensor.name)
        dropdown = QComboBox()
        dropdown.addItems(self.controller.show_sensor_modes())
        layout.addWidget(label)
        layout.addWidget(dropdown)
        self.setLayout(layout)

