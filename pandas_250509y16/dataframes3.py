import pandas as pd

genes = {
    'GeneID': ['b0001', 'b0002', 'b0003'],
    'Nombre' : ['thrL', 'thrA', 'thrB'],
    'Función' : ['regulador', 'enzima' , 'enzima'],
    'Longitud': [117, 2340, 1461]
}

df_genes = pd.DataFrame(genes) # Vuelve al diccionario un DataFrame
print(df_genes)

# Imprimir genes con longitud mayor a 1000 y que sean enzimas (doble condición)
print(df_genes[(df_genes['Función'] == 'enzima') & (df_genes['Longitud'] > 1000)])

# Imprime solo el ID del gen que cumpla con las condiciones pasadas
print(df_genes[(df_genes['Función'] == 'enzima') & (df_genes['Longitud'] > 1000)]['GeneID'])
# Se hizo un filtrado (condiciones) y además se extrajo informacion (GeneID)

# Imprimir GeneID y FUnción de genes con longitud mayor a 1000. Acceso vía fila y mostrar columnas
print(df_genes.loc[df_genes['Longitud'] > 1000, ['GeneID', 'Función']]) # loc accede por labels

# Equivalente a lo de arriba, pero con uso de loc
#print(df_genes.iloc[df_genes[4] > 1000, [0, 2]]) # ni idea q queria q pasara aki

# Imprimir a partir de slicing
print(df_genes.iloc[:2, :1]) # Primeros dos renglones, solo una columna

print(df_genes.iloc[:2]) # Primeros dos renglones, todas las columnas

# Imprimir una sola columna
print(df_genes['GeneID']) # Imprime solo los valores de esa columna

# Crear columna con valores TRUE solo para los que cumplan condiciones
df_genes['Es_largo'] = df_genes['Longitud'] > 1000
print(df_genes)