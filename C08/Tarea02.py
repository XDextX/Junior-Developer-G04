# Escribe una función llamada "elimina_duplicados" que tome una lista y devuelva una nueva lista con los elementos
# únicos de la lista original. No tienen porque estar en el mismo orden
def elimina_duplicados(lista: list):
    unicos = []
    for i in range(len(lista)):
        if lista[i] not in unicos:
            unicos.append(lista[i])
    return unicos


def imprimir(lista: list):
    s = ""
    for i in lista:
        s += f"{i},"
    print(s[0:len(s) - 1])


if __name__ == '__main__':
    duplicados = [3, 4, 7, 2, 3, 2, 4, 2, 5, 6, 7]
    print("Lista de duplicados: ", end="")
    imprimir(duplicados)
    print("Lista sin duplicados: ", end="")
    imprimir(elimina_duplicados(duplicados))
