# Created by German Montero at 12/8/2021
# Desarrolle una funcion que llene una matriz 3X4 de nombres, la imprima, luego solicite al usuario ingresar un nombre y
# buscar si dicho nombre se encuentra dentro de la matriz y dar la posición.

def obtener_matriz(filas: int, columnas: int):
    mat = []
    for f in range(filas):

        mat.append([])

        for col in range(columnas):
            mat[f].append(input("Dijiete un nombre: "))

    return mat


def imprimir_single(mat: list[list]):
    s = ""
    for fila in range(len(mat)):
        for col in range(len(mat[fila])):
            s += f"\t{mat[fila][col]}"
        s += "\n"
    print(s)


def buscar_posicion(elemento: str, mat: list[list[str]]):
    x = -1
    y = -1
    for fila in range(len(mat)):
        for col in range(len(mat[fila])):
            if mat[fila][col] == elemento:
                x = fila
                y = col

    return x, y


def verificar_existencia(elemento: str, mat: list[list[str]]):
    x, y = buscar_posicion(elemento, mat)
    if x == -1 or y == -1:
        print(f"El nombre {elemento} no se encuentra en la matriz")
    else:
        print(f"El nomre {elemento} se en cuentra en la fila {x + 1} y la columna {y + 1}")


def main():
    # mat = [
    #    ["julio",
    #     "marco",
    #     "milai",
    #     "maria"],
    #    ["jose",
    #     "carla",
    #     "milena",
    #     "julian"],
    #    ["clariza",
    #     "anastasia",
    #     "ana",
    #     "pedro"]
    # ]
    mat = obtener_matriz(3, 4)
    imprimir_single(mat)
    nombre = input("Dijite un nombre para buscar: ")
    verificar_existencia(nombre, mat)


if __name__ == '__main__':
    main()
