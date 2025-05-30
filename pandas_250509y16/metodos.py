# METODOS. Del 16
import pandas as pd


# .groupby()

df = pd.read_csv('genes.csv')
media_por_funcion = df.groupby('Función')['Expresión'].mean()
# Calcula la media de la columna Expresión, agrupada por valores únicos de la columna Función.
print(media_por_funcion)

genes_por_funcion = df.groupby('Función')['GeneID'].count()
print(genes_por_funcion)

longitud_promedio = df.groupby('Función')['Longitud'].mean()
print(longitud_promedio)

impacto_expresion = df.groupby('Función')['Expresión'].sum()
print(media_por_funcion)


# .agg()

import pandas as pd
df = pd.DataFrame({
    'Expresión': [10, 20, 30, 40]
})
resumen = df.agg(['mean', 'max', 'min'])
print(resumen)


# Usando ambos métodos

df = pd.read_csv('genes.csv')

resumen = df.groupby('Función')['Expresión'].agg(['mean', 'max', 'min', 'count'])
print(resumen)

# Añadir clasificación por longitud
df['Clasificación'] = df['Longitud'].apply(lambda x: 'Largo' if x > 1500 else 'Corto')
# Agrupar por Función y Clasificación
agrupado = df.groupby(['Función', 'Clasificación'])['GeneID'].count()
print(agrupado)