import serial
import serial.tools.list_ports
import threading

class ArduinoConnection:
    """
    Clase para manejar la conexión con un Arduino.

    Args:
        update_status_callback (function): Función de devolución de llamada para actualizar el estado.
        update_sensor_data_callback (function): Función de devolución de llamada para actualizar los datos del sensor.
    """
    def __init__(self, update_status_callback, update_sensor_data_callback):
        """
        Inicializa una instancia de ArduinoConnection.

        Args:
            update_status_callback (function): Función de devolución de llamada para actualizar el estado.
            update_sensor_data_callback (function): Función de devolución de llamada para actualizar los datos del sensor.
        """
        self.arduino = None
        self.update_status = update_status_callback
        self.update_sensor_data = update_sensor_data_callback

    def get_ports(self):
        """
        Obtiene una lista de puertos seriales disponibles.

        Returns:
            list: Una lista de nombres de puertos seriales disponibles.
        """
        return [port.device for port in serial.tools.list_ports.comports()]

    def connect_arduino(self, port):
        """
        Conecta con un Arduino en el puerto especificado.

        Args:
            port (str): El nombre del puerto serial al que se conectará.
        """
        try:
            self.arduino = serial.Serial(port, 9600, timeout=0.1)
            self.update_status("Conexión establecida")
            print("Arduino connected at:", port)
            self.start_reading()  # Start reading immediately after connecting
        except serial.SerialException as e:
            self.update_status(f"Conexión no establecida: {str(e)}")
            print("Failed to connect:", e)

    def disconnect_arduino(self):
        """Desconecta el Arduino."""
        if self.arduino and self.arduino.is_open:
            self.arduino.close()
            self.update_status("Desconectado")
            print("Arduino disconnected.")
        self.arduino = None

    def connect(self, port):
        """
        Inicia un hilo para conectar con el Arduino.

        Args:
            port (str): El nombre del puerto serial al que se conectará.
        """
        thread = threading.Thread(target=self.connect_arduino, args=(port,))
        thread.daemon = True
        thread.start()

    def disconnect(self):
        """Inicia un hilo para desconectar del Arduino."""
        thread = threading.Thread(target=self.disconnect_arduino)
        thread.daemon = True
        thread.start()

    def start_reading(self):
        """Inicia un hilo para leer los datos del Arduino."""
        if not self.arduino or not self.arduino.is_open:
            self.update_status("No hay conexión con el Arduino.")
            return
        self.reading_thread = threading.Thread(target=self.read_data)
        self.reading_thread.daemon = True
        self.reading_thread.start()

    def read_data(self):
        """Lee los datos del Arduino."""
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
        """
        Analiza los datos recibidos del Arduino.

        Args:
            line (str): La cadena de datos recibida desde el Arduino.

        Returns:
            list or None: Los datos parseados como una lista de valores flotantes, o None si hay un error.
        """
        try:
            data_str = line.strip('[]')
            data_list = [float(val) for val in data_str.split(',')]
            return data_list
        except Exception as e:
            print("Error parsing data:", e)
            return None

# Ejemplo de uso (comentado para evitar la ejecución):
# connection = ArduinoConnection(print, print)
# connection.connect('COM3')
