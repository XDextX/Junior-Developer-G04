# Created by German Montero at 4/8/2021
# Confeccionar un programa que permita cargar los nombres de “x” alumnos y sus
# notas respectivas. Luego ordenar las notas de mayor a menor. Imprimir las notas y
# los nombres de los alumnos.
# Debe quedar claro que cuando intercambiamos las notas para dejarlas ordenadas
# de mayor a menor debemos intercambiar los nombres para que las listas
# continúen paralelas (es decir que en los mismos subíndices de cada lista continúe la
# información relacionada

def llenar() -> tuple[list[str], list[int]]:
    nombres: list[str] = []
    notas: list[int] = []
    tam = int(input("Ingrese la cantidad de registros: "))
    for i in range(tam):
        nombre = input("Dijite el nombre: ")
        nota = int(input("Dijite la nota: "))
        nombres.append(nombre)
        notas.append(nota)
    return nombres, notas


def imprimir(nombres: list[str], notas: list[int]):
    if len(nombres) == len(notas):
        for i in range(len(nombres)):
            print(f"Nombre: {nombres[i]} | "
                  f"nota: {notas[i]}")


def ordenar(nombres: list[str], notas: list[int]):
    for _ in range(len(notas)):
        for i in range(1, len(notas)):
            if notas[i - 1] < notas[i]:
                _nombre = nombres[i]
                _nota = notas[i]
                # intercabio en la lista de nombres
                nombres[i] = nombres[i - 1]
                nombres[i - 1] = _nombre
                # intercambio en la lista de notas
                notas[i] = notas[i - 1]
                notas[i - 1] = _nota
    return nombres, notas


if __name__ == '__main__':
    nombres, notas = llenar()
    print("Datos ingresados: ")
    imprimir(nombres, notas)
    ordenar(nombres, notas)
    print("Datos según la nota mayor: ")
    imprimir(nombres, notas)
