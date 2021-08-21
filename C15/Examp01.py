# Created by German Montero at 20/8/2021
class Usuario:
    def __init__(self, nombre: str, clave: str):
        self._clave = clave
        self.nombre = nombre


if __name__ == '__main__':
    usuario = Usuario("Roberto", "asdas")
    print(usuario.nombre, usuario._clave)
