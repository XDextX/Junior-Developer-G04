# Escribir una clase en python que revierta una cadena de palabras
# Entrada: "Mi Diario Python"
# Salida: "Python Diario Mi”
class Inversor:

    def __init__(self, cadena=""):
        self.cadena = cadena

    def invertir(self):
        cadena_invertida = ""
        palabra = ""
        for letra in self.cadena:
            palabra += letra
            if letra == " ":
                cadena_invertida = palabra + cadena_invertida
                palabra = ""
        cadena_invertida = palabra + " " + cadena_invertida
        print(cadena_invertida)


def main():
    frase = input("Ingrese una frase que desee invertir:>_ ")
    i = Inversor(frase)
    i.invertir()


if __name__ == '__main__':
    main()
