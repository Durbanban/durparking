class Vehiculo:

    def __init__(self, matricula, tipo, cliente=None):
        self.__matricula = matricula
        self.__tipo = tipo
        self.__owner = cliente

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, nueva_matricula):
        self.__matricula = nueva_matricula

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        if(nuevo_tipo in ["turismo", "moto", "movilidad"]):
            self.__tipo = nuevo_tipo
        else:
            print("Introduce un tipo de vehículo válido (turismo, moto, movilidad)")

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, new_owner):
        self.__owner = new_owner

    def __str__(self):
        return f"Matricula: {self.__matricula}\n" \
               f"Tipo: {self.__tipo}\n" \
               f"Dueño: {self.__owner.id}"

    def __eq__(self, other):
        if not isinstance(other, Vehiculo):
            return NotImplemented
        return self.__matricula == other.matricula \
               and self.__tipo == other.tipo \
               and self.__owner == other.__owner
