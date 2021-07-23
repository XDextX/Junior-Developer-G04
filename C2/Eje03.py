# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el
# programa debe mostrar un error.
def dividir():
    divisor: float
    dividendo: float
    r_dividendo = input("Dijite el dividendo: ")
    r_divisor = input("Dijite el divisor: ")
    if r_dividendo.isdigit() or r_dividendo.isdecimal():
        dividendo = float(r_dividendos)
    if r_divisor.isdigit() or r_divisor.isdecimal():
        divisor = float(r_divisor)
    if divisor == 0:
        resultado = "El divosor de be ser un numero diferente de 0. "
    else:
        resultado = f"{resultado}"

    return resultado


if __name__ == '__main__':
    print("Dijite 2 numero para efectuar la divicion")
    dividir()
