import serial, time
from struct import  pack, unpack

from gui.domain.config_manager import ConfigManager

class SerialController():

    def __init__(self, entity, sensor):
        self.entity = entity
        self.sensor = sensor
        self.conf_manager = ConfigManager.make_obj()
        self.feeding = True

        self.ser = serial.Serial(
            self.conf_manager.get_uart_port(), 
            self.conf_manager.get_baud_rate(), 
            timeout=self.conf_manager.get_serial_timeout()
        )
    
    def unpack(self, d):
        return self.entity.unpack(d)

    def read(self):
        print("total_read", self.entity.get_window_length() * self.entity.get_size())
        d = self.ser.read(self.entity.get_window_length() * self.entity.get_size())
        return self.unpack(d)
    
    def start_receiving(self):
        time.sleep(1)
        msg = pack("6s", "BEGIN\0".encode())
        self.ser.write(msg)
        time.sleep(1)
        ok = self.ser.read(3)
        ok2 = unpack("3s", ok)[0]
        ok2 = ok2.decode()
        print(ok2)
        #while(True):
        #if (ok2 == "OK"):
        print("recibiendo...")
        time.sleep(1)
        data = self.read()
        print(data)
        for d in data:
            self.entity.add_data(d)        
            
    def stop_receiving(self):
        self.feeding = False
        #self.ser.write("STOP".encode())

