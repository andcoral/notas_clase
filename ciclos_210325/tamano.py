# Saca los tamanos de genes de un archivo GFF

with open("genes.gff") as file:
    for linea in file: # Usamos ciclo for porque los archivos son iterables, en estos cada unidad pasada son lineas.
        columnas = linea.strip().split("\t") # Con '.strip()' quitamos todos los espacios en blanco al principio y final de las lineas (NO de en medio). Con '.split()' dividimos cada que se encuentre un tabulador y se guarda el contenido como un elemento de la lista "columna".
        print(columnas[3])