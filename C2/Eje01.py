# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
def verficar_eddad():
    res: str = input("Cual es su edad: ")
    edad: int = 0
    if res.isdigit():
        edad = int(res)

    if edad >= 18:
        print("Mayor de edad.")
    else:
        print("Menor de edad")


if __name__ == '__main__':
    print("Dijite sub edad para saber si corresponde a un mayor de edad")
    verficar_eddad()
    