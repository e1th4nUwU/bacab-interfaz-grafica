# Cansat GUI 🛰️📊

Este es un proyecto de interfaz gráfica para visualizar datos de un CanSat (Satélite en una lata), diseñado para mostrar datos de sensores en tiempo real, como temperatura, presión, coordenadas GPS, orientación y aceleración.

## Requerimientos 📋

Para ejecutar este proyecto, necesitarás tener instalado Python 3 y los paquetes especificados en el archivo `requirements.txt`.

### Instalación de los requerimientos 💻

Para instalar los requerimientos, ejecuta el siguiente comando en tu terminal:

```bash
pip install -r requirements.txt
```
Se recomienda que uses un entorno virtual para instalar los requerimientos, para más información visita la [documentación oficial de Python](https://docs.python.org/3/library/venv.html).

### Estructura del proyecto 📂
El proyecto consta de varios archivos:

* main.py: Este es el punto de entrada del programa. Ejecutar este archivo iniciará la interfaz gráfica.
* SensorDisplay.py: Este archivo contiene la clase SensorDisplay que representa la interfaz gráfica para mostrar datos de sensores.
* funcionmap.py: Este archivo contiene la clase ShowMap que muestra un mapa en la interfaz gráfica utilizando la biblioteca tkintermapview.
* conexion_arduino.py: Este archivo contiene la clase ArduinoConnection que se encarga de la conexión con el Arduino y la lectura de datos de los sensores.

## Uso 🚀
Para ejecutar la interfaz gráfica, simplemente ejecuta el archivo 'main.py' con Python:
```bash
python main.py
```
Esto abrirá la ventana de la interfaz gráfica donde podrás ver los datos en tiempo real.

## Construido con 🛠️
* [Python](https://www.python.org/) - Lenguaje de programación
* [Tkinter](https://docs.python.org/3/library/tkinter.html) - Biblioteca para crear interfaces gráficas
* [PySerial](https://pyserial.readthedocs.io/en/latest/pyserial.html) - Biblioteca para la comunicación serial con Arduino
* [Matplotlib](https://matplotlib.org/) - Biblioteca para la visualización de datos