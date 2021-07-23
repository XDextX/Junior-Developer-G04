# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo
# de pizza aparecen a continuación.
#   ◦Ingredientes vegetarianos: Pimiento y tofu.
#   ◦Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su
# respuesta le muestre unmenú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente
# además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza
# elegida es vegetariana o no y todos los ingredientes que lleva.
def menu_pizzeria():
    print("Pizzería Bella Napoli")
    print("Desea una pizza Vejetariana")
    res = input("(s/n)")
    print("Todas las pizzas llevan mozzarella y tomate")
    tipo_pizza: str
    ingrediente: str
    if res.lower() == "s":
        tipo_pizza = "Vegetariana"
        ingrediente = menu_vejetariano()
    else:
        tipo_pizza = "Carnes"
        ingrdiente = menu_carnes()
    print(f"La pizza elegida fue {tipo_pizza} y los ingredientes fueron mozarella, tomate y {ingrdiente}")


def menu_vejetariano():
    print("1.Pimiento, 2.Tofu")
    res = input(":> ")


def menu_carnes():
    print("1.Peperoni,2. Jamón ,3.Salmón")
    res = input(":> ")
    if res == "1":
        return "Peperoni"
    elif res == "2":
        return "Jamón"
    else:
        return "Salmón"


if __name__ == '__main__':
    menu_pizzeria()
