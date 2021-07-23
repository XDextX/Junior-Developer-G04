# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

def verificaion_pares():
    num = 0
    s_num = input("Ingrese un numero entero")
    if s_num.isdigit():
        num = int(s_num)
    else:
        return "Debe de ingresar un numero entero"
    if num % 2 == 0:
        return "El numero es par"
    else:
        return "El numero es impar"


if __name__ == '__main__':
    print(verificaion_pares())
