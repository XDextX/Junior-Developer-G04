# Escribir un programa que pida al usuario un número entero
# y muestre por pantalla un triángulo rectángulo como el de más abajo.
def obtener_numero() -> int:
    res = input("ingrese un numero: ")
    if res.isdigit():
        return int(res)
    else:
        print("Debe ingresar un numero mayor a 0")
        return obtener_numero()


def desplegar_triangulo(base: int):
    for i in range(1, base + 1, 2):
        print(impares(i))


def impares(number):
    cadena = ""
    for i in range(number, 0, - 2):
        cadena += f" {i}"
    return cadena


if __name__ == '__main__':
    desplegar_triangulo(obtener_numero())
