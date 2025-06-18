import serial

from gui.domain.config_manager import ConfigManager

class SerialController():

    def __init__(self, entity, sensor):
        self.entity = entity
        self.sensor = sensor
        self.conf_manager = ConfigManager.make_obj()

        self.ser = serial.Serial(
            self.conf_manager.get_uart_port(), 
            self.conf_manager.get_baud_rate(), 
            timeout=self.conf_manager.get_serial_timeout()
        )
    
    def unpack(self, d):
        self.entity.unpack(d)

    def read(self):
        if self.ser.in_waiting > 0:
            d = self.ser.read(self.entity.get_window_length() * self.entity.get_size())
            return self.unpack(d)
    
