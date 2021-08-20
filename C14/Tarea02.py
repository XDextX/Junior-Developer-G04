# Escribir una clase en python con 2 métodos: get_string y print_string. get_string acepta una
# cadena ingresada por el usuario y print_string imprime la cadena en mayúsculas.


class Griton:
    cadena: str

    def __init__(self, cadena: str = ""):
        self.cadena = cadena

    def get_string(self, cadena):
        self.cadena = cadena

    def print_string(self):
        print(self.cadena.upper())


def main():
    grito = Griton()
    grito.get_string(input("Que desea gritar:>_ "))
    grito.print_string()


if __name__ == '__main__':
    main()
