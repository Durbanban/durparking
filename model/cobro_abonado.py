from locale import setlocale, LC_ALL
from model.cobro import Cobro

setlocale(LC_ALL, 'es-ES')

class CobroAbonado(Cobro):

    __abonado = None

    @property
    def abonado(self):
        return self.__abonado

    @abonado.setter
    def abonado(self, nuevo_abonado):
        self.__abonado = nuevo_abonado

    def __str__(self):
        return f"Cantidad: {self.cantidad} €\n" \
               f"Fecha: {self.fecha.strftime('%A %d de %B de %Y a las %I:%M:%S')}\n" \
               f"Nombre abonado: {self.__abonado.nombre}\n" \
               f"Dni abonado: {self.__abonado.dni}"