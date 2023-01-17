from model.parking import Parking
from model.plaza_parking import PlazaParking
from model.cliente import Cliente
from model.abono import Abono
from model.vehiculo import Vehiculo

def mostrar_estado(parking: Parking):
    resultado = []
    for plaza in parking.plazas:
        print(plaza)
    return f"Existen {len(resultado)} plazas libres en el parking"