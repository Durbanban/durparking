from datetime import date


class Abono:
    def __init__(self, tipo, tarifa, fecha_activacion, fecha_cancelacion, abonado=None):
        self.__tipo = tipo
        self.__tarifa = tarifa
        self.__fecha_activacion = fecha_activacion
        self.__fecha_cancelacion = fecha_cancelacion
        self.__abonado = abonado
        self.__caducidad = self.__fecha_cancelacion - date.today()

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        self.__tipo = nuevo_tipo


    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def tarifa(self, nueva_tarifa):
        self.__tarifa = nueva_tarifa

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
        self.__fecha_cancelacion = nueva_fecha


    @property
    def caducidad(self):
        return self.__caducidad

    @property
    def abonado(self):
        return self.__abonado

    @abonado.setter
    def abonado(self, nuevo_abonado):
        self.__abonado = nuevo_abonado

    def __str__(self):
        return f"Tipo de abono: {self.__tipo}\n" \
               f"Tarifa: {self.__tarifa} €\n" \
               f"Fecha de activación: {self.__fecha_activacion}\n" \
               f"Fecha de cancelación: {self.__fecha_cancelacion}\nCaducidad: {self.__caducidad}\n" \
               f"Abonado: {self.__abonado.nombre}"

    def __eq__(self, other):
        if not isinstance(other, Abono):
            return NotImplemented
        return self.__tipo == other.tipo \
               and self.__fecha_activacion == other.fecha_activacion \
               and self.__fecha_cancelacion == other.fecha_cancelacion \
               and self.__caducidad == other.caducidad \
               and self.__abonado == other.abonado
