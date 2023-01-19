import os.path

from model.parking import Parking
from model.plaza_parking import PlazaParking
from model.cliente import Cliente
from model.vehiculo import Vehiculo
from model.cliente_abonado import ClienteAbonado
from model.abono import Abono
from model.cobro import Cobro
from model.cobro_abonado import CobroAbonado
from model.ocupacion import Ocupacion
from datetime import date, datetime, timedelta

from dateutil.relativedelta import relativedelta
import pickle
from random import uniform, randrange
from io import open
from locale import setlocale, LC_ALL


setlocale(LC_ALL, 'es-ES')


def cargar_plazas():

    lista_plazas = []

    if os.path.isfile("recursos/pickle/plazas.pckl"):

        with open("recursos/pickle/plazas.pckl", "rb") as fr:
            lista_plazas = pickle.load(fr)

    else:

        for i in range(1, 41):
            if i <= 28:
                plaza = PlazaParking(i, True, "turismo", 0.12)
                lista_plazas.append(plaza)
            elif i <= 34:
                plaza = PlazaParking(i, True, "moto", 0.08)
                lista_plazas.append(plaza)
            else:
                plaza = PlazaParking(i, True, "movilidad", 0.10)
                lista_plazas.append(plaza)

        with open("recursos/pickle/plazas.pckl", "wb") as fw:
            pickle.dump(lista_plazas, fw)

    return lista_plazas


def cargar_vehiculos():

    lista_vehiculos = []

    if os.path.isfile("recursos/pickle/vehiculos.pckl"):
        with open("recursos/pickle/vehiculos.pckl", "rb") as fr:
            lista_vehiculos = pickle.load(fr)

    else:
        vehiculo_1 = Vehiculo("1234ASD", "turismo")
        vehiculo_2 = Vehiculo("4458FDA", "turismo")
        vehiculo_3 = Vehiculo("9891HGT", "turismo")
        vehiculo_4 = Vehiculo("7461BRA", "turismo")
        vehiculo_5 = Vehiculo("8788KJU", "turismo")
        vehiculo_6 = Vehiculo("7841GQA", "moto")
        vehiculo_7 = Vehiculo("6984JHG", "moto")
        vehiculo_8 = Vehiculo("6965FAS", "moto")
        vehiculo_9 = Vehiculo("5413MJH", "movilidad")
        vehiculo_10 = Vehiculo("8979JUU", "movilidad")

        lista_vehiculos = [vehiculo_1, vehiculo_2, vehiculo_3, vehiculo_4, vehiculo_5, vehiculo_6
                               , vehiculo_7, vehiculo_8, vehiculo_9, vehiculo_10]

        with open("recursos/pickle/vehiculos.pckl", "wb") as fw:
            pickle.dump(lista_vehiculos, fw)

    return lista_vehiculos

def cargar_clientes():

    lista_clientes = []

    if os.path.isfile("recursos/pickle/clientes.pckl"):

        with open("recursos/pickle/clientes.pckl", "rb") as fr:
            lista_clientes = pickle.load(fr)

    else:

        for i in range(1, 11):
            if i < 7:
                cliente = Cliente(i)
                lista_clientes.append(cliente)
            else:
                cliente = ClienteAbonado(i)
                lista_clientes.append(cliente)

        with open("recursos/pickle/clientes.pckl", "wb") as fw:
            pickle.dump(lista_clientes, fw)

    return lista_clientes

def cargar_abonos():

    lista_abonos = []

    if os.path.isfile("recursos/pickle/abonos.pckl"):

        with open("recursos/pickle/abonos.pckl", "rb") as fr:
            lista_abonos = pickle.load(fr)

    else:
        abono_1 = Abono("mensual", 25.0, date.today() - timedelta(days=24), ((date.today() - timedelta(days=24)) + relativedelta(months=1)))
        abono_2 = Abono("trimestral", 70.0, date.today(), (date.today() + relativedelta(months=3)))
        abono_3 = Abono("semestral", 130.0, date.today(), (date.today() + relativedelta(months=6)))
        abono_4 = Abono("anual", 200.0, date.today(), (date.today() + relativedelta(months=12)))

        lista_abonos=[abono_1, abono_2, abono_3, abono_4]

        with open("recursos/pickle/abonos.pckl", "wb") as fw:
            pickle.dump(lista_abonos, fw)

    return lista_abonos

def cargar_cobros():

    lista_cobros = []

    if os.path.isfile("recursos/pickle/cobros.pckl"):
        with open("recursos/pickle/cobros.pckl", "rb") as fr:
            lista_cobros = pickle.load(fr)

    else:
        for i in range(1, 25):
            cobro = Cobro(round(uniform(3.50, 25.60), 2),
            generar_fecha_aleatoria(datetime(2019, 1, 1, 8, 0, 0), datetime.now()))
            lista_cobros.append(cobro)

        cobro_1 = CobroAbonado(25.0, datetime.now() - timedelta(days=24))
        lista_cobros.append(cobro_1)
        cobro_2 = CobroAbonado(70.0, datetime.now())
        lista_cobros.append(cobro_2)
        cobro_3 = CobroAbonado(130.0, datetime.now())
        lista_cobros.append(cobro_3)
        cobro_4 = CobroAbonado(200.0, datetime.now())
        lista_cobros.append(cobro_4)

        with open("recursos/pickle/cobros.pckl", "wb") as fw:
            pickle.dump(lista_cobros, fw)

    return lista_cobros

def cargar_ocupaciones():

    lista_ocupaciones = []

    if os.path.isfile("recursos/pickle/ocupaciones.pckl"):
        with open("recursos/pickle/ocupaciones.pckl", "rb") as fr:
            lista_ocupaciones = pickle.load(fr)

    else:
        ocupacion_1 = Ocupacion(generar_fecha_aleatoria(datetime(2019, 1, 1, 8, 0, 0), datetime.now()))
        ocupacion_2 = Ocupacion(generar_fecha_aleatoria(datetime(2019, 1, 1, 8, 0, 0), datetime.now()))
        ocupacion_3 = Ocupacion(generar_fecha_aleatoria(datetime(2019, 1, 1, 8, 0, 0), datetime.now()))
        ocupacion_4 = Ocupacion(generar_fecha_aleatoria(datetime(2019, 1, 1, 8, 0, 0), datetime.now()))
        ocupacion_5 = Ocupacion(generar_fecha_aleatoria(datetime(2019, 1, 1, 8, 0, 0), datetime.now()))

        lista_ocupaciones = [ocupacion_1, ocupacion_2, ocupacion_3, ocupacion_4, ocupacion_5]

        with open("recursos/pickle/ocupaciones.pckl", "wb") as fw:
            pickle.dump(lista_ocupaciones, fw)

    return lista_ocupaciones

def generar_fecha_aleatoria(inicio, fin):
    delta = fin - inicio
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return inicio + timedelta(seconds=random_second)
