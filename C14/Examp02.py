# Created by German Montero at 18/8/2021
# Implementar una clase llamada Alumno que tenga como
# atributos su nombre y su nota. Definir los métodos para
# inicializar sus atributos, imprimirlos y mostrar un mensaje
# si está regular (nota mayor o igual a 4)
# Definir dos objetos de la clase Alumno
class Alumno:
    nombre: str
    nota: int

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre}\n"
              f"Nota: {self.nota}")

    def calificacion(self):
        text: str = ""
        if self.nota >= 4:
            text = "El estudiante esta regular"
        else:
            text = "El estudiante no esta regular"
        print(text)


if __name__ == '__main__':
    estudiante01 = Alumno("German", 5)
    estudiante02 = Alumno("Carlos", 2)

    for i in [estudiante01, estudiante02]:
        i.imprimir()
        i.calificacion()
