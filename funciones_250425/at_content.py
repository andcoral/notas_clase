# TERCER EJERCICIO

# Definicion de funcion
def at_content(dna):
    dna = dna.upper()
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    print(at_content)

# Llamados de funcion
at_content("GCAAATGACCGCATATCGATGATCGATTA")
at_content("atcagtacgtaaatgtccatgg")