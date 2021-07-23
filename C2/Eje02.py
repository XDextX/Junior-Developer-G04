# Escribir un programa que almacene la cadena de caracterescontraseña en una variable, pregunte al usuario por la
# contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable
# sin tener en cuenta mayúsculas y minúsculas.
def verificar_clave():
    clave: str = obtener_clave().lower()
    clave_ingresada: str = input("Ingrese su contraseña: ").lower()
    if clave == clave_ingresada:
        print("Bienvenido")
    else:
        print("Clave incorrecta")


def obtener_clave() -> str:
    return "hola"


if __name__ == '__main__':
    verificar_clave()
