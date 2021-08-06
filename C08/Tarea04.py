# Escribe una función "ordenada" que tome una lista como parámetro y devuelva True si la lista está ordenada en
# orden ascendente y devuelva False en caso contrario.
# Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada([b, a]) retorna False

def ordenada(lista: list) -> bool:
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


def imprimir(lista: list):
    s = "La lista: "
    for i in lista:
        s += f"{i},"
    print(s[0:len(s) - 1])


if __name__ == '__main__':
    lista_desordenada = ["clara", "maria", "fer"]
    lista_ordenada = [1, 2, 3, 4, 5]
    imprimir(lista_ordenada)
    print("está ordenada?")
    print(ordenada(lista_ordenada))
    imprimir(lista_desordenada)
    print("está ordenada?")
    print(ordenada(lista_desordenada))
