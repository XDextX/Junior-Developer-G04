# Escribe una función llamada "elimina" que tome una lista y elimine el primer y último elemento de la lista y cree una
# nueva lista con los elementos que no fueron eliminados.
# Luego escribe una función que se llame "media" que tome una lista y devuelva una nueva lista que contenga todos
# los elementos de la lista anterior menos el primero y el último.
def elimina(lista: list):
    _lista = []
    for i in range(1, len(lista) - 1):
        _lista.append(lista[i])
    return lista


def media(lista: list):
    _lista = []
    for i in range(1, len(lista) - 1):
        _lista.append(lista[i])
    return lista


def imprimir(lista: list):
    s = ""
    for i in lista:
        s += f"{i},"
    print(s[0:len(s) - 1])


if __name__ == '__main__':
    lista = ["a", "c", "ka"]
    imprimir(elimina(lista))
    imprimir(media(lista))
