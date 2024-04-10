import csv

with open("datos.csv") as datos: #apertura de la conexión al archivo csv con Python
    todos_datos = csv.reader(datos) #todos los renglones del archivo
    for renglon in todos_datos: #bucle de leer un renglon a la vez
        usuario,clave,mail = renglon #guardo en 3 variables por renglon
        print()