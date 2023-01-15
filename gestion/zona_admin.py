from model.parking import Parking
from model.plaza_parking import PlazaParking
from model.cliente import Cliente
from model.abono import Abono
from model.vehiculo import Vehiculo

def mostrar_estado(parking: Parking):
    return f"Existen {len(parking.plazas)} plazas en el parking"