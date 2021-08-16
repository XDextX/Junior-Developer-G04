# Crea una tupla con valores ya predefinidos del 1 al 10,
# pide un índice por teclado y muestra los valores de la tupla.
def tuplis():
    return 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


def pedir_indice():
    indice = int(input("Ingrese un indice del 0 al 9: "))
    t = tuplis()
    ind = -1
    for i in range(len(t)):
        if i == indice:
            ind = t[i]
            return ind
    return ind, indice


def main():
    contenido, indice = pedir_indice()
    if contenido != -1:
        print(f"El contenido del indice {indice} es {contenido}")
    else:
        print("El indice no es valido")


if __name__ == '__main__':
    main()
