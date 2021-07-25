# Created by German Montero at 25/7/2021
# Escribir un programa que pida al usuario
# un número entero positivo y muestre por
# pantalla todos los números impares desde 1
# hasta ese número separados por comas.
def obtener_numero() -> int:
    res = input("ingrese un numero: ")
    if res.isdigit():
        return int(res)
    else:
        print("Debe ingresar un numero mayor a 0")
        return obtener_numero()


def imprimir_impares():
    cadena = ""
    for i in range(1, obtener_numero() + 1, 2):
        cadena += f"{i},"
    cadena = cadena[:len(cadena) - 1]
    print(cadena)


if __name__ == '__main__':
    imprimir_impares()
