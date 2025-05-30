# del 16 de mayo
import pandas as pd

# Transformando en DataFrame y leyendo el archivo csv
df = pd.read_csv('genes.csv', header= 0)
print(df)

# Cambiar el nombre de una columna
df_renombrado = df.rename(mapper= {'Función' : 'Tipo_funcional'}, axis= 1, inplace= False) 
# ^ Cambio de nombre con "mapper" y vía diccionario
# ^ "axis" es igual a 1 pq queremos modificar una columna
# ^ "inplace= False" para que no modifique el df original
print(df_renombrado)
# Otra opcion habria sido: 
# df_renombrado = df.rename(columns={'Función': 'Tipo_funcional'})
# print(df_renombrado.columns)

# Estandarizar valores
df_estandarizado = df.replace( {'Función' : {'enzima' : 'enzima metabólica' ,'regulador' : 'TF'}}, {'Nombre' : {'thrA' : 'Pablo'}} )
print(df_estandarizado)
# Reemplaza todos los valores que se encuentran en la columna titulada 'Función' que sean 'enzima' por 'enzima metabólica' (nomas algo mas específico)
# En la misma columna que arriba cambia 'regulador' por 'TF' (dentro del mismo diccionario)
# En otra columna, y por lo tanto otro diccionario, cambia el nombre 'thrA' por 'Pablo'

# Eliminar columnas o filas innecesarias
df_sin_col = df.drop(columns=['Expresión']) # Elimina toda la columna etiquetada como 'Expresión'
print(df_sin_col)

df_sin_fil = df.drop(index=1) # Elimina toda la fila con índice 1, la de "thrA"
print(df_sin_fil)

# Asegurar el tipo correcto de datos
df['Longitud en decimales'] = df['Longitud'].astype(float) # Agregando columna de tipo uniforme de datos (Esto fue en el DataFrame original, q NO es lo recomendado)
print(df.dtypes)
df.drop(columns= 'Longitud en decimales') # Columna nueva borrada por lo que veremos de lambda a continuacion 

# Clasificación de genes por longitud
df['Clasificación longitud'] = df['Longitud'].apply(lambda len : 'Largo' if len > 1000 else 'Corto' )
# Se agrega nueva columna 'Clasificación'
# A los valores en la columna 'Longitud' se les aplica [.apply()] la mini funcion lambda
# "len" serán todos los valores que están en la columna 'Longitud'
# Lambda asigna 'Largo' en caso de que el valor metido sea mayor a 1000, de lo contrario asigna 'Corto'
print(df)

# Clasificacion de genes por expresion
df['Nivel de expresión'] = df['Expresión'].apply(lambda x : 'Sobreexpresado' if x > 35 else 'Subexpresado')
print(df)

# Crear una columna con valores derivados
df_nuevo = df.assign(LogExpresión = df['Expresión'].apply(lambda val: round(val ** 0.5, 2))) 
# A partir de otro (df), crea un nuevo DataFrame (df_nuevo), con una columna extra 'LogExpresión'.
# La nueva columna tomara a los valores de la columna 'Expresión' y les hara una operacion.
print(df_nuevo[['Expresión', 'LogExpresión']]) # Impresion de columnas de interes

# Solucion vista en clase, que al final lleva al mismo resultado de arriba, pero de distinto camino
#df_nuevo = df.assign(LogExpresión=lambda x: x['Expresión'].apply(lambda val: round(val ** 0.5, 2)))
# Se crea nueva columna ('LogExpresión') en DataFrame copia
# Cada valor en la columna nueva estará formado por...
# Tomar cada uno de los valores de la columna 'Expresión'
# A cada uno de esos valores le va aplicar la operación: round(val ** 0.5, 2) [Q es calcular la raíz cuadrada de un número, y sacar el resultado con solo 2 cifras decimales]
# Se usó el primer lambda para acceder a los valores de la columna 'Longitud', y el segundo lambda para hacer el cálculo debido con ese valor.
#print(df_nuevo[['GeneID', 'Expresión', 'LogExpresión']]) # Impresion de columnas de interes

# Ordenar el DataFrame
df_ordenado = df.sort_values(by='Longitud', ascending=False) 
# ^ Metodo para ordenar los valores de la columna 'Longitud' de mayor a menor.
print(df_ordenado[['GeneID', 'Longitud']])

# Reiniciar el indice
# El DataFrame q queda del ejercicio anterior tiene los indices revueltos, vamos a arreglarlos respetando el orden nuevo.
df_reset =  df_ordenado.reset_index(drop=True) # Metodo .reset_index() para reordenar. "drop=True" quita la columna conservada de los indices anteriores
print(df_reset[['GeneID', 'Longitud']])


# Establecer una columna como índice (AMbas opciones tienen mismo resultado, diferente procedimiento)

# Opcion1. Lo hace desde el cargado de DataFrame
df2 = pd.read_csv('genes2_setindex.csv', header= 0, index_col= 0) # Cree un nuevo archivo para que no fallen ejercicios anteriores
# Archivo origen. Encabezado primer fila. Mi primer columna es el index
print(df2)

# Opcion2. Lo hace después, con un método posterior al cargado de DataFrame
df2 = pd.read_csv('genes2_setindex.csv', header= 0)
# Archivo origen. Encabezado primer fila.
df_indexado = df2.set_index('0')
# Creacion nuevo DataFrame que tenga indices a la columna 0 del df anterior.
print(df_indexado)


# Ejercicios solitos

# 1
df['Nivel'] = df['Expresión'].apply(lambda x: 'Alta' if x > 40 else 'Media' if x>15 else 'Baja') 
print(df)

# 2
df_clasificado = df.assign(Tipo = df['Función'].apply(lambda x: 'Metabólico' if x == 'enzima' else 'Otro'))
print(df_clasificado[['GeneID', 'Función', 'Tipo']])

# 3
df_gene_modificado = df.assign(GeneID_modificado = df['GeneID'].apply(lambda x : 'eco_' + x))
# Crea nuevo DataFrame con una columna extra ('GeneIN_modificado'), a partir de uno anterior
# A los valores de la columna 'GeneID' les aplica una lambda que les agrega el prefijo "eco_"
print(df_gene_modificado[['GeneID', 'GeneID_modificado']])