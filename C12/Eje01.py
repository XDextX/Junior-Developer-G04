# Created by German Montero at 13/8/2021
#
import random


def obtener_matriz(filas: int, columnas: int):
    mat = []
    for f in range(filas):
        mat.append([])
        for col in range(columnas):
            mat[f].append(random.randint(0, filas * columnas))
    return mat


def imprimir_single(mat: list[list]):
    s = ""
    for fila in range(len(mat)):
        for col in range(len(mat[fila])):
            s += f"\t{mat[fila][col]}"
        s += "\n"
    print(s)


def sumar_diagonal(mat: list[list]):
    sumatoria = 0
    tam = len(mat)
    for i in range(tam):
        sumatoria += mat[i][tam - 1 - i]
    return sumatoria


def main():
    tam = 3
    math = obtener_matriz(tam, tam)
    print("la suma de la diagonal inversa de la matriz: ")
    imprimir_single(math)
    print(f"Es: {sumar_diagonal(math)}")


if __name__ == '__main__':
    main()
