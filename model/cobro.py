from locale import setlocale, LC_ALL

setlocale(LC_ALL, 'es-ES')


class Cobro:
    def __init__(self, cantidad, fecha):
        self.__cantidad = cantidad
        self.__fecha = fecha

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, nueva_fecha):
        self.__fecha = nueva_fecha

    def __str__(self):
        return f"Cantidad: {self.__cantidad} €\n" \
               f"Fecha: {self.__fecha.strftime('%A %d de %B de %Y a las %I:%M:%S')}"