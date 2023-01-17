from model.parking import Parking
from model.plaza_parking import PlazaParking
from repositorios.parking_repository import cargar_parking



class ParkingService:

    def cargar_parking(self):
        plazas = cargar_parking()
        return plazas


    def find_plaza_by_id(self, id):
        return id
