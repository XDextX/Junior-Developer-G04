# Created by German Montero at 4/8/2021
def llenar() -> tuple[list[str], list[int]]:
    nombres: list[str] = []
    edades: list[int] = []
    tam = int(input("Ingrese la cantidad de registros: "))
    for i in range(tam):
        nombre = input("Dijite el nombre: ")
        edad = int(input("Dijite la edad: "))
        nombres.append(nombre)
        edades.append(edad)
    return nombres, edades


def imprimir(nombres: list[str], edades: list[int]):
    if len(nombres) == len(edades):
        for i in range(len(nombres)):
            print(f"Nombre: {nombres[i]},"
                  f"Edad: {edades[i]}")


def imprimir_mayores(nombres: list[str], edades: list[int]):
    for i in range(len(edades)):
        print("Personas mayores de edad: ")
        if edades[i] >= 18:
            print(nombres[i])


if __name__ == '__main__':
    nombres, edades = llenar()
    imprimir_mayores(nombres, edades)
