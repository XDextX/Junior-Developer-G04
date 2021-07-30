# Ingresar por teclado los nombres de ”x” personas
# y almacenar los en una lista. Mostrar el nombre
# de la persona menor en orden alfabético.
def get_entero():
    res = input("ingrese un numero entero:>_ ")

    if res.isdigit():
        return int(res)
    else:
        print("Debe ingresar un numero entero.")
        return get_entero()


def get_dato():
    return input("ingrese un nombre:>_ ")


def llenar_lista(size: int):
    lista = []
    for i in range(size):
        lista.append(get_dato())

    return lista


def imprimir(lista: list):
    for i in lista:
        print(i, end=" ")
    print()

def ordenar(lista: list) -> list:
    stop = len(lista)
    for j in range(stop):
        for i in range(1, stop):
            if lista[i - 1] > lista[i]:
                mayor = lista[i - 1]
                lista[i - 1] = lista[i]
                lista[i] = mayor
    return lista


if __name__ == '__main__':
    lista = (llenar_lista(get_entero()))
    print("Lista original:")
    imprimir(lista)
    print("lista ordenada")
    ordenar(lista)
    imprimir(lista)
    print(f"El menor de la lista es {lista[0]}")
