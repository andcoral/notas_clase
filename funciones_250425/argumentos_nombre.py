# OCTAVO EJERCICIO

def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre = "Ana")

mostrar_info(nombre = "Ana", edad = 18)