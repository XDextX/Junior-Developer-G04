# Created by German Montero at 11/8/2021
# Escribir una función que reciba dos matrices y
# devuelva la suma. Solicitar el tamaño de la matriz
# al iniciar y llenarlo de manera random
import random


def obtener_matriz(filas: int, columnas: int):
    mat = []
    for f in range(filas):
        mat.append([])
        for col in range(columnas):
            mat[f].append(random.randint(1, filas * columnas))
    return mat


def sumar_matrices(m1: list[list], m2: list[list]):
    suma = 0
    for fila in range(len(m1)):
        for col in range(len(m1[fila])):
            suma += m1[fila][col] + m2[fila][col]
    return suma


def imprimir(m1: list[list], m2: list[list]):
    s = ""
    for fila in range(len(m1)):
        f1 = ""
        f2 = ""
        for col in range(len(m1[fila])):
            f1 += f"{m1[fila][col]} "
            f2 += f"{m2[fila][col]} "
        s += f"\t{f1}\t{f2}\n"
    print(s)


def main():
    filas = int(input("Dijite el numero de filas: "))
    columnas = int(input("Dijite el numero de columnas: "))
    m1 = obtener_matriz(filas, columnas)
    m2 = obtener_matriz(filas, columnas)
    print("De la suma de las matrices: ")
    imprimir(m1, m2)
    print(f"se obtiene: {sumar_matrices(m1, m2)}")


if __name__ == '__main__':
    main()
