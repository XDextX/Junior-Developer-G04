def lleno():
    personas = []
    tam = int(input("DIGITE EL NUMERO DE PERSONAS: "))
    for x in range(tam):
        nombre = input("Digite el nombre: ")
        personas.append(nombre)
    return personas


def ordeno(lista):
    for y in range(len(lista)):
        for x in range(len(lista) - 1):
            if lista[x].upper() > lista[x + 1].upper():
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
print("La lista ordenada >", end="")
imprimo(orden)