# Realizar un programa que contenga una lista con 10 valores enteros. Informar de cuántos de ellos son superiores a
# 100
def sobre_la_medida(lista: list[int], medida: int):
    cont = 0
    for i in range(len(lista)):
        if lista[i] > medida:
            cont += 1
    return cont


def imprimir(lista: list):
    s = "La lista: "
    for i in lista:
        s += f"{i},"
    print(s[0:len(s) - 1])


if __name__ == '__main__':
    lista = [2, 1233, 49, 100, 56, 389, 89]
    imprimir(lista)
    print(f"Tiene {sobre_la_medida(lista, 100)} elementos superiores a 100.")
