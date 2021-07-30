def lleno():
    ganadores = []
    num = 1
    print("Digite los numeros ganadores y 0 para terminar")
    while (num > 0):
        num = int(input("Digite el numero-> "))
        if (num != 0):
            ganadores.append(num)
    return ganadores


def ordeno(lista):
    for y in range(len(lista)):
        for x in range(len(lista) - 1):
            if lista[x] > lista[x + 1]:
                aux = lista[x]
                lista[x] = lista[x + 1]
                lista[x + 1] = aux
    return lista


def imprimo(nums):
    for x in range(len(nums)):
        print(nums[x], end=" ")
    print("")


lista = lleno()
imprimo(lista)
orden = ordeno(lista)
print("La lista de los premios ordenada >", end="")
imprimo(orden)