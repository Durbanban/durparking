from model.cliente import Cliente


class ClienteAbonado(Cliente):

    __dni = ''
    __nombre = ''
    __tarjeta = ''
    __abono = None

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, nuevo_dni):
        if len(nuevo_dni) == 9:
            self.__dni = nuevo_dni
        else:
            print("Introduce un dni válido (9 caracteres)")

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if(type(nuevo_nombre) == str):
            self.__nombre = nuevo_nombre

    @property
    def tarjeta(self):
        return self.__tarjeta

    @tarjeta.setter
    def tarjeta(self, nueva_tarjeta):
        if type(nueva_tarjeta == str and len(nueva_tarjeta) == 16):
            self.__tarjeta = nueva_tarjeta
        else:
            print("Introduce un número de tarjeta válido (16 caracteres)")

    @property
    def abono(self):
        return self.__abono

    @abono.setter
    def abono(self, nuevo_abono):
        self.__abono = nuevo_abono

    def __str__(self):
        return f"Id: {self.id}\n" \
               f"Tipo de vehículo: {self.vehiculo.tipo}\n" \
               f"Dni: {self.__dni}\n" \
               f"Nombre: {self.__nombre}\n" \
               f"Número de tarjeta: {self.__tarjeta}\n" \
               f" Tipo de abono: {self.__abono.tipo}"

