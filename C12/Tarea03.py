# Escribir una funcióndiaSiguienteEque dada una fecha
# expresada como la terna (Día, Mes, Año) (donde Día, Mes y
# Año son números enteros) calcule el día siguiente al dado,
# en el mismo formato.

def obtener_fecha():
    d = int(input("Ingrese el dia actual"))
    m = int(input("Ingrese el mes actual"))
    a = int(input("Ingrese el año actual"))
    return d, m, a


def dia_siguiente(datatime: tuple):
    d, m, a = datatime
    max_days = 31
    if m == 2:
        max_days = 28
    elif m % 2 == 0:
        max_days = 30
    else:
        max_days = 31
    next_d = d
    next_m = m
    next_a = a
    if d + 1 > max_days:
        next_d = (d + 1) - max_days
        next_m += 1
    else:
        next_d += 1
    if next_m > 12:
        next_m = next_m - 12
        next_a += 1

    return next_d, next_m, next_a


def imprimir_fecha(datatime1: tuple, datatime2: tuple):
    dia, mes, anio = datatime1
    next_d, next_m, next_a = datatime2
    print(f"la fecha siguiente a {dia}/{mes}/{anio} es {next_d}/{next_m}/{next_a}")


if __name__ == '__main__':
    t = obtener_fecha()

    imprimir_fecha(t, dia_siguiente(t))
