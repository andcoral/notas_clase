# Usando "break" para detener un bucle antes de que termine. Con programa que para al encontrar una base en específico.

secuencia = "ATGCGTACGTAG"
buscar = "C"
for base in secuencia:
    if base == buscar:
        print(f"Base '{buscar}' encontrada, deteniendo el bucle.")
        break
    print(base)