# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10

def obtener_tabla() -> int:
    res = input("ingrese un numero: ")
    if res.isdigit():
        return int(res)
    else:
        print("Debe ingresar un numero mayor a 0")
        return obtener_tabla()


def desplegar_tabla(tabla: int):
    for i in range(10):
        print(f"{tabla} x {i + 1} = {tabla * (i + 1)}")


if __name__ == '__main__':
    desplegar_tabla(obtener_tabla())
