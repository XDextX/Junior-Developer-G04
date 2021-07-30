# Realizar un programa que pida la carga de dos listas numéricas enteras de 5 elementos cada una.
# Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista.
# Imprimir las 3 listas.

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


def sumar_vectores(vector1: list, vector2: list):
    resultado = []
    for i in range(len(vector1)):
        resultado.append(vector1[i] + vector2[i])
    return resultado


if __name__ == '__main__':
    print("Ingrese un tamaño para las listas")
    size = get_entero()
    print("Llenado de la lista de enteros 1.")
    enteros1 = llenar_lista(size)
    print("Llenado de la lista de enteros 1.")
    enteros2 = llenar_lista(size)
    enteros3 = sumar_vectores(enteros1, enteros2)
    print("Lista de entero 1.")
    imprimir(enteros1)
    print("Lista de entero 2.")
    imprimir(enteros2)
    print("resultado de la suma de ambas listas.")
    imprimir(enteros3)
