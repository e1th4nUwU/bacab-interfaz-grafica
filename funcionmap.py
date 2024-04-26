import customtkinter as ctk
import tkinter, tkintermapview
from SensorDisplay import SensorDisplay

global data
class ShowMap(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(corner_radius=10)
        
        map_widget = tkintermapview.TkinterMapView(self, corner_radius=8)
        map_widget.pack(fill='both', expand=True)

        map_widget.set_position(19.42847, -99.12766) # Coordenadas 
'''
        datos = SensorDisplay(self).update_sensor_data(data)
        print(datos)
'''