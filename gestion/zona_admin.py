from model.parking import Parking
from model.plaza_parking import PlazaParking
from model.cliente import Cliente
from model.abono import Abono
from model.vehiculo import Vehiculo

def mostrar_estado(parking: Parking):
    resultado = []
    for plaza in parking.plazas:
        if plaza.libre:
            resultado.append(plaza)
    return f"Existen {len(parking.plazas)} plazas libres en el parking"