# Created by German Montero at 19/7/2021
def solicitar_cantidad(articulo: str) -> int:
    numero: int = 0
    while numero <= 0:
        respuesta = input(f"Dijites la cantidad de {articulo} vendida: ")
        if respuesta.isdigit():
            if int(respuesta) > 0:
                numero = int(respuesta)
            else:
                print(f"El numero de {articulo} debe ser un numero mayor a 0.")
        else:
            print(f"El numero de {articulo} debe ser un numero mayor a 0.")

    return numero


# Una panadería vende barras de pan a ¢600 cada una. El pan que no es el día tiene
# un descuento del 60%. Escribir un programa que comience leyendo el número de
# barras vendidas que no son del día. Después el programa debe mostrar el precio
# habitual de una barra de pan, el descuento que se le hace por no ser fresca y el
# coste final total.
if __name__ == '__main__':
    precio_barra: int = 600
    descuento_no_fresco: int = 60
    cantidad_barras = solicitar_cantidad("barras del dia anterior")
    print(f"Precio regular de barras de pan: ¢{precio_barra}")
    print(f"Descuento por no ser barra fresca:{descuento_no_fresco}% ({precio_barra * (descuento_no_fresco / 100)})")
    print(f"Coste final:{(precio_barra * (descuento_no_fresco / 100)) * cantidad_barras}")
