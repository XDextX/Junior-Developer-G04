# Created by German Montero at 25/7/2021
# Escribir un programa que pida al usuario
# un número entero positivo y muestre por
# pantalla la cuenta atrás desde ese número
# hasta cero separados por comas.

def obtener_numero() -> int:
    res = input("ingrese un numero: ")
    if res.isdigit():
        return int(res)
    else:
        print("Debe ingresar un numero mayor a 0")
        return obtener_numero()


def cuenta_regresiva(num):
    cadena: str = ""
    for i in range(num, 0, -1):
        cadena += f"{i},"
    cadena = cadena[:len(cadena) - 1]
    print(cadena)


if __name__ == '__main__':
    cuenta_regresiva(obtener_numero())
