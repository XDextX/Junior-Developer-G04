# Created by German Montero at 13/8/2021
def dia_mes_anio() -> tuple:
    dia = int(input("ingrese el dia del mes actual: "))
    mes = input("Ingrese el mes actual: ")
    anio = int(input("Ingrese el año actual: "))
    return dia, mes, anio


def imprimir_fecha(datatime: tuple):
    dia, mes, anio = datatime
    print(f"la fecha de hoy es {dia}/{mes}/{anio}")


if __name__ == '__main__':
    imprimir_fecha(dia_mes_anio())
