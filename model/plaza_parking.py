from random import randint

class PlazaParking:

    def __init__(self, id, libre, tipo, tarifa):
        self.__id = id
        self.__libre = libre
        self.__tipo = tipo
        self.__tarifa = tarifa

    @property
    def id(self):
        return self.__id;

    @property
    def is_libre(self):
        return self.__libre

    @is_libre.setter
    def is_libre(self, libre):
        self.__libre = libre

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        if (nuevo_tipo in ["turismo", "moto", "movilidad"]):
            self.__tipo = nuevo_tipo
        else:
            print("Introduce un tipo válido (turismo, moto, movilidad")

    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def tarifa(self, nueva_tarifa):
        if (nueva_tarifa >= 0):
            self.tarifa = nueva_tarifa
        else:
            print("Introduce una tarifa válida (sólo números positivos")

    def generar_pin(self):
        pin = ''
        for cifra in range(0, 6):
            pin += str(randint(0, 9))
        self.__pin == pin



    def borrar_pin(self, pin=None):
        if hasattr(self, pin):
            delattr(self, pin)
        else:
            print("La plaza no tiene pin asociado")



    def __str__(self):
        return f"Id: {self.__id}\n" \
               f"Libre: {self.__libre}\n" \
               f"Tipo: {self.__tipo}\n" \
               f"Tarifa: {self.__tarifa} cent por minuto"

    def __eq__ (self, other):
        if not isinstance(other, PlazaParking):
            return NotImplemented
        return self.__id == other.id \
               and self.__libre == other.libre \
               and self.__tipo == other.tipo \
               and self.__tarifa == other.tarifa

