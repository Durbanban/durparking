from datetime import datetime


class Abono:
    def __init__(self, tipo, fecha_activacion, fecha_cancelacion, cliente):
        self.__tipo = tipo
        self.__fecha_activacion = fecha_activacion
        self.__fecha_cancelacion = fecha_cancelacion
        self.__caducidad = self.__fecha_cancelacion - self.__fecha_activacion
        self.__cliente = cliente

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        if (nuevo_tipo in ["mensual", "trimestral", "semestral", "anual"]):
            self.__tipo = nuevo_tipo
        else:
            print("Introduce un abono válido")

    @property
    def fecha_activacion(self):
        return self.__fecha_activacion

    @fecha_activacion.setter
    def fecha_activacion(self, nueva_fecha):
        self.__fecha_activacion = nueva_fecha

    @property
    def fecha_cancelacion(self):
        return self.__fecha_cancelacion

    @fecha_cancelacion.setter
    def fecha_cancelacion(self, nueva_fecha):
        if (nueva_fecha > datetime.now()):
            self.__fecha_cancelacion = nueva_fecha
        else:
            print("Introduce una fecha válida")

    @property
    def caducidad(self):
        return self.__caducidad

    def __eq__(self, other):
        if not isinstance(other, Abono):
            return NotImplemented
        return self.__tipo == other.tipo \
               and self.__fecha_activacion == other.fecha_activacion \
               and self.__fecha_cancelacion == other.fecha_cancelacion \
               and self.__caducidad == other.caducidad \
               and self.__cliente == other.cliente
