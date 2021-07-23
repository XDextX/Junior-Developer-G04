# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado
# por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
def verificacion_grupo():
    nombre = input("Ingrese su nombre")
    genero = input("Ingrese su genero (m/f)")
    if (nombre[0].lower() <= "m" and genero == "f") or (nombre[0].lower() >= "n" and genero == "m"):
        print("Pertenece al grupo A")
    else:
        print("Pertenece al grupo B")


def letra_mayor(a: str, b: str):
    if a < b:
        print(f"{a}<{b}")
    else:
        print(f"{a}>{b}")


if __name__ == '__main__':
    verificacion_grupo()
# letra_mayor("m", "n")
