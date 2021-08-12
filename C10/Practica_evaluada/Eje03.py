# Created by German Montero at 9/8/2021
# Diseña un programa que calcule la menor de cinco palabras dadas; es decir, la primera
# palabra de las cinco en orden alfabético. No aceptaremos que las mayúsculas sean
# “alfabéticamente” menores que las minúsculas. O sea, ’pepita’ es menor que ’Pepito’. No
# se puede utilizar sort. Valor 15 puntos
def lleno():
    cantidad = 5
    print(f"Ingresa {cantidad} palabras para encontrar cual es la primera segun el alfabeto.")
    palabras = []
    for i in range(cantidad):
        palabras.append(input(f"palabra #{i + 1}:> "))
    print("Gracias.")
    return palabras


def ordenar(lista: list[str]):
    for i in range(len(lista)):
        for j in range(1, len(lista)):
            if lista[j - 1] > lista[j]:
                _menor = lista[j]
                _mayor = lista[j - 1]
                lista[j - 1] = _menor
                lista[j] = _mayor
    return lista


def mostrar_menor_palabra(lista: list):
    if len(lista) > 0:
        print(f"{lista[0]} es la menor de las palabras ingresadas")


def main():
    palabras = lleno()
    ordenar(palabras)
    mostrar_menor_palabra(palabras)


if __name__ == '__main__':
    main()
