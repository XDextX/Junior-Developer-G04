# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el
# de más abajo, de altura el número introducido.
def obtener_numero() -> int:
    res = input("ingrese un numero: ")
    if res.isdigit():
        return int(res)
    else:
        print("Debe ingresar un numero mayor a 0")
        return obtener_numero()


def generar_triangulo(base: int):
    for i in range(1, base + 1):
        print("*" * i)


if __name__ == '__main__':
    generar_triangulo(obtener_numero())
