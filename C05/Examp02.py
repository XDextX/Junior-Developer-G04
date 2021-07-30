# Created by German Montero at 28/7/2021
def imprimo(nums):
    for x in range(len(nums)):
        print(nums[x], end=" ")
    print()


def get_dato(msj="") -> int:
    if msj == "":
        msj = "Digite un numero entero: "
    res = input(msj)
    if res.isdigit():
        return int(res)
    else:
        print("El dato debe ser un numero entero")
        return get_dato()


def ordeno(lista: list):
    for y in range(len(lista)):
        for x in range(len(lista) - 1):
            if lista[x] > lista[x + 1]:
                aux = lista[x]
                lista[x] = lista[x + 1]
                lista[x + 1] = aux
        print("\nLista con la lista completamente ordenada")
        imprimo(lista)


def lleno(size: int):
    lista = []
    for x in range(size):
        valor = int(input("Ingrese sueldo:"))
        lista.append(valor)
    print("Lista sin ordenar")
    imprimo(lista)
    return lista


if __name__ == '__main__':
    lista_num = lleno(5)
    ordeno(lista_num)
