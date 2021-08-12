# Created by German Montero at 12/8/2021
# Construya un algoritmo que determine cuantos
# elementos pares y cuantos impares hay en una matriz y cuantos de
# ellos son cero. Solicitar el tamaño de la
# matriz al iniciar y llenarlo de manera random
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


def contar_impares_pares_y_cero(mat: list[list[int]]):
    pares = 0
    impares = 0
    cero = 0
    for fila in range(len(mat)):
        for col in range(len(mat[fila])):
            if mat[fila][col] == 0:
                cero += 1
            elif mat[fila][col] % 2:
                pares += 1
            else:
                impares += 1
    return impares, pares, cero


def main():
    filas = int(input("Dijite la cantidad de filas: "))
    columnas = int(input("Dijite la cantidad de columnas: "))
    mat = obtener_matriz(filas, columnas)
    impares, pares, cer = contar_impares_pares_y_cero(mat)
    print("En la matriz: ")
    imprimir_single(mat)
    print("Se encuentran:\n"
          f"{impares} impares,"
          f" {pares} pares y"
          f" {cer} ceros")


if __name__ == '__main__':
    main()
