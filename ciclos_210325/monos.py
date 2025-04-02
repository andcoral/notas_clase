# Recorre al objeto iterable: lista

apes = ["Pongo pygmaeus", "Pan troglodytes", "Gorilla gorilla"]

for ape in apes: # Pasa por cada elemento de la lista
    name_length = len(ape) # Funcion len() que cuenta el numero de componentes de la string guardada en la posicion de la celda que estemos.
    first_letter = ape[0] # Asignamos a la letra en la primera posicion (la cero) de la string en la celda que estemos.
    
    # La forma en que se usa el print a continuacion es la de una version antigua y no tan amigable.
    print(ape + " is an ape. Its name starts with " + first_letter)
    print("Its name has " + str(name_length) + " letters") # Se agrego lo de "str" antes de la variable "length_name" porque el "+" usado es para concatenar UNICAMENTE string, y no int como es nuestra variable.