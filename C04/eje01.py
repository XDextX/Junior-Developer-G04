# Created by German Montero at 27/7/2021
# Definir una lista que almacene 5 enteros.
# Sumar todos sus  elementos y mostrar dicha suma

lista: list = [1, 23, 4, 5, 6]

if __name__ == '__main__':
    suma: int = 0
    for i in lista:
        suma += i
    print(suma)
