# Created by German Montero at 19/7/2021
def operar():
    return ((3 + 2) / (2 - 5)) ** 2


# Escribir un programa que realice la siguiente operación aritmética.
# ((3+2)/(2-5))**2
if __name__ == '__main__':
    print("Realizando operacion...")
    operacion: float = operar()
    print(f"El resultado fue:{operacion}")
