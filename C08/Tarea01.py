# En un curso de 4 alumnos se registraron y la nota de su examen y se deben procesar de acuerdo a lo siguiente:
# a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
# b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar "Muy Bueno" si
# la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
# c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”
def llenar():
    tam = int(input("Dijite la cantidad de registros a llenar"))
    _nombres: list[int] = []
    _notas: list[str] = []
    for i in range(tam):
        nombre = input("Ingrese la nota del estudiante: ")
        nota = int(input("Ingrese la nota: "))
        _notas.append(nota)
        _nombres.append(nombre)
    return _nombres, _notas


def condicion(nota: int) -> str:
    leyenda = ""
    if (nota > 7):
        leyenda = "Muy bueno"
    elif (nota > 3):
        leyenda = "Bueno"
    else:
        leyenda = "Insuficiente"
    return leyenda


def listar_alumnos(alumnos: list[str], notas: list[int]):
    for i in range(len(alumnos)):
        print(f"Alumno:{alumnos[i]}", end=", ")
        print(f"Nota:{notas[i]}", end=", ")
        print(f"Condicion:{condicion(notas[i])}")


def condicion_muy_bueno(alumnos: list[str], notas: list[int]):
    _alumnos: list[str] = []
    _notas: list[int] = []
    for i in range(len(alumnos)):
        if condicion(notas[i]) == "Muy bueno":
            _alumnos.append(alumnos[i])
            _notas.append(notas[i])
    print(f"Alumnos en condicion \"Muy bueno\":{len(_alumnos)}")
    # listar_alumnos(_alumnos, _notas)


if __name__ == '__main__':
    mocosos, calificaciones = llenar()
    listar_alumnos(mocosos, calificaciones)
    condicion_muy_bueno(mocosos, calificaciones)
