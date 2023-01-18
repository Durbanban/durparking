from model.parking import Parking
from model.plaza_parking import PlazaParking
from model.cliente import Cliente
from model.abono import Abono
from model.vehiculo import Vehiculo
from model.ocupacion import Ocupacion
from model.cobro import Cobro
from datetime import datetime, timedelta

def depositar_vehiculo(matricula, tipo, plazas, clientes, ocupaciones):
    vehiculo = Vehiculo(matricula, tipo)
    cliente = Cliente(len(clientes) + 1, vehiculo)
    vehiculo.owner = cliente

    flag = False

    for plaza in plazas:
        if plaza.tipo == tipo and plaza.pin == '' and not flag:
            plaza.generar_pin()
            ocupacion = Ocupacion(datetime.now(), plaza, vehiculo)
            ocupaciones.append(ocupacion)
            plaza.libre = False
            flag = True


    return ocupacion

def retirar_vehiculo(matricula, plaza_cliente, pin, plazas, cobros, ocupaciones):

    flag_2 = False

    for ocupacion in ocupaciones:
        if ocupacion.plaza.id == plaza_cliente.id and not plaza_cliente.libre:
            o = ocupacion
            flag_2 = True

    intervalo = datetime.now() - o.fecha_deposito
    importe = round(plaza_cliente.tarifa * (intervalo.total_seconds() / 60), 2)
    cobro = Cobro(importe, datetime.now())
    cobros.append(cobro)

    plaza_cliente.libre = True
    plaza_cliente.pin = ''

    return cobro





