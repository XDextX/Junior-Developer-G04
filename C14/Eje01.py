# Created by German Montero at 18/8/2021
# Realizar una clase que administre una agenda. Se debe almacenar para
# cada contacto el nombre, el teléfono y el email. Además deberá mostrar
# un menú con las siguientes opciones
# ◦ Añadir contacto
# ◦ Lista de contactos
# ◦ Buscar contacto
# ◦ Editar contacto
# ◦ Cerrar agenda
class Contacto:
    def __init__(self, nombre: str, telefono: str, email: str):
        self.email = email
        self.telefono = telefono
        self.nombre = nombre

    def mostrar(self):
        text = f"Nombre:{self.nombre}\n" \
               f"Telefono:{self.telefono}\n" \
               f"E-mail:{self.email}"
        print(text)
        return text


class Agenda:
    def __init__(self, contactos=None):
        if contactos is None:
            contactos = []
        self.contactos: list[Contacto] = contactos

    def agregar(self, contacto: Contacto):
        self.contactos.append(contacto)

    def buscar(self, nombre: str):
        for i in range(len(self.contactos)):
            if nombre == self.contactos[i].nombre:
                return i
            else:
                return -1

    def mostrar(self, indice):
        if -1 < indice < len(self.contactos):
            self.contactos[indice].mostrar()

    def obtener(self, indice: int):
        if -1 < indice < len(self.contactos):
            return self.contactos[indice]
        else:
            return None

    def menu(self):
        seguir = True
        while (seguir):
            print(self.opciones())
            opcion = input("")
            if opcion == "1":
                contacto = self.nuevo_contacto()
                self.agregar(contacto)
            elif opcion == "2":
                for i in range(len(self.contactos)):
                    self.mostrar(i)
            elif opcion == "3":
                nombre = input("Ingrese el nombre del contacto")
                indice = self.buscar(nombre)
                if indice > 0:
                    self.mostrar(indice)
                else:
                    print("Sin coincidencias")
            elif opcion == "4":
                print(self.opciones_edicion())
                i

    def nuevo_contacto(self):
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el telefono del contacto: ")
        email = input("Ingrese el e-mail del contacto: ")
        contacto = Contacto(nombre, telefono, email)
        return contacto

    def opciones(self):
        return "1. Añadir contacto\n" \
               "2. Listar contactos\n" \
               "3. Buscar contacto\n" \
               "4. Editar contacto\n" \
               "5. Cerrar Agenda\n"

    def opciones_edicion(self):
        return "1. Nombre" \
               "2. Telefono" \
               "3. E-mail"

    def editar_contacto(self, indice: int, opcion: str):
        contacto = self.contactos[indice]
        if opcion == "1":
            nombre = input("Digite el nombre del contacto: ")
            contacto.nombre = nombre
        elif opcion == "2":
            telefono = input("Digite el e-mail del contacto: ")
            contacto.telefono = telefono
        elif opcion == "3":
            email = input("Digite el e-mail del contacto: ")
            contacto.email = email


if __name__ == '__main__':
    print("Hola")
