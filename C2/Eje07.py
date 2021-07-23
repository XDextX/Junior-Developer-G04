# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la
# evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden
# conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero
# conseguida en cada nivel es de $2.400 multiplicada por la puntuación del nivel. Escribir un programa que lea la
# puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

def rendimiento_anual():
    incentivo = 2.400
    s_rendimiento = input("Ingrese la puntucaion de rendimiento del usaurio")
    rendimiento: float = 0.0
    nivel: str = ""
    if s_rendimiento.isdigit() or s_rendimiento.isdecimal():
        rendimiento = float(s_rendimiento)
    else:
        print("El rendimeinto debe ser un numero igual o mayor a 0")
    if rendimiento >= 0.6:
        nivel = "Meritorio"
    elif rendimiento >= 0.4:
        nivel = "Aceptable"
    else:
        nivel = "Inaceptable"
    print(f"El empleado tiene una puntiacion de {rendimiento}"
          f"\nEl nivel es {nivel}"
          f"\nEl incentivo es de ${incentivo * rendimiento}")


if __name__ == '__main__':
    rendimiento_anual()
