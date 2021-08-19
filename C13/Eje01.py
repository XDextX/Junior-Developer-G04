# Created by German Montero at 16/8/2021
# Realice una función recursiva que realice el retorno de un número dado
# hasta llegar a cero, la función se debe de llamar cuenta regresiva y recibe
# el número entero por parámetro
def cuenta_regresiva(numero: int):
    if numero > 1:
        print(numero - 1)
        cuenta_regresiva(numero - 1)
    else:
        print("Boooooooom!")


if __name__ == '__main__':
    cuenta_regresiva(5)
