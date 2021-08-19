# Created by German Montero at 18/8/2021
class Persona:
    def __init__(self, nombre):
        self.nombre: str = nombre

    def imprimir(self):
        print(f"Buenas tardes {self.nombre}")


if __name__ == '__main__':
    objecto = Persona("German")
    objecto.imprimir()
