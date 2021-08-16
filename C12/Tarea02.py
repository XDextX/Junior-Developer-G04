# Created by German Montero at 13/8/2021
# Crea una tupla con números, pide un numero
# por teclado e indica cuantas veces se repite.

def tuplis():
    return 1, 23, 3, 5, 6, 2, 3, 1


def contar(data: int, tup: tuple):
    contador = 0
    for i in range(len(tup)):
        if data == tup[i]:
            contador += 1
    return contador


def imprimir_single(mat: list[list]):
    s = ""
    for fila in range(len(mat)):
        s += f"\t{mat[fila]}"
    s += "\n"
    print(s)


def main():
    t = tuplis()
    imprimir_single(t)
    data = int(input("Ingrese un numero uno de los numeros anteriores: "))
    coincidencias = contar(data, t)
    print(f"El dato {data} se encontro {coincidencias} veces")


if __name__ == '__main__':
    main()
