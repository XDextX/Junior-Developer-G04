# Created by German Montero at 19/7/2021
def solicitar_peso() -> int:
    numero: int = 0
    while numero <= 0:
        respuesta = input("Dijites su peso: ")
        if respuesta.isdigit():
            if int(respuesta) > 0:
                numero = int(respuesta)
            else:
                print("El peso debe ser un numero mayor a 0.")
        else:
            print("El peso debe ser un numero mayor a 0.")

    return numero


def solicitar_estatura() -> int:
    numero: int = 0
    while numero <= 0:
        respuesta = input("Dijites su estatura: ")
        if respuesta.isdigit():
            if int(respuesta) > 0:
                numero = int(respuesta)
            else:
                print("La estatura debe ser un numero mayor a 0.")
        else:
            print("La estatura debe ser un numero mayor a 0.")

    return numero


# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
# calcule el índice de masa corporal y lo almacene en una variable, y muestre por
# pantalla la fraseTu índice de masa corporal es <imc>donde<imc>es el índice de masa
# corporal calculado redondeado con dos decimales.
if __name__ == '__main__':
    print("vamos a revisar su indice de masa corporal")
    peso: int = solicitar_peso()
    altura: int = solicitar_estatura()
    imc: float = peso / altura ** 2
    print(f"Su indice de masa corporal es de {imc :.2f}")
