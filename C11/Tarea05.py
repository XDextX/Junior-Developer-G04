# Created by German Montero at 12/8/2021
# Construya un algoritmo que sume la diagonal de una matriz
# (superior izquierda hasta inferior derecha). Solicitar el
# tamaño de la matriz al iniciar y llenarlo de manera random
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
    for i in range(len(mat)):
        sumatoria += mat[i][i]
    return sumatoria


def main():
    print("la suma de la diagonal en la matriz: ")
    matriz = obtener_matriz(3, 3)
    imprimir_single(matriz)
    print(f"Es {sumar_diagonal(matriz)}")


if __name__ == '__main__':
    main()
