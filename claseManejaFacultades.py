import csv
from claseFacultad import Facultad
from claseCarrera import Carrera
class ManejaFacultades:
    __listafacu: list

    def __init__(self):
        self.__listafacu = []    #crea una lista bidimensional

    def agregarFacultad(self, unaFacultad):
        self.__listafacu.append(unaFacultad)

    def cargar(self):
        archivo = open('Facultades.csv', 'r')
        reader = csv.reader(archivo, delimiter=',')
        i = 0
        next(reader)
        for fila in reader:
            if int(fila[0]) != i:
                unaFacultad = Facultad(int(fila[0]), fila[1], fila[2], fila[3], fila[4])
                self.agregarFacultad(unaFacultad)
                i = int(fila[0])
            else:
                unaCarrera = Carrera(int(fila[1]), fila[2], fila[3], fila[4], fila[5])
                self.__listafacu[i-1].agregarCarrera(unaCarrera)

    def mostrarLista(self):
        for i in range(len(self.__listafacu)):
            print(self.__listafacu[i])
            self.__listafacu[i].mostrarCarreras()

    def buscarFacultad(self, cod):
        i = 0
        band = False
        while band == False and i < len(self.__listafacu):
            if cod == int(self.__listafacu[i].getCodigo()):
                band = True
                print('Nombre de la Facultad:', self.__listafacu[i].getNombre())
                print('Carreras:\n')
                self.__listafacu[i].nombreYDuracion()
            else:
                i += 1

    def buscarCarrera(self, carrera):
        for facu in self.__listafacu:
            facu.buscarCarrera(carrera)