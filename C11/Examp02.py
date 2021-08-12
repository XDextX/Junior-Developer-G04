# Created by German Montero at 11/8/2021
def llenar_matriz():
    matriz = []
    filas = int(input("Dijite la cantidad de filas: "))
    columnas = int(input("Dijite la cantidad de columnas: "))
    for f in range(filas):
        matriz.append([])
        for col in range(columnas):
            num = int(input("Dijite un valor: "))
            matriz[f].append(num)
    return matriz


def imprimir_matriz(matriz: list[list]):
    deco1 = "["
    deco2 = "]"
    _format = f"{deco1}"
    for f in range(len(matriz)):
        _format += f"\n {deco1} "
        for col in range(len(matriz[f])):
            _format += f"{matriz[f][col]} "
        _format += f"{deco2}"
    _format += f"\n{deco2}"
    print(_format)


if __name__ == '__main__':
    imprimir_matriz([[], []])
