import customtkinter as ctk
import tkinter, tkintermapview
from SensorDisplay import SensorDisplay

global data

class ShowMap(ctk.CTkFrame):
    """
    Clase para mostrar un mapa en un marco de Tkinter.

    Args:
        master (tk.Widget): El widget principal al que se adjunta el marco.
        **kwargs: Argumentos adicionales para personalizar el marco.
    """
    def __init__(self, master, **kwargs):
        """
        Inicializa la instancia de ShowMap.

        Args:
            master (tk.Widget): El widget principal al que se adjunta el marco.
            **kwargs: Argumentos adicionales para personalizar el marco.
        """
        super().__init__(master, **kwargs)
        self.configure(corner_radius=10)
        
        map_widget = tkintermapview.TkinterMapView(self, corner_radius=8)
        map_widget.pack(fill='both', expand=True)

        # Configuración de la posición del mapa (coordenadas de ejemplo)
        map_widget.set_position(19.42847, -99.12766)
