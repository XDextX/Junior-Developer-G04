# Created by German Montero at 9/8/2021
# Se desea obtener el salario neto de un empleado de una empresa cuyo trabajo se paga por
# horas, de la siguiente manera:
# a. Si la cantidad de horas trabajadas es menor o igual a 35, se paga la tarifa de hora
# normal.
# b. Si la cantidad es mayor a 35, para las primeras 35 horas se paga la tarifa normal y
# para el resto se paga la tarifa de hora extra.
# El usuario debe ingresar las horas trabajadas, el precio de la tarifa de hora normal y el
# precio de la tarifa de la hora extra. Valor 15 puntos

def pedir_dijito(msj: str = ""):
    res = input(msj)
    if res.isdigit():
        return int(res)
    else:
        print("El dato ingresado debe ser un numero entero.")
        return pedir_dijito(msj)


def datos_trabajador():
    horas_laboradas: int = pedir_dijito("Dijite las horas laboradas:> ")
    tarifa_regular: int = pedir_dijito("Dijite la tarifa de hora regular:> ")
    tarifa_extra: int = pedir_dijito("Dijite la tarifa de hora extra:> ")
    return horas_laboradas, tarifa_regular, tarifa_extra


def calculo_pago(horas_laboradas: int, tarifa_regular: int, tarifa_extra: int):
    limite_tarifa_normal = 35
    pago: int = 0
    if horas_laboradas > limite_tarifa_normal:
        pago = (limite_tarifa_normal * tarifa_regular) + \
               (horas_laboradas - limite_tarifa_normal) * tarifa_extra
    else:
        pago = horas_laboradas * tarifa_regular
    return pago


def reporte_de_pago(horas_laboradas: int, tarifa_regular: int, tarifa_extra: int, pago: int):
    print(f"Horas trabajadas: {horas_laboradas},\n"
          f"Tarifa normal por hora: {tarifa_regular},\n"
          f"Tarifa por hora extra: {tarifa_extra},\n"
          f"El pago correspondiente es de {pago}.\n\n"
          f"La tarifa por hora extra empieza a regir despues de 35 horas laboradas")


if __name__ == '__main__':
    print("Programa para calcular el pago de un trabajador.")
    horas_laboradas, tarifa_normal, tarifa_extra = datos_trabajador()
    pago = calculo_pago(horas_laboradas, tarifa_normal, tarifa_extra)
    reporte_de_pago(horas_laboradas, tarifa_normal, tarifa_extra, pago)
