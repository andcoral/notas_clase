# Visualizando distintas funciones de Python 

# enumerate(), que nos regresa 2 valores, la posicion y el contenido dentro de una string
secuencia = "ATGCGT"
for i, base in enumerate(secuencia): # 2 valores despues del for, por los 2 que regresa la funcion: índice, valor
    print(f"Posición {i}: {base}")


# zip(), itera sobre multiples listas a la vez
bases = "ATGC"
complementos = "TACG"
for base, complemento in zip(bases, complementos): # Van los 2 iteradores despues del in. Num de iterables = Num de variables 
    print(f"{base} → {complemento}")

# Cuando los iterables NO son del mismo tamano, la funcion zip() simplemente los compara al tamano del mas chico.
genes = ["thrL", "thrA", "thrB"]
longitudes = [66, 2463]  # Lista más corta
for gen, tamaño in zip(genes, longitudes):
    print(f"Gen: {gen}, Tamaño: {tamaño} pb")
