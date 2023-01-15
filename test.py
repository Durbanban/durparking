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


cliente = Cliente(1, vehiculo=Vehiculo)
vehiculo = Vehiculo("4545GZG", "turismo", cliente)

print(cliente)