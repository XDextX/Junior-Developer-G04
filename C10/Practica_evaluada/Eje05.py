# Created by German Montero at 9/8/2021
# Realizar un programa que determine cual es el mayor de tres numeros diferentes. Valor 10
# puntos
def pedir_dijito(msj: str = ""):
    res = input(msj)
    if res.isdigit():
        return int(res)
    else:
        print("El dato ingresado debe ser un numero entero.")
        return pedir_dijito(msj)


def llenar(cantidad=3):
    numeros: list[int] = []
    print(f"Ingrese {cantidad} numeros a continuacion.")
    for i in range(cantidad):
        numeros.append(pedir_dijito(f"Ingrese el numero {i + 1}: "))
    return numeros


def ordenar(lista: list[int]):
    for i in range(len(lista)):
        for j in range(1, len(lista)):
            if lista[j - 1] > lista[j]:
                _menor = lista[j]
                _mayor = lista[j - 1]
                lista[j - 1] = _menor
                lista[j] = _mayor
    return lista


def mostrar_mayor_numero(lista: list):
    if len(lista) > 0:
        print(f"{lista[-1]} es la mayor de los numeros ingresados")


def main():
    lista = llenar()
    mostrar_mayor_numero(ordenar(lista))


if __name__ == '__main__':
    main()
