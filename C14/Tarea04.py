# Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva
# el área y otro que devuelva el perímetro del circulo.
import math


class Circulo:
    def __init__(self, radio: float):
        self.radio: float = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return math.pi * self.radio * 2


if __name__ == '__main__':
    circulo = Circulo(8)
    print(f"El area del circulo es {circulo.area():.2f}")
    print(f"El perimetro del circulo es {circulo.perimetro():.2f}")
