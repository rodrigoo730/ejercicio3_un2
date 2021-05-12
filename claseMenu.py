from claseCosecha import Cosecha
from claseManejadorCamion import ManejadorCamion
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1, 2:self.opcion2, 3:self.salir}

    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op,manejadorC, cosechas):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))

        bandera=False
        while not bandera:
            if op == 1 or op == 2 or op== 3:
                bandera = True
            else:
                print('Opción no válida')
                op = int(input('Ingrese una opcion: '))
        func(manejadorC, cosechas)

    def salir(self,manejador,cosecha):
        print('Salir')

    def opcion1(self,manejadorC,cosechas):
        ind = input('Ingrese identificador del camion ')
        bandera = False
        while not bandera:
            if (not ind.isdigit()) or (int(ind) > 20):
                print('Dato erroneo del identificador , intente denuevo ')
                ind = input('Ingrese identificador: ')
            else:
                bandera = True
        kilos = cosechas.obtenerCosechaCamion(int(ind)-1)
        print('Kilos total descargados del camnio {} es {}'.format(ind,kilos))

    def opcion2(self,manejadorC, cosechas):
        dia=input('Ingrese dia (el archivo cosecha solo tiene 3 dias): ')
        bandera = False
        while not bandera:
            if (not dia.isdigit()) or (int(dia) > 3):
                print('Dato erroneo del dia, el archivo solo tiene cargado hasta el dia 3 ')
                dia = input('Ingrese dia: ')
            else:
                bandera = True
        dia_c=cosechas.obtenerDia(int(dia)-1)
        print('PATENTE        CONDUCTOR        CANTIDAD DE KILOS \n')
        for i in range(len(dia_c)):
            camion = manejadorC.obtenerCamion(i)
            #print('fila {}'.format(i))
            print('{}           {}                  {}\n'.format(camion.obtenerPatente(),camion.obtenerNombre(),dia_c[i]))


