# Usando la funcion input(), ademas del metodo .split() y 

numeros_str = input("Dame 3 numeros separados por espacio\n").split() # Todo lo que se reciba por input sera huardado en la string especificada.
 # La funcion al final del input toma al string recien creado y lo separa por espacios, convirtiendo al contenido en una lista
print(numeros_str)
suma = sum(numeros_str)
print(suma)