# Created by German Montero at 11/8/2021


import random


def main():
    lista = []
    # Generar números aleatorios entre 49999 y 99999
    for n in range(0, 50):
        lista.append(random.randint(49999, 99999))
    # Elegir un número al azar
    numero_al_azar = random.choice(lista)
    # Elegir 5 números al azar
    numeros_al_azar = random.sample(lista, 5)
    # reordenar los elementos de una lista
    mujeres = ["Ana", "Beatriz", "Camila", "Carmen", "Delia", "Dora", "Emilse"]
    random.shuffle(mujeres)


if __name__ == '__main__':
    main()
