# Uso de "continue" que salta a la siguiente iteracion segun una condicion.

secuencia = "ATGCGTACGTAG"
for base in secuencia:
    if base == "C":
        continue
    print(base, end="")

print("\n")