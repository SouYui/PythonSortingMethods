# Esta clase crea listas random y las ordena con los metodos de ordenamiento de la clase metodosOrdenamiento.py

import random as rn
import copy
from time import time
import metodosOrdenamiento as metodos

def crearLista(longitud):
    lista = []
    for i in range(0, longitud):
        lista.append(rn.randint(0, 200))
    return lista


if __name__ == "__main__":
    numeroElementos = 1500
    x = 10
    lista = crearLista(numeroElementos)
    listaSeleccion = copy.deepcopy(lista)
    listaInsercion = copy.deepcopy(lista)
    listaQuickSort = copy.deepcopy(lista)
    listaQuickSortDos = copy.deepcopy(lista)
    
    
    # ---------------------------------- Archivo para metodo burbuja   -------------------------------------
    archivo = open("m1.csv", "w")
    archivo.write("N,Tiempo\n")
    
    for i in range(10, numeroElementos, 10):
        listaNueva = copy.deepcopy(lista[:x])
        inicioTiempo = time()
        metodos.metodoBurbuja(listaNueva)
        transcurrido = time() - inicioTiempo
        archivo.write(str(x) + "," + format(transcurrido, ".7f") + "\n")
        x = x + 10
    archivo.close()
    
    # ---------------------------------- Archivo para metodo Seleccion   -------------------------------------
    archivoSeleccion = open("m2.csv", "w")
    archivoSeleccion.write("N,Tiempo\n")
    
    for i in range(10, numeroElementos, 10):
        listaNueva = copy.deepcopy(listaSeleccion[:x])
        inicioTiempo = time()
        metodos.metodoSeleccion(listaNueva)
        transcurrido = time() - inicioTiempo
        archivoSeleccion.write(str(x) + "," + format(transcurrido, ".7f") + "\n")
        x = x + 10
    archivoSeleccion.close()
    
    # ---------------------------------- Archivo para metodo Insercion   -------------------------------------
    archivoInsercion = open("m3.csv", "w")
    archivoInsercion.write("N,Tiempo\n")
    
    for i in range(10, numeroElementos, 10):
        listaNueva = copy.deepcopy(listaInsercion[:x])
        inicioTiempo = time()
        metodos.metodoInsercion(listaNueva)
        transcurrido = time() - inicioTiempo
        archivoInsercion.write(str(x) + "," + format(transcurrido, ".7f") + "\n")
        x = x + 10
    archivoInsercion.close()
    
    # ---------------------------------- Archivo para metodo QuickSort   -------------------------------------
    archivoQuickSort = open("m4.csv", "w")
    archivoQuickSort.write("N,Tiempo\n")
    
    for i in range(10, numeroElementos, 10):
        listaNueva = copy.deepcopy(listaQuickSort[:x])
        inicioTiempo = time()
        listaNueva = metodos.metodoQuickSortDos(listaNueva)
        transcurrido = time() - inicioTiempo
        archivoQuickSort.write(str(x) + "," + format(transcurrido, ".7f") + "\n")
        x = x + 10
    archivoQuickSort.close()
    
    # ---------------------------------- Archivo para metodo QuickSort Dos  -------------------------------------
    archivoQuickSortDos = open("m5.csv", "w")
    archivoQuickSortDos.write("N,Tiempo\n")
    
    for i in range(10, numeroElementos, 10):
        listaNueva = copy.deepcopy(listaQuickSortDos[:x])
        inicioTiempo = time()
        metodos.metodoQuickSortTres(listaNueva, 0, len(listaNueva) - 1)
        transcurrido = time() - inicioTiempo
        archivoQuickSortDos.write(str(x) + "," + format(transcurrido, ".7f") + "\n")
        x = x + 10
    archivoQuickSortDos.close()