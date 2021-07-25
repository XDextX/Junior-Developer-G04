# Created by German Montero at 19/7/2021
def obtener_nombre() -> str:
    return input("Dijite el nombre su nombre")


def obtener_numero() -> int:
    respuesta = input("Dijite su numero favorito: ")
    if respuesta.isdigit():
        return int(respuesta)
    else:
        return 0


def verificar_informacion():
    global numero
    while numero <= 0:
        print("tu numero debe ser mayor a 0: ")
        numero = obtener_numero()
    else:
        for loop in range(numero):
            print(nombre)


# Escribir un programa que pregunte el nombre del usuario en la consola y un número
# entero e imprima por pantalla en líneas distintas el nombre del usuario tantas
# veces como el número introducido.
if __name__ == '__main__':
    """Inicio del programa"""
    nombre: str = obtener_nombre()
    numero: int = obtener_numero()
    verificar_informacion()
