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


# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada
# paquete así que deben calcular el peso de los payasos y muñecas que saldrán en
# cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un
# programa que lea el número de payasos y muñecas vendidos en el último pedido y
# calcule el peso total del paquete que será enviado.
if __name__ == '__main__':
    clown_w: int = 112
    doll_w: int = 75
    print("Calculadora de peso de paquetes.")
    clown_q: int = solicitar_cantidad("payasos")
    doll_q: int = solicitar_cantidad("muñecas")
    total_w = (clown_q * clown_w) + (doll_q * doll_w)
    print(f"El peso total de paquetes es de {total_w}g")
