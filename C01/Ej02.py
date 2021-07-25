# Created by German Montero at 19/7/2021
def mostrar_cantidad_letras(cadena: str):
    print(f"{cadena} tiene {len(cadena)} letras")


# Escribir un programa que pregunte el nombre del usuario en la consola y después
# de que el usuario lo introduzca muestre por pantalla<NOMBRE> tiene <n> letras,
# donde<NOMBRE>es el nombre de usuario en mayúsculas y <n>es el número de letras
# que tienen el nombre.
if __name__ == '__main__':
    nombre: str = input("Dijite un nombre: ")
    mostrar_cantidad_letras(nombre.upper())
