# Solicitar al usuario que ingrese números, los cuales se guardarán
# en una lista. Finalizar al ingresar el número 0, el cual no debe
# guardarse.
#   •A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista,
#    eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
#   •Recorrer la lista para imprimir la sumatoria de todos los elementos.
#   •Solicitar al usuario otro número y crear una lista con los elementos de la lista
#    original que sean menores que el número dado. Imprimir esta nueva lista,
#    iterando por ella.
#   •Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos,
#    cada una compuesta por un número de la lista original y la cantidad de veces que aparece
#    en ella.
#     Por ejemplo, si la lista original# es [5,16,2,5,57,5,2]
#     la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]
import random


def llenar():
    lista = []
    seguir = True
    while seguir:
        dato = int(input("Ingrese cualquier numero entero: "))
        #dato = random.randint(0, 20)
        if dato != 0:
            lista.append(dato)
        else:
            seguir = False
    return lista


def eliminar(lista: list):
    dato = int(input("Ingrese un numero para eliminar de la lista: "))
    for i in range(len(lista)):
        if lista[i] == dato:
            lista.pop(i)
            return i
    return -1


def sumatoria(lista: list):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma


def corte(lista: list):
    limite = int(input("Ingrese el un numero para marcar un corte superior"))
    lista_cortada = []
    for i in range(len(lista)):
        if lista[i] < limite:
            lista_cortada.append(lista[i])
    return lista_cortada, limite


def imprimir_single(mat: list):
    s = ""
    for fila in range(len(mat)):
        s += f"\t{mat[fila]}"
    s += "\n"
    print(s)


def contar_ocurrencias(lista: list):
    unicos = []
    for i in range(len(lista)):
        unico = True
        for j in range(len(unicos)):
            if lista[i] == unicos[j]:
                unico = False
        if unico:
            unicos.append(lista[i])
    coincidencias = []
    for x in range(len(unicos)):
        contador = 0
        for y in range(len(lista)):
            if unicos[x] == lista[y]:
                contador += 1
        coincidencias.append((unicos[x], contador))
    return coincidencias


def imprimir_lista_tupla(lista: list[tuple]):
    s = ""
    for i in range(len(lista)):
        s += "\t(\t"
        for j in range(len(lista[i])):
            s += f"{lista[i][j]}\t"
        s += ")\n"
    print(s)


if __name__ == '__main__':
    lista = llenar()
    imprimir_single(lista)
    eliminacion = eliminar(lista)
    if eliminacion == -1:
        print("No es posible eliminar")
    suma = sumatoria(lista)
    print(f"La suma de todos los elementos de la lista ")
    imprimir_single(lista)
    print(f"Es es {suma}")
    filtro, limite = corte(lista)
    print(f"Los elementos menores a {limite} son: ")
    imprimir_single(filtro)
    print("La cantidad por cada elemento dentro de ")
    imprimir_single(lista)
    print("Es")
    imprimir_lista_tupla(contar_ocurrencias(lista))
