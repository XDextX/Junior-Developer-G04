# Escribir una clase en python llamada rectangulo que contenga una base y una altura, y que
# contenga un método que devuelva el área del rectángulo.
class Rectangulo:

    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


if __name__ == '__main__':
    rectangulo = Rectangulo(8, 4)
    print(f"El area del rectangulo es {rectangulo.area():.2f}")
