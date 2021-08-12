# Created by German Montero at 12/8/2021
# Escribir una función que reciba dos matrices
# y devuelva el producto. Solicitar el tamaño
# de la matriz al iniciar y llenarlo
# de manera random.
import random


def producto(m1: list[list], m2: list[list]):
    resultado = 0
    for fila in range(len(m1)):
        for col in range(len(m1[fila])):
            resultado += m1[fila][col] * m2[fila][col]
    return resultado


def obtener_matriz(filas: int, columnas: int):
    mat = []
    for f in range(filas):
        mat.append([])
        for col in range(columnas):
            mat[f].append(random.randint(1, filas * columnas))
    return mat


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


def imprimir_single(mat: list[list]):
    s = ""
    for fila in range(len(mat)):
        for col in range(len(mat[fila])):
            s += f"\t{mat[fila][col]}"
        s += "\n"
    print(s)


def main():
    filas = int(input("Dijite el numero de filas: "))
    columnas = int(input("Dijite el numero de columnas: "))
    m1 = obtener_matriz(filas, columnas)
    m2 = obtener_matriz(filas, columnas)
    resutado = producto(m1, m2)
    print("El producto de las matrices: ")
    imprimir(m1, m2)
    print(f"Es: {resutado}")


if __name__ == '__main__':
    main()
