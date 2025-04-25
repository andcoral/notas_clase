# SEXTO EJERCICIO

# Definicion de funcion
def at_content(dna, sig_figs):
    """
    Calcula el contenido AT de una secuencia de ADN,
    redondeando a un número específico de cifras decimales.
    Parámetros:
    dna (str): Secuencia de ADN (ej. 'ATGCGC')
    sig_figs (int, opcional): número de cifras decimales (por defecto = 2)
    Retorna:
    float: contenido AT redondeado
    """
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