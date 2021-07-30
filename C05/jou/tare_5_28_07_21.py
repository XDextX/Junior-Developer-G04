def palabra():
    word = input("Ingrese una palabra:> ")
    return word

def palindromo(poli):
    alreves =""
    for i in range(len(poli) -1, -1, -1):
         alreves += poli [i]
    if (alreves == poli):
        print("La palabra ", poli, "es un palindromo")
    else:
        print("La palabra ", poli, " no es un palindromo")


if __name__ == '__main__':
    palindromo(palabra())
