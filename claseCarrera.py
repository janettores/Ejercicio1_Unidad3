class Carrera:
    __codCarrera: int
    __nomCarrera: str
    __titulo: str
    __duracion: str
    __tipo: str

    def __init__(self, codCarrera, nomCarrera, titulo, duracion, tipo):
        self.__codCarrera = codCarrera
        self.__nomCarrera = nomCarrera
        self.__titulo = titulo
        self.__duracion = duracion
        self.__tipo = tipo

    def __str__(self):
        return f'Codigo: {self.__codCarrera}, Nombre: {self.__nomCarrera}, Titulo:{self.__titulo}, Duracion:{self.__duracion}, Tipo:{self.__tipo}'

    def getCodigoCarrera(self):
        return self.__codCarrera

    def getNombreCarrera(self):
        return self.__nomCarrera