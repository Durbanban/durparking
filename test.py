import calendar
from model.parking import Parking
from model.plaza_parking import PlazaParking
from model.cliente import Cliente
from model.vehiculo import Vehiculo
from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
import pickle
from io import open
from gestion import zona_admin, zona_cliente
import menu
from servicios.parking_servicio import ParkingService


vehiculo = Vehiculo("4545GZG", "turismo")
cliente = Cliente(1, vehiculo)
vehiculo.owner = cliente
service = ParkingService()

plaza_1 = PlazaParking(1, False, "turismo", 0.12)
plaza_2 = PlazaParking(2, True, "movilidad", 0.10)
plazas = [plaza_1, plaza_2]
parking = Parking(plazas)

for plaza in parking.plazas:
    if plaza.libre:
        print(plaza)
    else:
        print("Plaza no libre")
if plaza_1 == plaza_2:
    print("Son iguales")
else:
    print("No son iguales")

fw = open("recursos/pickle/test.pckl", "wb")
pickle.dump(plazas, fw)
fw.close()
#
# with open("recursos/pickle/test.pckl", "wb") as fw:
#     pickle.dump(plaz)

fr = open("recursos/pickle/test.pckl", "rb")
plazas_test = pickle.load(fr)
fr.close()

for item in plazas_test:
    print(item)




print(cliente)
print(cliente.vehiculo)

variable = service.find_plaza_by_id(2)
print(variable)