import pandas as pd # importando libreria con alias

s = pd.Series([10, 20, 30], index =['a', 'b', 'c']) # pd.Series constructor de la clase Series en pandas
print(s)

data = {
    'Gene': ['thrL', 'thrA', 'thrB'],
    'Longitud': [117, 2340, 1461]
}
#df = pd.DataFrame(data)  # Interpreta automaticamente q es un diccionario y ajusta parámetros automáticamente.
df = pd.DataFrame.from_dict(data)
print(df.loc[0, 'Gene']) # .loc para acceder con nombres, no solo índices