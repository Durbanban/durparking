from datetime import datetime
from locale import setlocale, LC_ALL

setlocale(LC_ALL, 'es-ES')


class Ocupacion:

    def __init__(self, fecha_deposito=None, plaza=None, vehiculo=None):
        self.__fecha_deposito = fecha_deposito
        self.__plaza = plaza
        self.__vehiculo = vehiculo

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

    def __str__(self):
        return f"******************************************************\nMatrícula: {self.__vehiculo.matricula}\n" \
               f"Fecha: {self.__fecha_deposito.strftime('%A %d de %B de %Y a las %I:%M:%S')}\n" \
               f"Plaza: {self.__plaza.id}\n" \
               f"PIN: {self.__plaza.pin}\n" \
               f"******************************************************"