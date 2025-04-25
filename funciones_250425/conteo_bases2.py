# QUINTO EJERCICIO

# Definicion de funcion
def count_bases(dna, sig_figs):
    dna = dna.upper()
    conteo = {
        'A': dna.count('A'),
        'T': dna.count('T'),
        'G': dna.count('G'),
        'C': dna.count('C'),                       
    }

    return conteo

dna = " ATGCATTTACGTTTAAGCATTCA"
resultado = count_bases