# Saca los tamanos de genes de un archivo GFF

with open("genes.gff") as file:
    for linea in file: # Usamos ciclo for porque los archivos son iterables, en estos cada unidad pasada son lineas.
        print(linea)

