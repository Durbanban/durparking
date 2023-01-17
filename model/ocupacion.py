from datetime import datetime

class Ocupacion:

    def __init__(self, plaza, vehiculo, fecha_deposito):
        self.__plaza = plaza
        self.__vehiculo = vehiculo
        self.__fecha_deposito = fecha_deposito

    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, nueva_plaza):
        self.__plaza = nueva_plaza

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, nuevo_vehiculo):
        self.__vehiculo = nuevo_vehiculo

    @property
    def fecha_deposito(self):
        return self.__fecha_deposito

    @fecha_deposito.setter
    def fecha_deposito(self, nueva_fecha_deposito):
        if nueva_fecha_deposito > datetime.now():
            self.__fecha_deposito = nueva_fecha_deposito
        else:
            print("Introduzca una fecha válida")