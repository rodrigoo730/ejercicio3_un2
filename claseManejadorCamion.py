from claseCamion import Camion
import csv
class ManejadorCamion:
    __listaC = []
    def __init__(self):
        self.__listaC= []
    def testCamio(self):
        archivo = open('camiones.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                camion = Camion(fila[0], fila[1], fila[2], fila[3], fila[4])
                self.__listaC.append(camion)

        archivo.close()

    def obtenerCamion(self,ind):
        return self.__listaC[ind]
    def obtenerTara1(self,ind):
        return self.__listaC[ind].obtenerTara()






