import pandas as pd

genes = {
    'GeneID': ['b0001', 'b0002', 'b0003'],
    'NOmbre' : ['thrL', 'thrA', 'thrB'],
    'Función' : ['regulador', 'enzima' , 'enzima'],
    'Longitud': [117, 2340, 1461]
}
df_genes = pd.DataFrame(genes)
print(df_genes)

# Imprimir genes con longitud mayor a 1000 y que sean enzimas (doble condición)
print(df_genes[(df_genes['Función'] == 'enzima') & (df_genes['Longitud'] > 1000)])

# Imprimir genes con longitud mayor a 1000, nombre y función. Vía filas
print(df_genes.loc[df_genes['Longitud'] > 1000, ['GeneID', 'Función']])

# COmprension de listas 
print(df_genes.iloc[1:2])