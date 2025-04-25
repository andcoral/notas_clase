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
resultado = at_content("GCAAATGACCGCATATCGATGATCGATTA", 1)
print(resultado)

at_content(dna = "atcagtacgtaaatgtccatgg", sig_figs = 2)
print(resultado)