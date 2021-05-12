

class Camion:
    __indentificador=0
    __nombre=''
    __patenteCamion=0
    __marcaCamion=''
    __tara=0
    def __init__(self,inden=0,nom='',paten=0,marca='',tara=0):
        self.__indentificador = inden
        self.__nombre = nom
        self.__patenteCamion = paten
        self.__marcaCamion = marca
        self.__tara = int(tara)
    def obtenerIndent(self):
        return self.__indentificador
    def obtenerTara(self):
        return self.__tara
    def obtenerNombre(self):
        return self.__nombre
    def obtenerPatente(self):
        return self.__patenteCamion