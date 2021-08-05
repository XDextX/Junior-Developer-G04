# Created by German Montero at 4/8/2021
# Crear y cargar dos listas con los nombres de 5 productos en una
# y sus respectivos precios en otra. Definir dos listas paralelas.
# Mostrar cuantos productos tienen un precio mayor al primer
# producto ingresado
def llenar() -> tuple[list[str], list[int]]:
    productos: list[str] = []
    precios: list[int] = []
    tam = int(input("Ingrese la cantidad de registros: "))
    for i in range(tam):
        producto = input("Dijite el nombre del producto: ")
        precio = int(input("Dijite el precio del producto: "))
        productos.append(producto)
        precios.append(precio)
    return productos, precios


def imprimir(nombres: list[str], edades: list[int]):
    if len(nombres) == len(edades):
        for i in range(len(nombres)):
            print(f"Nombre: {nombres[i]},"
                  f"Edad: {edades[i]}")


def imprimr_productos_mas_caros_al_primero(productos: list[str], precios: list[int]):
    primer_precio = precios[0]
    productos_mas_caros = 0
    for i in range(1, len(productos)):
        if precios[i] > primer_precio:
            productos_mas_caros += 1
    print(f"{productos_mas_caros} productos son mas caros al primer producto ingresado")


if __name__ == '__main__':
    productos, precios = llenar()
    imprimr_productos_mas_caros_al_primero(productos, precios)
