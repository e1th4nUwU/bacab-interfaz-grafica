import customtkinter as ctk
from SensorDisplay import SensorDisplay
from conexion_arduino import ArduinoConnection
from funcionmap import ShowMap
import traceback
import tkinter, tkintermapview
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Global variable initialization
arduino_conn = None
status_label = None
frame_00 = None
combobox_ports = None

def main():
    try:
        app = create_main_window()
        app.mainloop()
    except Exception as e:
        print("Error caught in main loop:")
        traceback.print_exc()

# Crear una función para actualizar la etiqueta de estado de la UI
def update_status(status):
    status_label.configure(text=status)

def update_sensor_data(data):
    # Esta función será llamada con los datos recibidos del Arduino.
    # Aquí actualizamos los widgets de la UI con los nuevos datos.
    # Debes asegurarte de que esta actualización se ejecute en el hilo principal.
    frame_00.update_sensor_data(data)

def create_main_window():
    global arduino_conn, combobox_ports, status_label, frame_00

    # Configuración inicial de la ventana principal
    app = ctk.CTk()
    app.title("Estación Terrena Bacab")
    app.geometry("800x600")  # Tamaño inicial, pero será redimensionable

    # Frame principal y configuración de grid para responsividad
    main_frame = ctk.CTkFrame(master=app, corner_radius=10)
    main_frame.pack(fill="both", expand=True)
    main_frame.configure(fg_color="black")  # Fondo negro
    # main_frame.rowconfigure(0, weight=1)  # Hace que la primera fila crezca con la ventana
    # main_frame.columnconfigure(0, weight=1)  # Hace que la primera columna crezca con la ventana

    # Configuración del grid dentro del frame principal
    # Configurar los pesos para responsividad
    rows = 2
    columns = 3
    for row in range(rows):
        main_frame.rowconfigure(row, weight=1)
    for col in range(columns):
        main_frame.columnconfigure(col, weight=1)

    # Creación específica de cada sub-frame con nombre de coordenada (fila, columna)
    frame_00 = SensorDisplay(main_frame)
    frame_00.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    # Instantiate ArduinoConnection with proper callbacks
    arduino_conn = ArduinoConnection(update_status, update_sensor_data)

    frame_02 = ctk.CTkFrame(master=main_frame, corner_radius=10)
    frame_02.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

    # ======= FRAME PARA CONECTAR A ARDUINO =======
    frame_10 = ctk.CTkFrame(master=main_frame, corner_radius=10)
    frame_10.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    combobox_ports = ctk.CTkComboBox(frame_10, values=arduino_conn.get_ports())
    combobox_ports.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    # Botón de actualización
    button_refresh = ctk.CTkButton(frame_10, text="Actualizar Puertos", command=lambda: update_combobox_ports(arduino_conn.get_ports()))
    button_refresh.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    # Botón de conexión
    button_connect = ctk.CTkButton(frame_10, text="Conectar", command=lambda: arduino_conn.connect(combobox_ports.get()))
    button_connect.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    # Botón de desconexión
    button_disconnect = ctk.CTkButton(frame_10, text="Desconectar", command=lambda: disconnect_device())
    button_disconnect.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    global status_label
    # Etiqueta de estado de la conexión
    status_label = ctk.CTkLabel(frame_10, text="Desconectado")
    status_label.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    # Función wrapper para el botón de desconexión
    def disconnect_device():
        if arduino_conn:
            arduino_conn.disconnect()

    # ======== FINALIZA LO CORRESPONDIENTE AL FRAME CONECTAR ARDUINO =======

    # ======== Graficas =========
    frame_11 = ctk.CTkFrame(master=main_frame, corner_radius=10)
    frame_11.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

    frame_label = ctk.CTkLabel(master=frame_11, text=" GRAFICAS ")
    frame_label.pack()

    # def create_plot(frame):
    #     fig, ax = plt.subplots()
    #     ax.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])  # Ejemplo de datos para la gráfica

    #     canvas = FigureCanvasTkAgg(fig, master=frame)  # A Tk drawing area
    #     canvas.draw()
    #     canvas.get_tk_widget().pack(fill='both', expand=True)
    
    # create_plot(frame_11)  # Aquí se agrega la gráfica
    # ======== Finaliza zona graficas ==========

    # ======== MAPA ========
    frame_12 = ShowMap(main_frame)#ctk.CTkFrame(master=main_frame, corner_radius=10)
    frame_12.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

    def on_closing():
        global arduino_conn  # Declarar como global para acceder a ella
        if arduino_conn:
            arduino_conn.disconnect()
        app.destroy()
        
    def update_combobox_ports(new_ports):
        try:
            global combobox_ports
            # Guarda la configuración actual del grid antes de destruir el combobox
            grid_info = combobox_ports.grid_info()
            
            combobox_ports.destroy()
            
            combobox_ports = ctk.CTkComboBox(frame_10, values=new_ports)
            # Aplica la misma configuración de grid al nuevo combobox
            combobox_ports.grid(**grid_info)
            
            if new_ports:
                combobox_ports.set(new_ports[0])
        except Exception as e:
            print("Error updating combobox:", e)


    app.protocol("WM_DELETE_WINDOW", on_closing)  # Para manejar el cierre de la ventana
    return app

# Uso de la función main para iniciar la aplicación
if __name__ == "__main__":
    main()
