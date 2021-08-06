# Pide una cadena por teclado, mete los caracteres en una lista sin espacios.
def cortar_espacios(frase: str):
    cadena = ""
    for i in frase:
        if i != " ":
            cadena += i
    return cadena


if __name__ == '__main__':
    frase_original = input("Dijite una frase: ")
    print(cortar_espacios(frase_original))
