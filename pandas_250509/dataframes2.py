import pandas as pd

data = {
    'Nombre': ['Ana', 'Luis', 'Sofía'],
    'Edad' : [28,34,22],
    'Ciudad': ['CDMX', 'Guadalajara', 'Monterrey']
}
#df = pd.DataFrame.from_dict(data, orient='index') # Presenta diferente la tabla
df = pd.DataFrame.from_dict(data, orient='columns')
print(df)

#print(df['Edad'])
print(df[['Nombre', 'Edad']]) 
print(df.loc[0]) # Accede a todos los datos de Ana vía NOMBRE fila
print(df.loc[0]) # Accede a todos los datos de Ana vía ÍNDICE fila

# IMpresion con condicion
print(df[df['Edad'] > 25]) # Imprime datos de personas mayores de 25

# Multiples condiciones
#print(df[])

df['Ocupación'] = ['Médico', 'Economista', 'Genómico']
print()