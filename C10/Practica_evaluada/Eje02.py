# Created by German Montero at 9/8/2021
# Haga el algoritmo que permita calcular la cantidad de estudiantes que aprobó, perdió o
# fue a ampliación en un curso para el cuál realiza una cantidad de tres exámenes. El primer
# examen vale un 20 %, el segundo un 30% y el tercero un 50 %. La cantidad de estudiantes
# debe ser ingresada por el usuario. Un estudiante pasa el curso si tiene una nota mayor o
# igual a 70, lo pierde si tiene una nota menor a 60. Si la nota está entre 60 y 69 va a
# ampliación. Valor 30 puntos.
import random


def pedir_dijito(msj: str = ""):
    res = input(msj)
    if res.isdigit():
        return int(res)
    else:
        print("El dato ingresado debe ser un numero entero.")
        return pedir_dijito(msj)


def obtener_notas(cantidad: int):
    primero: list[int] = []
    segundo: list[int] = []
    tercero: list[int] = []
    for i in range(cantidad):
        primero.append(random.randint(20, 100))
        segundo.append(random.randint(30, 100))
        tercero.append(random.randint(50, 100))
    return primero, segundo, tercero


def sacar_pesos(nota, peso):
    porcentaje_obtenido = ((nota * peso) / 100)
    return porcentaje_obtenido


def mostrar_resultados(primer_examen, segundo_examen, tercer_examen, ponderado):
    print(f"primer examen: {primer_examen}\n"
          f"segundo examen: {segundo_examen}\n"
          f"tercer examen: {tercer_examen}\n"
          f"Nota final: {ponderado:.2f}")


def verificar_condicion(primer_examen: list, segundo_examen: list, tercer_examen: list):
    aprobados = 0
    aplazados = 0
    reprobados = 0
    for i in range(len(primer_examen)):
        peso1 = sacar_pesos(primer_examen[i], 20)
        peso2 = sacar_pesos(segundo_examen[i], 30)
        peso3 = sacar_pesos(tercer_examen[i], 50)
        peso_neto = peso3 + peso2 + peso1
        if peso_neto >= 70:
            aprobados += 1
        elif peso_neto > 60:
            aplazados += 1
        else:
            reprobados += 1
        print(f"\nEstudiante {i}:")
        mostrar_resultados(primer_examen[i],
                           segundo_examen[i],
                           tercer_examen[i],
                           peso_neto)
    print()
    return aprobados, aplazados, reprobados


def main():
    estudiantes = pedir_dijito("Dijite la cantidad de estudiantes: ")
    examn1, examen2, examen3 = obtener_notas(estudiantes)
    aprobados, aplazados, reprovados = verificar_condicion(examn1, examen2, examen3)
    print(f"Estudiantes aprovados:{aprobados},\n"
          f"Estudiantes aplazados:{aplazados},\n"
          f"Estudiantes reprobados:{reprovados}\n"
          )


if __name__ == '__main__':
    main()
