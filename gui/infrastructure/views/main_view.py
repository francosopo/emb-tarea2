from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout

from gui.infrastructure.views.gas_sensor_tab import GasSensorTab
from gui.infrastructure.views.intertial_sensor_tab import IntertialSensorTab
class MainView():

    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()

        tabs = QTabWidget()
        tabs.addTab(GasSensorTab(), "Gas Sensor")
        #tabs.addTab(IntertialSensorTab(), "Inertial Sensor")
        layout = QVBoxLayout()
        layout.addWidget(tabs)
        self.window.setLayout(layout)

    def show(self):
        self.window.show()
        self.app.exec()