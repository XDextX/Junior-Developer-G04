# Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.
def obtener_frase(prompt):
    res = input(prompt)
    return res


def contar_ocurrencia(frase: str, ocurrencia: str):
    print(ocurrencia, "se repite", frase.count(ocurrencia), "veces.")


if __name__ == '__main__':
    print("Vamos a contar cuantas veces se repite uhna letra en una frase")
    contar_ocurrencia(obtener_frase("Escriba una frace:>_ "), obtener_frase("Escriba una letra:>_ "))
