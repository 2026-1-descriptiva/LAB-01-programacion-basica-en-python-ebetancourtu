"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("./files/input/data.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        datos = {}
        for row in reader:
            letra = row[0]
            valor = int(row[1])
            if letra not in datos:
                datos[letra] = [valor, valor]  # [max, min]
            else:
                datos[letra][0] = max(datos[letra][0], valor)
                datos[letra][1] = min(datos[letra][1], valor)
    return [(letra, vals[0], vals[1]) for letra, vals in sorted(datos.items())]