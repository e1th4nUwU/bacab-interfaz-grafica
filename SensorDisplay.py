import customtkinter as ctk

class SensorDisplay(ctk.CTkFrame):
    """
    Clase para mostrar los datos de los sensores en una interfaz gráfica.

    Args:
        master (tk.Widget): El widget padre al que se adjunta el marco.
        **kwargs: Argumentos adicionales para personalizar el marco.
    """
    def __init__(self, master, **kwargs):
        """
        Inicializa una instancia de SensorDisplay.

        Args:
            master (tk.Widget): El widget padre al que se adjunta el marco.
            **kwargs: Argumentos adicionales para personalizar el marco.
        """
        super().__init__(master, **kwargs)
        self.configure(corner_radius=10)
        self.setup_widgets()

    def setup_widgets(self):
        """
        Configura los widgets para mostrar los datos de los sensores.
        """
        # Define estilos de fuente
        font_default = ("Times New Roman", 20)
        font_data = ("System", 18)

        no_filas = 8
        no_columnas = 4

        for i in range(no_filas):
            self.rowconfigure(i, weight=1)  # Hace que las filas crezcan con el marco
        for j in range(no_columnas):
            self.columnconfigure(j, weight=1)  # Hace que las columnas crezcan con el marco

        # Inicializa etiquetas y valores para cada sensor
        # Temperatura
        self.label_temperatura = ctk.CTkLabel(self, text="Temperatura", font=font_default)
        self.label_temperatura.grid(row=0, column=0, padx=10)
        self.value_temperatura = ctk.CTkLabel(self, text="0 °C", font=font_data, fg_color="#535862", corner_radius=5)
        self.value_temperatura.grid(row=1, column=0, padx=10)

        # Presión
        self.label_presion = ctk.CTkLabel(self, text="Presión", font=font_default)
        self.label_presion.grid(row=0, column=1, padx=10)
        self.value_presion = ctk.CTkLabel(self, text="0 Pa", font=font_data, fg_color="#535862", corner_radius=5)
        self.value_presion.grid(row=1, column=1, padx=10)

        self.labelCP = ctk.CTkLabel(self, text= " ---  CARGA PRIMARIA  ---", font=font_default)
        self.labelCP.grid(row=2, column=0, columnspan=2, padx=10)

        # Latitud CP
        self.label_latitud = ctk.CTkLabel(self, text="Latitud", font=font_default)
        self.label_latitud.grid(row=3, column=0, padx=10)
        self.value_latitud = ctk.CTkLabel(self, text="0 °", font=font_data, fg_color="#535862", corner_radius=5)
        self.value_latitud.grid(row=4, column=0, padx=10)

        # Longitud CP
        self.label_longitud = ctk.CTkLabel(self, text="Longitud", font=font_default)
        self.label_longitud.grid(row=3, column=1, padx=10)
        self.value_longitud = ctk.CTkLabel(self, text="0 °", font=font_data, fg_color="#535862", corner_radius=5)
        self.value_longitud.grid(row=4, column=1, padx=10)
        
        self.labelCS = ctk.CTkLabel(self, text= "---  CARGA SECUNDARIA  ---", font=font_default)
        self.labelCS.grid(row=5, column=0, columnspan=2, padx=10)

        # Latitud CS
        self.label_latitud2 = ctk.CTkLabel(self, text="Latitud", font=font_default)
        self.label_latitud2.grid(row=6, column=0, padx=10)
        self.value_latitud2 = ctk.CTkLabel(self, text="0 °", font=font_data, fg_color="#535862", corner_radius=5)
        self.value_latitud2.grid(row=7, column=0, padx=10)

        # Longitud CS
        self.label_longitud2 = ctk.CTkLabel(self, text="Longitud", font=font_default)
        self.label_longitud2.grid(row=6, column=1, padx=10)
        self.value_longitud2 = ctk.CTkLabel(self, text="0 °", font=font_data, fg_color="#535862", corner_radius=5)
        self.value_longitud2.grid(row=7, column=1, padx=10)

        # Orientación
        self.label_orientacion_label = ctk.CTkLabel(self, text="Orientación", font=font_default)
        self.label_orientacion_label.grid(row=0, column=2, padx=10)

        # Orientación X
        self.value_orientacionx = ctk.CTkLabel(self, text="0 °", font=font_data, fg_color="#535862", corner_radius=5)
        self.value_orientacionx.grid(row=2, column=2, padx=10)

        # Orientación Y
        self.value_orientaciony = ctk.CTkLabel(self, text="0 °", font=font_data, fg_color="#535862", corner_radius=5)
        self.value_orientaciony.grid(row=4, column=2, padx=10)

        # Orientación Z
        self.value_orientacionz = ctk.CTkLabel(self, text="0 °", font=font_data, fg_color="#535862", corner_radius=5)
        self.value_orientacionz.grid(row=6, column=2, padx=10)

        # Aceleración
        self.label_aceleracion = ctk.CTkLabel(self        , text="Aceleración", font=font_default)
        self.label_aceleracion.grid(row=0, column=3, padx=10)

        # Aceleración X
        self.value_aceleracionx = ctk.CTkLabel(self, text="0 m/s²", font=font_data, fg_color="#535862", corner_radius=5)
        self.value_aceleracionx.grid(row=2, column=3, padx=10)

        # Aceleración Y
        self.value_aceleraciony = ctk.CTkLabel(self, text="0 m/s²", font=font_data, fg_color="#535862", corner_radius=5)
        self.value_aceleraciony.grid(row=4, column=3, padx=10)

        # Aceleración Z
        self.value_aceleracionz = ctk.CTkLabel(self, text="0 m/s²", font=font_data, fg_color="#535862", corner_radius=5)
        self.value_aceleracionz.grid(row=6, column=3, padx=10)

    def update_sensor_data(self, new_data):
        """
        Actualiza los valores de los sensores en la interfaz gráfica con los nuevos datos.

        Args:
            new_data (list): Lista de datos de los sensores en el siguiente orden:
                             [temperatura, presion, latitud_CP, longitud_CP, latitud_CS, longitud_CS,
                              orientacion_x, orientacion_y, orientacion_z, aceleracion_x, aceleracion_y, aceleracion_z]
        """
        # Actualizar los valores directamente basados en el orden de la lista
        self.value_temperatura.configure(text=f"{new_data[0]} °C")
        self.value_presion.configure(text=f"{new_data[1]} Pa")
        self.value_latitud.configure(text=f"{new_data[2]} °")
        self.value_longitud.configure(text=f"{new_data[3]} °")
        self.value_latitud2.configure(text=f"{new_data[4]} °")
        self.value_longitud2.configure(text=f"{new_data[5]} °")
        self.value_orientacionx.configure(text=f"{new_data[6]} m/s²")
        self.value_orientaciony.configure(text=f"{new_data[7]} m/s²")
        self.value_orientacionz.configure(text=f"{new_data[8]} m/s²")
        self.value_aceleracionx.configure(text=f"{new_data[9]} m/s²")
        self.value_aceleraciony.configure(text=f"{new_data[10]} m/s²")
        self.value_aceleracionz.configure(text=f"{new_data[11]} m/s²")

