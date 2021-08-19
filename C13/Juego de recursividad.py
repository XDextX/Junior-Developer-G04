# Created by German Montero at 16/8/2021
def juego(intentos=2):
    resp = input("¿De que color es el cielo?: ")
    if resp.lower() == "celeste":
        print("Gano")
    else:
        if intentos > 0:
            print("Intente de nuevo!!")
            juego(intentos - 1)
        else:
            print("Perdio")


if __name__ == '__main__':
    juego()
