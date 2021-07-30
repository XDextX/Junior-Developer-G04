# Escribir un programa que almacene el abecedario
# en una lista,elimine de la lista las letras que
# ocupen posiciones múltiplos de 3, y muestre por
# pantalla la lista resultante.

def lista_alfabetica() -> list:
    lista: list = []
    for i in range(ord('a'), ord('z') + 1):
        lista.append(chr(i))
    return lista


def imprimir(lista: list):
    for i in lista:
        print(i, end=" ")
    print()


def remover_multiplos(multiplo: int, lista: list):
    for i in range(len(lista) - 1, 1, -1):
        if (i + 1) % multiplo == 0:
            lista.pop(i)
    return lista


if __name__ == '__main__':
    print("Alfabeto")
    alphabet = lista_alfabetica()
    imprimir(alphabet)
    multiplo = 3
    print(f"Alfabeto sin lentras que son multiplos de \"{multiplo}\"")
    new_alphabet = remover_multiplos(multiplo, alphabet)
    imprimir(new_alphabet)
