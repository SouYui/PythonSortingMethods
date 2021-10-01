# Graficacion de los tiempos extraidos de los .csv creados en calcularTiempo.py

import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #Extraccion de datos por la separacion en el archivo de << , >>
    datos = pd.read_csv("m1.csv", sep=",")                  # Linea azul
    datosSeleccion = pd.read_csv("m2.csv", sep=",")         # Linea naranja
    datosInsercion = pd.read_csv("m3.csv", sep=",")         # Linea verde
    datosQuickSort = pd.read_csv("m4.csv", sep=",")         # Linea roja
    datosQuickSortDos = pd.read_csv("m5.csv", sep=",")      # Linea morada
    
    # Posicionamiento de datos en el eje x
    x = datos.N
    # Posicionamiento de datos en el eje y
    y = datos.Tiempo
    ySeleccion = datosSeleccion.Tiempo
    yInsercion = datosInsercion.Tiempo
    yQuickSort = datosQuickSort.Tiempo
    yQuickSortDos = datosQuickSortDos.Tiempo
    
    # Ploteo de los datos con sus ejes. Al ser x la misma cantidad de datos, todos tienen los mismos y cambiara en y solamente.
    plt.plot(x, y, x, ySeleccion, x, yInsercion, x, yQuickSort)
    plt.xlabel("Numero de elementos")
    plt.ylabel("Tiempo en segundos")
    plt.title("Burbuja vs Seleccion vs Insercion vs QuickSort")
    plt.grid()
    plt.show()