# Created by German Montero at 11/8/2021
# ◦Crear y cargar una lista con los nombres de tres alumnos. Cada
# alumno tiene dos notas, almacenar las notas en una lista paralela.
# Cada componente de la lista paralela debe ser también una lista con
# las dos notas. Imprimir luego cada nombre y sus dos notas.
# ◦ Si cargáramos los datos por asignación sería algo parecido a esto:
# ◦ alumnos=["juan", "ana", "luis"]
# ◦ notas=[[10,8], [6,5], [2,8]]

def llenar_matriz():
    notas = []
    alumnos = []
    filas = int(input("Dijite la cantidad de estudiantes: "))
    columnas = int(input("Dijite la cantidad de notas por estudiante: "))
    for f in range(filas):
        notas.append([])
        nombre = input("Dijite el nombre del estudiante: ")
        alumnos.append(nombre)
        for col in range(columnas):
            num = int(input(f"Dijite un valor para la nota {col + 1}: "))
            notas[f].append(num)
    return alumnos, notas


def imprimir(alumnos: list, notas: list[list]):
    print("Desglose de notas: ")
    s = ""
    for i in range(len(alumnos)):
        s += f"Alumno: {alumnos[i]}"
        for j in range(len(notas[i])):
            s += f"\n\tNota {j + 1}: {notas[i][j]}"
        s += "\n"
    print(s)


if __name__ == '__main__':
    alumnos, notas = llenar_matriz()
    # alumnos = ["juan", "ana", "luis"]
    # notas = [[10, 8], [6, 5], [2, 8]]
    imprimir(alumnos, notas)
