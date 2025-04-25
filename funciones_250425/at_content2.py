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

# Llamados de funcion y testing
assert at_content("ATGC", 1) == 0.5
# Casos en que falla:
assert at_content("ATGCNNNNN", 1) == 0.5
assert at_content("", 1) == 0.5
assert at_content("ATGC", -1) == 0.5