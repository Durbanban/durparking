import calendar
from model.parking import Parking
from model.plaza_parking import PlazaParking
from model.cliente import Cliente
from model.cliente_abonado import ClienteAbonado
from model.vehiculo import Vehiculo
from model.abono import Abono
from datetime import datetime, timedelta, date
from dateutil import relativedelta
from locale import setlocale, LC_ALL
import pickle
from io import open
from gestion import zona_admin, zona_cliente
import menu
from servicios.parking_servicio import ParkingService


with open("recursos/pickle/clientes.pckl", "rb") as fr:
    clientes = pickle.load(fr)

with open("recursos/pickle/vehiculos.pckl", "rb") as fr:
    vehiculos = pickle.load(fr)

with open("recursos/pickle/abonos.pckl", "rb") as fr:
    abonos = pickle.load(fr)

with open("recursos/pickle/plazas.pckl", "rb") as fr:
    plazas = pickle.load(fr)

with open("recursos/pickle/cobros.pckl", "rb") as fr:
    cobros = pickle.load(fr)

with open("recursos/pickle/ocupaciones.pckl", "rb") as fr:
    ocupaciones = pickle.load(fr)


for item in plazas:
    print(item)
