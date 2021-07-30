# Created by German Montero at 28/7/2021
# Creary  cargar una lista con 5  enteros.
# Implementar un algoritmo que identifique el
# mayor valor de la lista.
def lleno(cantidad: int):
    lista = []
    for x in range(cantidad):
        valor = int(input("Ingrese valor:"))
        lista.append(valor)
    return lista


def imprimo(nums: list):
    for x in range(len(nums)):
        print(nums[x], end=" ")


def mayor(lista: list):
    may = lista[0]
    for x in range(1, 5):
        if lista[x] > may:
            may = lista[x]
    print("\nMayor de la lista", may)


def get_dato() -> int:
    res = input("Digite un numero entero: ")
    if res.isdigit():
        return int(res)
    else:
        print("El dato debe ser un numero entero")
        return get_dato()


if __name__ == '__main__':
    lista_numeros = lleno(get_dato())
    imprimo(lista_numeros)
    mayor(lista_numeros)
