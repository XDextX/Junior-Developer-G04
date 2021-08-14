# Created by German Montero at 13/8/2021
# Crea una tupla con los meses del año, pide
# números al usuario, si el numero esta entre
# 1 y la longitud máxima de la tupla, muestra
# el contenido de esa posición sino muestra un
# mensaje de error. El programa termina cuando
# el usuario introduce un cero.
def meses():
    return (
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre"
    )


def busqueda(dato: int):
    mes = meses()
    if dato >= len(mes):
        print(f"{dato} no corresponde a un mes valido")
        return ""
    for i in range(len(mes)):
        if i + 1 == dato:
            return mes[i].capitalize()


def main():
    dato = int(input("Dijite un numero referete al: "))
    mes = busqueda(dato)
    if mes != "":
        print(f"el numero indicado corresponde a el mes de {mes}")


if __name__ == '__main__':
    main()
