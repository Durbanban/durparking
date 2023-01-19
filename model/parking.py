class Parking:
    plazas = []
    def __init__(self, recaudacion, plazas = [], cobros = []):
        self.__recaudacion = recaudacion
        self.__plazas = plazas
        self.__cobros = cobros

    @property
    def plazas(self):
        return self.__plazas

    @plazas.setter
    def plazas(self, plazas):
        self.__plazas = plazas

    @property
    def cobros(self):
        return self.__cobros

    @cobros.setter
    def cobros(self, cobros):
        self.__cobros = cobros

    @property
    def recaudacion(self):
        return self.__recaudacion

    @recaudacion.setter
    def recaudacion(self, nueva_recaudacion):
        self.__recaudacion = nueva_recaudacion

    def addPlaza(self, plaza):
        self.__plazas.append(plaza)

    def addCobro(self, cobro):
        self.__cobros.append(cobro)


    def mostrar(self):
        for plaza in self.__plazas:
            print(f"PLAZA {self.__plazas.index(plaza) + 1}")
            print("=======================")
            print(plaza)
            print()


