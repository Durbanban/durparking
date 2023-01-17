from datetime import datetime

class Cobro:
    def __init__(self, cantidad):
        self.__cantidad = cantidad
        self.__fecha = datetime.now()

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if nueva_cantidad > 0:
            self.__cantidad = nueva_cantidad
        else:
            print("La cantidad debe ser positiva")

    @property
    def fecha(self):
        return self.__fecha