def lleno(tam):
    numeros = []
    for x in range(tam):
        nums = int(input("Digite el numero: "))
        numeros.append(nums)
    return numeros

def suma(lista1, lista2):
    s = []
    for x in range(len(lista1)):
        resultado = lista1[x] + lista2[x]
        s.append(resultado)
    return s


def imprimo(nums):
    for x in range(len(nums)):
        print(nums[x], end=" ")
    print("")



tam = int(input("El tamaño de las listas: "))
print("LLENA TU PRIMERA LISTA")
lista1 = lleno(tam)
print("")
print("LLENA TU SEGUNDA LISTA")
lista2= lleno(tam)
print("Lista 1")
imprimo(lista1)
print("Lista 2")
imprimo(lista2)
sumatoria = suma(lista1, lista2)
print("Lista 3")
imprimo(sumatoria)

