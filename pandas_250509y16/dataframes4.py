# del 16 de mayo

import pandas as pd
# Leer archivo GFF ignorando comentarios
df = pd.read_csv(
    "genes.gff",
    sep="\t",                # Separador tabulado
    comment="#",             # Ignorar líneas que comienzan con #
    header=None,             # No hay cabecera en el archivo
    names=["seqid", "source", "type", "start", "end", "score", "strand", "phase", "attributes"]
)
print(df)

# Usando metodos, atributos, procedimientos
print("Uso de metodos:")
print(df.head(3))
print(df.tail(3))
print(df.info())
print(df.shape) # NO lleva paréntesis porque es un atributo del objeto
print(df.columns) # Devuelve los nombres de las columnas como una serie


df = pd.DataFrame() # Vacio el DataFrame, aunque creo es innecesario

# Leer un DataFrame
df = pd.read_csv('expresion_genica.tsv', sep= '\t', header= 0) # Indicando ruta, separadores y encabezado
print("Leyendo un DataFrame:")
print(df)

# Ejercicios:

# Identificarle genes altamente expresados en las tres condiciones
print("Genes altamente expresados:")
df_altos = df[(df['cond1'] > 1000) & (df['cond2'] > 1000) & (df['cond3'] > 1000)].copy() # El ultimo metodo para que sea propio y no un apuntador
print(df_altos) # Observar el nuevo DataFrame (no una vista) creado

# Calcular el promedio de expresion por gen (por filas)
#print(df[['cond1', 'cond2', 'cond3']].dtypes) # Era para saber si podia operarlos por su tipo de dato
#print(df.columns, df_altos.columns) # Era para ver si los df contenian la misma informacion
df_altos['promedios'] = df_altos[['cond1', 'cond2', 'cond3']].mean(axis=1) # Creacion nueva columna con promedios
print(df_altos['promedios']) # Viendo solo columna nueva

# Ordenar de mayor a menor promedio
ordenados = df_altos.sort_values(by= 'promedios', ascending= False) 
# ^ Metodo con sus parametros para la columna de interes y el orden deseado (descendente)

# Exportar el resultado
ordenados.to_csv('ordenados.csv', sep= ',', index= False, header= True) 
# ^ Nueva funcion con parametros: destino, separadores nuevos, ignorar el index anterior, conservar el header anterior
print("Leyendo el archivo creado a partir de los resultados:")
print(pd.read_csv('ordenados.csv', sep= ','))