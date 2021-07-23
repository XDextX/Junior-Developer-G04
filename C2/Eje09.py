# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma
# automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del
# cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18
# años debe pagar $5 y si es mayor de 18 años, $10.
def cuota_de_entreda():
    s_edad = input("Dijite su edad")
    edad: int
    if s_edad.isdigit():
        edad = int(s_edad)
    else:
        edad = -1
        print("Edad no valida")
        return
    if edad > 18:
        print("Son $10 por favor")
    elif edad > 4:
        print("Son $5 por favor")
    else:
        print("Entra gratis, pase adelante")


if __name__ == '__main__':
    cuota_de_entreda()
