class Ocupacion:

    def __init__(self, plaza, vehiculo):
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