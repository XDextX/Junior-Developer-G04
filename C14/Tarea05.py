# Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para
# inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero,
# isósceles o escaleno).

class Triangulo:

    def __init__(self):
        self.lados = [0, 0, 0]

    def ingresar_lados(self):
        print("Ingrese los lados del triangulo:")
        for i in range(len(self.lados)):
            self.lados[i] = int(input(f"Lado #{i + 1}:>_ "))

    def lado_mayor(self):
        mayor = 0
        for i in self.lados:
            if i > mayor:
                mayor = i
        print(f"El lado mayor mide {mayor}")

    def clasificar(self):
        unicos = []
        clasificacion = ""
        for i in self.lados:
            unico = True
            for j in unicos:
                if i == j:
                    unico = False
            if unico:
                unicos.append(i)
        diferentes = len(unicos)
        if diferentes == 1:
            clasificacion = "Equilatero"
        elif diferentes == 2:
            clasificacion = "Isósceles"
        else:
            clasificacion = "Escaleno"
        print(f"EL triangulo es {clasificacion}")


if __name__ == '__main__':
    triangulo = Triangulo()
    triangulo.ingresar_lados()
    triangulo.lado_mayor()
    triangulo.clasificar()
