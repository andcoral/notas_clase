import pandas as pd

df = pd.read_csv('genes.csv', header = 0)
print(df)

# Ejercicio 1 (básico): Conteo de genes por función

df_count = df.groupby('Función').count()
print(df_count['GeneID']) # SIn 'Función' pq ya se volvió el index, y si lo especificamos da error

# Ejercicio 2 (intermedio): Promedio de longitud por función

df_promedio = df.groupby('Función')['Longitud'].mean().sort_values(ascending= False)
print(df_promedio)

# Ejercicio 3 (intermedio-avanzado): Estadísticas múltiples de expresión

# Agrupamos por función y aplicamos múltiples estadísticas a la columna 'Expresión'
resumen = df.groupby('Función')['Expresión'].agg(['mean', 'max', 'min', 'count'])
# Renombramos las columnas para mayor claridad (opcional)
resumen.columns = ['Media', 'Máximo', 'Mínimo', 'Cantidad']
# Mostramos el resultado
print(resumen)