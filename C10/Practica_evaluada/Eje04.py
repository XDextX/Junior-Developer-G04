# Created by German Montero at 9/8/2021
# Diseña un programa que, dados dos números enteros, muestre por pantalla uno de estos
# mensajes: “El segundo es el cuadrado exacto del primero”, “El segundo es menor que el
# cuadrado del primero” o “El segundo es mayor que el cuadrado del primero”, dependiendo
# de la verificación de la condición correspondiente al significado de cada mensaje. Valor 15
# puntos

def pedir_dijito(msj: str = ""):
    res = input(msj)
    if res.isdigit():
        return int(res)
    else:
        print("El dato ingresado debe ser un numero entero.")
        return pedir_dijito(msj)


def obtener_datos():
    print("Ingrese 2 numeros enteros para compararlos")
    numero1 = pedir_dijito("Ingrese el primer número: ")
    numero2 = pedir_dijito("Ingrese el segundo número: ")
    return numero1, numero2


def comparacion(num1: int, num2: int):
    if num1 ** 2 == num2:
        print("El segundo es el cuadrado exacto del primero")
    elif num1 ** 2 > num2:
        print("El segundo es menor que el cuadrado del primero")
    else:
        print("El segundo es mayor que el cuadrado del primero")


def main():
    numero1, numero2 = obtener_datos()
    comparacion(numero1, numero2)


if __name__ == '__main__':
    main()
