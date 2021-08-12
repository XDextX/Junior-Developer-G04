# Created by German Montero at 11/8/2021
# Crear una lista por asignación. La lista tiene que tener
# cuatro elementos. Cada elemento debe ser una lista de 3
# enteros. Imprimir sus elementos con formato de matriz.

def imprimir_matriz(matriz: list[list]):
    format = ""
    for f in range(len(matriz)):
        format += "\n\t"
        for col in range(len(matriz[f])):
            format += f"{matriz[f][col]} "
        format += ""
    format += ""
    print(format)


def main():
    mat = [[1, 2], [2, 3]]
    imprimir_matriz(mat)


if __name__ == '__main__':
    main()
