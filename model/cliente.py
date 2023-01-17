class Cliente:

    def __init__(self, id, vehiculo=None):
        self.__id = id
        self.__vehiculo = vehiculo

    @property
    def id(self):
        return self.__id

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, nuevo_vehiculo):
        self.__vehiculo = nuevo_vehiculo

    def __str__(self):
        return f"Id: {self.__id}\n" \
               f"Tipo de vehiculo: {self.__vehiculo.tipo}"