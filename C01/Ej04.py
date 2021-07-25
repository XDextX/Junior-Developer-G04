# Created by German Montero at 19/7/2021
def mostrar_respuesta_erronea(cadena: str):
    print(f"{cadena} no es un numero mayor a 0")


# Escribir un programa que lea un entero positivo,n, introducido por el usuario y
# después muestre en pantalla la suma de todos los enteros desde 1 hasta n.
if __name__ == '__main__':
    respuesta: str = ""
    numero: int = 0
    while numero <= 0:
        respuesta = input("Hasta que numero quiere contar?: ")
        if not respuesta.isdigit():
            mostrar_respuesta_erronea(respuesta)
        elif int(respuesta) <= 0:
            mostrar_respuesta_erronea(respuesta)
        else:
            numero = int(respuesta)
    else:
        print("contando...")
        for entero in range(numero):
            print(entero + 1)
