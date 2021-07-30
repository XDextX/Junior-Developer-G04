# Created by German Montero at 28/7/2021
# Crear y cargar una lista con “x” enteros por teclado.
# Implementar un algoritmo que identifique el menor valor
# de la lista y la posición donde se encuentra.

def get_dato(msj="") -> int:
    if msj == "":
        msj = "Digite un numero entero: "
    res = input(msj)
    if res.isdigit():
        return int(res)
    else:
        print("El dato debe ser un numero entero")
        return get_dato()


def imprimo(nums: list):
    for x in range(len(nums)):
        print(nums[x], end=" ")
    print()


def llenar(size: int):
    lista = []
    for x in range(size):
        lista.append(get_dato())
    return lista


def menor(lista: list):
    men = lista[0]
    pos = 0
    for x in range(len(lista)):
        if lista[x] < men:
            men = lista[x]
            pos = x
    print(f"El menor de la lista es {men}\n"
          f"y su posiscion es {pos}")


if __name__ == '__main__':
    lista_numeros = llenar(get_dato("Dijite el tamaño de la lista: "))
    imprimo(lista_numeros)
    menor(lista_numeros)
