from claseManejadorCamion import ManejadorCamion
from claseCosecha import Cosecha
from claseMenu import Menu
import os

def test():

    print('testeo de datos: ')
    print('"Ingreso de datos de la cosecha:"')
    camion = '2' ; dia = '42'; peso = '6000'
    print('1er :Camion {}, dia {}, peso {}'.format(camion,dia,peso))
    cosecha.cargarCosecha(manejadorC, camion, dia, peso)
    camion = '20';     dia = '55'; peso = '6000'
    print('2do :Camion {}, dia {}, peso {}'.format(camion,dia,peso))
    cosecha.cargarCosecha(manejadorC, camion, dia, peso)
    print('Presione ENTER para continuar \n')
    os.system('pause')

if __name__ == '__main__':
    print('PyCharm')
    cosecha = Cosecha()
    cosecha.crearmatrix()
    manejadorC = ManejadorCamion()
    manejadorC.testCamio()
    print('Desea ejecutar funcion test?')
    p = int(input('1:si, 2:no : '))
    if p == 1:
        #print('paso')
        test()
    os.system('cls')
    print('Desea cargar una cosecha o ejecutar menu?')
    p = int(input('1:cargar una cosecha, 2:ejecutar menu : '))
    if p == 1:
        bandera = False
        while not bandera:
            camion = input('Ingrese identificador del camio: ')
            dia = input('Ingrese dia de cosecha: ')
            peso = (input('Ingrese peso del camion: '))
            cosecha.cargarCosecha(manejadorC, camion, dia, peso)
            p = int(input('Desea ingresar otra cosecha?: 1 si, 2 no: '))
            if p==2:
                bandera = True

    cosecha.testCosecha(manejadorC)
    menu = Menu()
    bandera = False
    while not bandera:
        print(
            "\n------------Menu------------\n1. Cantidad total de kilos descargados un camion \n2. Lista de consecha de un dia \n3. Salir")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op, manejadorC, cosecha)
        if op == 3:
            bandera = True
    







