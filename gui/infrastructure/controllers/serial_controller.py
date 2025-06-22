import serial, time, threading, abc
from struct import  pack, unpack


from gui.domain.config_manager import ConfigManager

class SerialController(abc.ABC):

    def __init__(self, entity, sensor, view):
        self.entity = entity
        self.sensor = sensor
        self.enabled = True
        self.conf_manager = ConfigManager.make_obj()
        self.cond = threading.Condition()
        self.entity.add_lock(self.cond)
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
        raw_data = self.ser.read(self.entity.get_window_length() * self.entity.get_size())
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
        time.sleep(1)
        # Empezamos con un BEGIN la comunicación
        print("empezando...")
        msg = pack("6s", "BEGIN\0".encode())
        self.cond.acquire()
        self.ser.write(msg)
        self.cond.release()
        time.sleep(1)
        self.cond.acquire()

        # Leemos la respuesta, debe ser un OK
        ok = self.ser.read(3)
        self.cond.release()
        ok2 = unpack("3s", ok)[0]
        ok2 = ok2.decode()
        print(ok2)
        # Mandamos la configuración del sensor
        self.cond.acquire()

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

        
        # Qué tipo de dato queremos leer
        # Entity debe tener un nombre:
        # Temperature, Pressure, Gas o Humidity
        # o Acceleration, Gyroscope, etc...
        payload_name = self.get_entity().get_name()
        payload_name_size = len(payload_name)
        payload_name_msg = pack("i", payload_name_size)
        self.ser.write(payload_name_msg)
        time.sleep(1)
        payload = pack(f"{len(self.entity.get_name()) + 1}s", (self.entity.get_name() + "\0").encode())
        self.ser.write(payload)
        print("enviando entidad de datos")
        print("recibiendo...")
        time.sleep(1)

        raw_data = self.ser.read(3)
        data = unpack("3s", raw_data)[0]
        ack = data.decode()
        print(ack)
        self.cond.release()
        data = self.read()
        for d in data:
            self.entity.add_data(d)
        self.add_data_to_view(data)
             

    @abc.abstractmethod
    def add_data_to_view(self, d):
        pass

    def stop_receiving(self):  
        self.stop = True   

    


