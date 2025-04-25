# CUARTO EJERCICIO

# Definicion de funcion
def count_bases(dna):
    bases = "ATGC"
    for base in bases:
        numbases = dna.upper().count(base)
        print(f"{base} {numbases}")

# Llamado de funcion
count_bases("GTACAGTTTAGGCATTGTTATGAC")