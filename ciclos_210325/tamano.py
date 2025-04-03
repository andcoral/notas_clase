# Saca los tamanos de genes de un archivo GFF

with open("genes.gff") as file:
    for linea in file: # Usamos ciclo for porque los archivos son iterables, en estos cada unidad pasada son lineas.
        columnas = linea.strip().split("\t") # Con '.strip()' quitamos todos los espacios en blanco al principio y final de las lineas (NO de en medio). Con '.split()' dividimos cada que se encuentre un tabulador y se guarda el contenido como un elemento de la lista "columna".
        if columnas[3].isdigit() and columnas[4].isdigit(): # Condicion para cersiorarnos de que los datos ingresados son numericos.
            tamano = int(columnas[4])-int(columnas[3])+1 # Funciones int() para volver esos valores de str a int. El "+1" es para no omitir un nucleotido.

            print(f"Gen de tamaño: {tamano} pb")