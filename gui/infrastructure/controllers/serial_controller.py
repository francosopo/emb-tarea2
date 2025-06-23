import serial, time, threading, abc
from struct import  pack, unpack

from gui.domain.config_manager import ConfigManager

class SerialController(abc.ABC):

    def __init__(self, entity, sensor, view):
        self.entity = entity
        self.sensor = sensor
        self.enabled = True
        self.conf_manager = ConfigManager.make_obj()
        #self.cond = threading.Condition()
        #self.entity.add_lock(self.cond)
        self.view = view

        self.ser = serial.Serial(
            self.conf_manager.get_uart_port(), 
            self.conf_manager.get_baud_rate(), 
            timeout=self.conf_manager.get_serial_timeout()
        )
    
    def get_entity(self):
        return self.entity

    def unpack(self, d):
        return self.entity.unpack(d)

    def read(self):
        print("total_read", self.entity.get_window_length() * self.entity.get_size())
        #while self.ser.in_waiting > 0:
        self.cond.acquire()
        #time.sleep(1)
        raw_data = self.ser.read(self.entity.get_window_length() * self.entity.get_size())
        print("raw_data", len(raw_data), raw_data)
        data = self.unpack(raw_data)
        self.cond.release()
        return data
    
    def start_comm(self):
        self.start_receiving()
    
    def get_receiving_thread(self):
        return self.receiving_thread
    
    def get_retrieving_thread(self):
        return self.retrieving_thread

    def start_receiving(self):
        # first_data = self.ser.read(1)
        # f = unpack("B", first_data)[0]
        # print(f, "==1?")
        # time.sleep(1)

        # Empezamos con un BEGIN la comunicación
        print("empezando...")
        msg = pack("6s", "BEGIN\0".encode())
        #self.cond.acquire()
        self.ser.write(msg)
        #self.cond.release()
        time.sleep(1)
        #self.cond.acquire()

        # Leemos la respuesta, debe ser un OK
        ok = self.ser.read(3)
        #self.cond.release()
        ok2 = unpack("3s", ok)[0]
        ok2 = ok2.decode()
        print(ok2)
        # Mandamos la configuración del sensor
        #self.cond.acquire()

        sensor_conf = self.view.selected_mode # forced, parallel o sleep
        # Mandamos el tamaño del dato "sensor_conf"
        sensor_conf_length = len(sensor_conf)
        sensor_conf_length_msg = pack(f"i", sensor_conf_length)
        self.ser.write(sensor_conf_length_msg)
        print("sending configuration")
        time.sleep(1)
        msg = pack(f"{sensor_conf_length}s", sensor_conf.encode())
        self.ser.write(msg)
        time.sleep(1)

        # Leemos la respuesta, debe ser un OK
        ok3 = self.ser.read(3)
        #self.cond.release()
        ok3 = unpack("3s", ok3)[0]
        ok3 = ok3.decode()
        print(ok3)
        time.sleep(1)
        for i in range(self.conf_manager.get_window_length()):
            self.view.add_time()
            response = self.ser.read(16)
            print("len response:", len(response))
            data = unpack("fIII", response)
            self.view.add_temperature_data(data[0])
            self.view.add_pressure_data(data[1])
            self.view.add_humidity_data(data[2])
            self.view.add_gas_data(data[3])  
            time.sleep(1)

    # @abc.abstractmethod
    # def add_data_to_view(self, d):
    #     pass

    def stop_receiving(self):  
        self.stop = True   

    


