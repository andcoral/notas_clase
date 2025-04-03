# Usando la funcion input(), ademas del metodo .split() y la funcion map() que convierte tipos de datos.

numeros_str = input("Dame 3 numeros separados por espacio\n").split() # Todo lo que se reciba por input sera huardado en la string especificada.
 # La funcion al final del input toma al string recien creado y lo separa por espacios, convirtiendo al contenido en una lista
lista_numeros = map(int,numeros_str) # GUardamos en una lista los datos convertidos del tipo string a int para poder aplicarles sum()
print(lista_numeros) # Descubrimos que el objeto map tambien es un iterable, porque sum() pudo trabajar con el.
suma = sum(lista_numeros) # Funcion sum()
print(suma)