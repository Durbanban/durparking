from model.cliente import Cliente


class ClienteAbonado(Cliente):

    __dni = ''
    __nombre = ''
    __tarjeta = ''
    __email = ''
    __abono = None

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, nuevo_dni):
        self.__dni = nuevo_dni


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def tarjeta(self):
        return self.__tarjeta

    @tarjeta.setter
    def tarjeta(self, nueva_tarjeta):
        self.__tarjeta = nueva_tarjeta

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nuevo_email):
        self.__email = nuevo_email

    @property
    def abono(self):
        return self.__abono

    @abono.setter
    def abono(self, nuevo_abono):
        self.__abono = nuevo_abono

    def generar_abono(self, abono):
        self.__abono = abono

    def __str__(self):
        return f"Id: {self.id}\n" \
               f"Tipo de vehículo: {self.vehiculo.tipo}\n" \
               f"Dni: {self.__dni}\n" \
               f"Nombre: {self.__nombre}\n" \
               f"Número de tarjeta: {self.__tarjeta}\n" \
               f"Tipo de abono: {self.__abono.tipo}"

