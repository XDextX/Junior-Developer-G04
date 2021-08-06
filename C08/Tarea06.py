# Realizar un programa que permita crear una lista y almacenar los nombres de n países. Ordenar alfabéticamente la
# lista e imprimirla
def llenar():
    lista: list = []
    tam = int(input("Ingrese la cantidad de paises que desea ingreasar: "))
    for i in range(tam):
        pais = input("Dijite el pais: ")
        lista.append(pais)
    return lista


def ordenar(lista: list):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            _elem = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = _elem
    return lista


def imprimir(lista: list):
    s = ""
    for i in lista:
        s += f"{i},"
    print(s[0:len(s) - 1])


if __name__ == '__main__':
    paises = llenar()
    print("La lista de paises: ")
    imprimir(paises)
    print("Se ordena de forma alfabetica como: ")
    imprimir(ordenar(paises))
