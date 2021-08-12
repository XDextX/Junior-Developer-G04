# Created by German Montero at 12/8/2021
# Construya un algoritmo que sume dos matrices
# de igual dimensión y guarde el resultado en una tercera matriz.
# Imprima las 3 matrices. Solicitar el tamaño
# de la matriz al iniciar y llenarlo de manera random.
import random


def suma(m1: list[list], m2: list[list]):
    resultado = []
    for fila in range(len(m1)):
        resultado.append([])
        for col in range(len(m1[fila])):
            resultado[fila].append(m1[fila][col] + m2[fila][col])
    return resultado


def imprimir(m1: list[list], m2: list[list]):
    s = ""
    for fila in range(len(m1)):
        f1 = ""
        f2 = ""
        for col in range(len(m1[fila])):
            f1 += f"\t{m1[fila][col]}"
            f2 += f"\t{m2[fila][col]}"
        s += f"{f1}\t{f2}\n"
    print(s)


def imprimir_single(mat: list[list]):
    s = ""
    for fila in range(len(mat)):
        for col in range(len(mat[fila])):
            s += f"\t{mat[fila][col]}"
        s += "\n"
    print(s)


def obtener_matriz(filas: int, columnas: int):
    mat = []
    for f in range(filas):
        mat.append([])
        for col in range(columnas):
            mat[f].append(random.randint(1, filas * columnas))
    return mat


def main():
    filas = int(input("Dijite el numero de filas: "))
    columnas = int(input("Dijite el numero de columnas: "))
    m1 = obtener_matriz(filas, columnas)
    m2 = obtener_matriz(filas, columnas)
    # m1 = obtener_matriz(5, 8)
    # m2 = obtener_matriz(5, 8)
    print("El resultado de sumar las matrices: ")
    imprimir(m1, m2)
    print("Es: ")
    imprimir_single(suma(m1, m2))


if __name__ == '__main__':
    main()
