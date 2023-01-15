class Parking:
    plazas = []
    def __init__(self, plazas = []):
        self.__plazas = plazas

    @property
    def plazas(self):
        return self.__plazas

    @plazas.setter
    def plazas(self, plazas):
        self.__plazas = plazas

    def addPlaza(self, plaza):
        self.__plazas.append(plaza)

    def mostrar(self):
        for plaza in self.__plazas:
            print(f"PLAZA {self.__plazas.index(plaza) + 1}")
            print("=======================")
            print(plaza)
            print()


