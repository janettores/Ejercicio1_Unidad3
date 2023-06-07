from claseManejaFacultades import ManejaFacultades
if __name__ == '__main__':
    facultades = ManejaFacultades()
    facultades.cargar()
    facultades.mostrarLista()
    print('\n--Menu de Opciones--'
          '\n1: Mostrar una facultad + Nombre y Duracion de sus carreras'
          '\n2: Mostrar el Codigo de una carrera + Nombre y localidad de la facultad'
          '\n0: Salir del menu')
    op = int(input('Ingrese opcion:'))
    while op != 0:
        if op == 1:
            cod = int(input('Ingrese el codigo de una facultad'))
            facultades.buscarFacultad(cod)

        elif op == 2:
            carrera = input('Ingresar nombre de la carrera: ')
            facultades.buscarCarrera(carrera)
            
        print('\n--Menu de Opciones--'
              '\n1: Mostrar una facultad + Nombre y Duracion de sus carreras'
              '\n2: Mostrar el Codigo de una carrera + Nombre y localidad de la facultad'
              '\n0: Salir del menu')
        op = int(input('Ingrese opcion:'))