secuencia = tuple("ATGCTTCGA")

print("La cantidad de veces que aparecio cada base en tu secuencia es:")

# Forma 1
print(f"A = {secuencia.count("A")}\tT = {secuencia.count("T")}\tG = {secuencia.count("G")}\tC = {secuencia.count("C")}\n")

# Forma 2 - Comprension de listas
bases = list("ATGC")
freq = [(base, secuencia.count(base)) for base in bases]
print(freq)

# Forma 3 - Ciclos
for base in "ATGC":
    print(f"{secuencia.count(base)} repeticiones de {base}")