# Crea una lista con números, pide un numero por teclado e indica cuantas veces se repite
def contar_numero(lista: list, numero):
    contemos = 0
    for i in range(len(lista)):
        if lista[i] == numero:
            contemos += 1
    return contemos


def imprimir(lista: list):
    s = ""
    for i in lista:
        s += f"{i},"
    print(s[0:len(s) - 1])


if __name__ == '__main__':
    lista = [1, 2, 3, 3, 44, 2, 5, 66, 2, 7, 3, 6, 4, 6, 37, 37, 13, 7, 23, 6, 3, 61, 3, 54, 6]
    imprimir(lista)
    numero = int(input("Dijite un numero para encontrar las coincidencias: "))
    cantidad = contar_numero(lista, numero)

    print(f"{numero} se repite en la lista {cantidad} veces.")
