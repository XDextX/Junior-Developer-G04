# Created by German Montero at 23/7/2021
def retornar_superficie(lado):
    sup = lado ** 2
    return sup


if __name__ == '__main__':
    va = int(input("ingrese el valor del lado del cuadrado"))
    superficie = retornar_superficie(va)
