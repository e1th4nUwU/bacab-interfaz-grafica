# Adding debug prints in conexion_arduino.py to ensure data flow is correct

import serial
import serial.tools.list_ports
import threading

class ArduinoConnection:
    def __init__(self, update_status_callback, update_sensor_data_callback):
        self.arduino = None
        self.update_status = update_status_callback
        self.update_sensor_data = update_sensor_data_callback

    def get_ports(self):
        return [port.device for port in serial.tools.list_ports.comports()]

    def connect_arduino(self, port):
        try:
            self.arduino = serial.Serial(port, 9600, timeout=0.1)
            self.update_status("Conexión establecida")
            print("Arduino connected at:", port)
            self.start_reading()  # Start reading immediately after connecting
        except serial.SerialException as e:
            self.update_status(f"Conexión no establecida: {str(e)}")
            print("Failed to connect:", e)

    def disconnect_arduino(self):
        if self.arduino and self.arduino.is_open:
            self.arduino.close()
            self.update_status("Desconectado")
            print("Arduino disconnected.")
        self.arduino = None

    def connect(self, port):
        thread = threading.Thread(target=self.connect_arduino, args=(port,))
        thread.daemon = True
        thread.start()

    def disconnect(self):
        thread = threading.Thread(target=self.disconnect_arduino)
        thread.daemon = True
        thread.start()

    def start_reading(self):
        if not self.arduino or not self.arduino.is_open:
            self.update_status("No hay conexión con el Arduino.")
            return
        self.reading_thread = threading.Thread(target=self.read_data)
        self.reading_thread.daemon = True
        self.reading_thread.start()

    def read_data(self):
        while self.arduino and self.arduino.is_open:
            try:
                line = self.arduino.readline().decode('utf-8').strip()
                if line:  # Ensure we don't process empty lines
                    print("Data received:", line)
                    new_data = self.parse_data(line)
                    if new_data:
                        print("Parsed data:", new_data)
                        # Update the sensor data via the callback
                        self.update_sensor_data(new_data)
            except serial.SerialException:
                self.update_status("Error de lectura del puerto serial.")
                break
            except Exception as e:
                print("Error during data reading:", e)
                break

    def parse_data(self, line):
        try:
            data_str = line.strip('[]')
            data_list = [float(val) for val in data_str.split(',')]
            return data_list
        except Exception as e:
            print("Error parsing data:", e)
            return None

# Example usage (commented to avoid execution):
# connection = ArduinoConnection(print, print)
# connection.connect('COM3')
