# Escribir un programa que pregunte al usuario los números
# ganadores de la lotería primitiva,los almacene en una lista
# y los muestre por pantalla ordenados de menor a mayor.

def get_entero():
    res = input("ingrese un numero entero:>_ ")

    if res.isdigit():
        return int(res)
    else:
        print("Debe ingresar un numero entero.")
        return get_entero()


def llenar_lista(size: int):
    lista = []
    for i in range(size):
        lista.append(get_entero())

    return lista


def imprimir(lista: list):
    for i in lista:
        print(i, end=" ")
    print()


def ordenar(lista: list):
    for j in range(1, len(lista)):
        for i in range(1, len(lista)):
            if lista[i - 1] > lista[i]:
                mayor = lista[i - 1]
                lista[i - 1] = lista[i]
                lista[i] = mayor
    return lista


if __name__ == '__main__':
    print("Ingrese la cantidad de numeros ganadores")
    size = get_entero()
    print("Ingrese los numeros ganadores de la loteria.")
    lista = llenar_lista(size)
    lista_ordenada = ordenar(lista)
    print("Los nmumeros gandores son:")
    imprimir(lista_ordenada)
