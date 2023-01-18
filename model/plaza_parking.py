from random import randint

class PlazaParking:

    def __init__(self, id, libre, tipo, tarifa, abonado=None):
        self.__id = id
        self.__libre = libre
        self.__tipo = tipo
        self.__tarifa = tarifa
        self.__pin = ''
        self.__abonado = abonado

    @property
    def id(self):
        return self.__id;

    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id

    @property
    def libre(self) -> bool:
        return self.__libre

    @libre.setter
    def libre(self, nuevo_libre: bool):
        self.__libre = nuevo_libre

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

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, nuevo_pin):
        self.__pin = nuevo_pin

    @property
    def abonado(self):
        return self.__abonado

    @abonado.setter
    def abonado(self, nuevo_abonado):
        self.__abonado = nuevo_abonado

    def generar_pin(self):
        pin = ''
        for cifra in range(0, 6):
            pin += str(randint(0, 9))
        self.__pin = pin


    def generar_abonado(self, abonado):
        self.__abonado = abonado






    def __str__(self):
        if self.__abonado is not None:
            return f"Id: {self.__id}\n" \
                   f"Libre: {self.__libre}\n" \
                   f"Tipo: {self.__tipo}\n" \
                   f"Tarifa: {self.__tarifa} cent por minuto\n" \
                   f"PIN: {self.__pin}\n" \
                   f"Abonado: {self.__abonado.nombre}"
        elif self.__abonado is None:
            return f"Id: {self.__id}\n" \
                   f"Libre: {self.__libre}\n" \
                   f"Tipo: {self.__tipo}\n" \
                   f"Tarifa: {self.__tarifa} cent por minuto\n" \
                   f"PIN: {self.__pin}"

    def __eq__ (self, other):
        if not isinstance(other, PlazaParking):
            return NotImplemented
        return self.__id == other.id \
               and self.__libre == other.libre \
               and self.__tipo == other.tipo \
               and self.__tarifa == other.tarifa

