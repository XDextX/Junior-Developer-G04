# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a $1000
# mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el
# usuario tiene que tributar o no.
def verificacion_tributacion():
    edad_minima = 16
    monto_minimo = 1000
    monto_mensual: int = 0
    edad: int = 0
    s_edad = input("Dijite su edad actual: ")
    s_monteo_mensual = input("Dijite su edad actual: ")
    if s_edad.isdigit():
        edad = int(s_edad)
    if s_monteo_mensual.isdigit():
        monto_mensual = int(monto_mensual)
    if monto_mensual >= monto_minimo and edad_minima <= edad:
        print("Debe tributar")
    else:
        print("No debe tributar")


if __name__ == '__main__':
    verificacion_tributacion()
