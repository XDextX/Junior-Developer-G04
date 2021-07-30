# Escribir un programa que pida al usuario
# una palabra y muestre por pantalla si es un palíndromo.
def get_dato():
    return input("ingrese una palabra:>_ ")


def is_palindromo(original: str, reversa: str) -> bool:
    return original == reversa


def reverse_string(word: str) -> str:
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    return reversed_word


if __name__ == '__main__':
    print("Vamos a revisar si lo ingresos son palindromos.")
    parada = ""
    while parada != "salir":
        palabra = get_dato()
        if is_palindromo(palabra, reverse_string(palabra)):
            print(f"{palabra} es un palindromo")
        else:
            print(f"{palabra} no es un palindromo")
        parada = input("Ingrese \"salir\" para salir o la tecla enter para seguir.")
