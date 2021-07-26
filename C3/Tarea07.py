# Escribir un programa que muestre el eco de todo
# lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def obtener_dato(mensaje):
    msj = input(mensaje)
    return msj


def eco():
    mensaje = obtener_dato("Empecemos con el eco, escriba 'salir' para parar\n:>_ ")
    while mensaje.lower() != "salir":
        print(mensaje)
        mensaje = obtener_dato(":>_ ")
    print("saliendo...")


if __name__ == '__main__':
    eco()
