# Created by German Montero at 27/7/2021
# Cuando el programa inicia, se le solicita al
# usuario almacenar números enteros en una lista,
# no se sabe cuantos números se ingresan
# a la lista, solo sabemos que cuando se ingresa
# el cero “0”, se termina la carga de la lista,
# se procede a imprimir la lista completa
# y dar el tamaño de la lista.
# (El cero no se agrega en la lista).
def get_dato():
    dato: str = input("Ingrese un numero entero: ")
    if dato.isdigit():
        return int(dato)
    else:
        print("Debe ingresar un numero entero")
        return get_dato()


def make_list():
    lista_enteros = []
    dato = 1
    while dato != 0:
        dato = get_dato()
        if dato != 0:
            lista_enteros.append(dato)
    return lista_enteros


if __name__ == '__main__':
    print(make_list())
