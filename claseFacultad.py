#from claseCarrera import Carrera
class Facultad:
    __codigo: int
    __nombre: str
    __direccion: str
    __localidad: str
    __telefono: str
    __listacarrera: list

    def __init__(self, codigo, nombre, direccion, localidad, telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__listacarrera = []

    def __str__(self):
        return f'\nCodigo de Facultad: {self.__codigo}, Nombre Facultad: {self.__nombre}, Direccion:{self.__direccion},Localidad:{self.__localidad},Telefono:{self.__telefono}'

    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def getLocalidad(self):
        return self.__localidad

    def getTelefono(self):
        return self.__telefono

    def getListaCarrera(self):
        return self.__listacarrera

    def agregarCarrera(self, unaCarrera):
        self.__listacarrera.append(unaCarrera)

    def mostrarCarreras(self):
        for i in range(len(self.__listacarrera)):
            print(self.__listacarrera[i])

    def nombreYDuracion(self):
        for i in range(len(self.__listacarrera)):
            print('Codigo:', self.__listacarrera[i].getCodigoCarrera())
            print('Nombre', self.__listacarrera[i].getNombreCarrera())

    def buscarCarrera(self, carrera):
        carrera = carrera.lower()
        i = 0
        flag = False
        while not flag and i < len(self.__listacarrera):
            if self.__listacarrera[i].nombre() == carrera:
                print(f"{self.__codigo}.{self.__listacarrera[i].codigo()}")
                print(self.__listacarrera[i])
                print("Localidad: ", self.__localidad)
                flag = True
            else:
                i += 1