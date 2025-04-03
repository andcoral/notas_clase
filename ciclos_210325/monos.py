# Recorre al objeto iterable: lista

apes = ["Pongo pygmaeus", "Pan troglodytes", "Gorilla gorilla"]

for ape in apes: # Pasa por cada elemento de la lista
    # Usamos f-strings para tener valores de variables en la impresion.
    print(f"{ape} is an ape. Its name starts with '{ape[0]}'.\nIts name has {len(ape)} letters.")