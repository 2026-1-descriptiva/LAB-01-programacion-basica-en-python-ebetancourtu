"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    with open("./files/input/data.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        resultado = []
        for row in reader:
            letra = row[0]
            col4 = len(row[3].split(","))  # "b,g,f" -> 3 elementos
            col5 = len(row[4].split(","))  # "jjj:12,bbb:3,..." -> 5 elementos
            resultado.append((letra, col4, col5))
    return resultado