# Visualizando distintas funciones de Python 

# enumerate(), que nos regresa 2 valores, la posicion y el contenido dentro de una string
secuencia = "ATGCGT"
for i, base in enumerate(secuencia): # 2 valores despues del for, por los 2 que regresa la funcion: índice, valor
    print(f"Posición {i}: {base}")