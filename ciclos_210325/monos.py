# Recorre al objeto iterable: lista

apes = ["Pongo pygmaeus", "Pan troglodytes", "Gorilla gorilla"]

for ape in apes: # Pasa por cada elemento de la lista
    name_length = len(ape) # Funcion len() que cuenta el numero de componentes de la string guardada en la posicion de la celda que estemos.
    first_letter = ape[0] # Asignamos a la letra en la primera posicion (la cero) de la string en la celda que estemos.
    
    # Usamos f-strings para tener valores de variables en la impresion.
    print(f"{ape} is an ape. Its name starts with '{first_letter}'.\nIts name has {name_length} letters")