# SEXTO EJERCICIO

# Definicion de funcion
def at_content(dna, sig_figs):
    dna = dna.upper()
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, sig_figs)

# Llamados de funcion
# Solo se vale en pasos de parametros combinados primero orden y despues por nombre, lo contrario da error.
resultado = at_content("GCAAATGACCGCATATCGATGATCGATTA", sig_figs= 1) 
print(resultado)

at_content(dna = "atcagtacgtaaatgtccatgg", sig_figs = 2)
print(resultado)