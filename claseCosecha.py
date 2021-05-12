import csv
import os



class Cosecha:
    __lista = []

    def __init__(self):
        self.__lista = []

    def crearmatrix(self):
        for i in range(45):
            self.__lista.append([])
            for j in range(20):
                self.__lista[i].append(0)


    def testCosecha(self,manejador):
        archivo = open('cosechas.csv')
        reader = csv.reader(archivo,delimiter=';')
        i=0
        for fila in reader:
            for j in range(20):
                camion_p = manejador.obtenerCamion(j)
                cosecha = int(fila[j]) - camion_p.obtenerTara()
                self.__lista[i][j]= cosecha
            i += 1

        archivo.close()


    def cargarCosecha(self,manejador,camion,dia,peso):
        bandera = True
        #print(type(camion))
        if (not camion.isdigit()) or (int(camion) > 20):
            print('id del camion no valido')
            bandera = False
        if (not dia.isdigit()) or (int(dia) > 45):
            print('Dia no valido')
            bandera = False
        if not peso.isdigit():
            print('Peso no valido')
            bandera = False
        if not bandera:
            print('Error, no se cargo la cosecha')

        else:
            camion= int(camion) ; dia= int(dia)  ; peso= int(peso)
            camion_ob = manejador.obtenerCamion(camion - 1)
            peso = peso - camion_ob.obtenerTara()
            self.__lista[dia - 1][camion - 1] += peso
            print('Cosecha registrada: kg ={} camion ={} dia ={} \n '.format(self.__lista[dia - 1][camion - 1], camion,dia))





    def obtenerCosechaCamion(self,indice):
        cont=0
        for i in range(3):
            cont+= int(self.__lista[i][indice])
        return cont

    def obtenerDia(self,i):
        return self.__lista[i]


