# Created by German Montero at 27/7/2021
def lleno() -> list:
    lista = []
    tam: int = int(input("Ingrese el tamaño de su lista"))
    for i in range(tam):
        element = int(input("Digite un numero: "))
        lista.append(element)
    return lista


def imprimo(lista: list):
    for i in range(len(lista)):
        print(lista[i], end=" ")


if __name__ == '__main__':
    imprimo(lleno())
