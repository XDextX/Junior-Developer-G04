# Created by German Montero at 25/7/2021
# Escribir un programa que pregunte al usuario su edad
# y muestre por pantalla todos los años que ha cumplido
# (desde 1 hasta su edad).
def preguntar_edad() -> int:
    res = input("ingrese su edad: ")
    if res.isdigit():
        return int(res)
    else:
        print("La edad debe ser un numero entero mayor a 0")
        return preguntar_edad()


def imprimir_edades():
    for i in range(1, preguntar_edad() + 1):
        print(i)


if __name__ == '__main__':
    imprimir_edades()
