# Created by German Montero at 25/7/2021
# Escribir un programa que pida al usuario una palabra
# y la muestre por pantalla 10 veces
def get_data() -> str:
    res = input("Ingrese una palabra: ")
    return res


def imprimir_informacion(veces: int):
    for i in range(veces):
        print(get_data())


if __name__ == '__main__':
    imprimir_informacion(10)
