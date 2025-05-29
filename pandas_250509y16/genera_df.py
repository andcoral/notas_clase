'''
Formas distintas de generar DataFrames:
Lista de diccionarios, desde un archivo, diccionario de listas, diccionario de Series (pandas),  
lista de listas o tuplas, copiar otro data frame y array de NumPy (no mucha idea de ese).
'''
import pandas as pd

# Creando DataFrames...

# Desde una lista de diccionarios
data = [
    {'nombre': 'Ana', 'edad': 25},
    {'nombre': 'Luis', 'edad': 30}
]
df = pd.DataFrame(data)

print(df)
# print(df['nombre']) 
# Palabra/clave queda como nombre de columna y definicion/ como contenido de columna

# Desde un archivo
df = pd.read_csv("genes.gff", sep= '\t', comment= '#', header= None)
# ^ La funcion pandas para convertir de archivo a DataFrames con sus especificaciones necesarias
print(df)
# Empleando el método .describe()
#df = pd.read_csv("genes.gff", sep= '\t', comment= '#', header= None).describe()
#print(df)

# Desde diccionarios de listas
data = {
    'Nombre': ['Ana', 'Luis', 'Pedro'],
    'Edad': [23, 30, 25]
}
# La clave sera el nombre de las columnas y las listas el contenido (renglones)
df = pd.DataFrame(data)
print(df)