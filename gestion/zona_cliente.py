import pickle

from model.parking import Parking
from model.plaza_parking import PlazaParking
from model.cliente import Cliente
from model.abono import Abono
from model.vehiculo import Vehiculo
from model.ocupacion import Ocupacion
from model.cobro import Cobro
from datetime import datetime, timedelta

def depositar_vehiculo(matricula, opcion_tipo, plazas, clientes, ocupaciones, vehiculos):

    if opcion_tipo in [1, 2, 3]:
        if opcion_tipo == 1:
            tipo = "turismo"
        elif opcion_tipo == 2:
            tipo = "moto"
        elif opcion_tipo == 3:
            tipo = "movilidad"

    check_vehiculos = list(filter(lambda vehiculo: vehiculo.matricula == matricula, vehiculos))
    if len(check_vehiculos) > 0:
        vehiculo_cliente = check_vehiculos[0]
    elif len(check_vehiculos) == 0:
        vehiculo_cliente = Vehiculo(matricula, tipo)
        cliente = Cliente(len(clientes) + 1, vehiculo_cliente)
        vehiculo_cliente.owner = cliente

    check_plazas = list(filter(lambda plaza: plaza.tipo == vehiculo_cliente.tipo
                                             and plaza.libre
                                             and plaza.abonado is None, plazas))

    if len(check_plazas) > 0 and len(check_vehiculos) == 0:

        ocupacion = Ocupacion(datetime.now(), check_plazas[0], vehiculo_cliente)
        check_plazas[0].libre = False
        check_plazas[0].generar_pin()
        clientes.append(cliente)
        vehiculos.append(vehiculo_cliente)
        ocupaciones.append(ocupacion)

        with open("recursos/pickle/clientes.pckl", "wb") as fw:
            pickle.dump(clientes, fw)

        with open("recursos/pickle/vehiculos.pckl", "wb") as fw:
            pickle.dump(vehiculos, fw)

        with open("recursos/pickle/ocupaciones.pckl", "wb") as fw:
            pickle.dump(ocupaciones, fw)

        return ocupacion

    elif len(check_plazas) > 0 and len(check_vehiculos) > 0:

        ocupacion = Ocupacion(datetime.now(), check_plazas[0], vehiculo_cliente)
        check_plazas[0].libre = False
        check_plazas[0].generar_pin()
        ocupaciones.append(ocupacion)

        with open("recursos/pickle/ocupaciones.pckl", "wb") as fw:
            pickle.dump(ocupaciones, fw)

        return ocupacion


def retirar_vehiculo(matricula, plaza_cliente, pin, cobros, ocupaciones):

    check = list(filter(lambda ocupacion: ocupacion.plaza.id == plaza_cliente.id
                                          and not plaza_cliente.libre
                                          and ocupacion.vehiculo.matricula == matricula, ocupaciones))

    if len(check) > 0:
        intervalo = datetime.now() - check[0].fecha_deposito
        importe = round(plaza_cliente.tarifa * (intervalo.total_seconds() / 60), 2)
        cobro = Cobro(importe, datetime.now())
        cobros.append(cobro)

        plaza_cliente.libre = True
        plaza_cliente.pin = ''

        with open("recursos/pickle/cobros.pckl", "wb") as fw:
            pickle.dump(cobros, fw)

        return cobro


def depositar_vehiculo_abonado(abonado, plazas, ocupaciones):

    for plaza in plazas:
        if plaza.abonado is not None:
            if plaza.abonado.id == abonado.id:
                ocupacion = Ocupacion(datetime.now(), plaza, abonado.vehiculo)
                plaza.libre = False

    ocupaciones.append(ocupacion)


    with open("recursos/pickle/ocupaciones.pckl", "wb") as fw:
        pickle.dump(ocupaciones, fw)

    with open("recursos/pickle/plazas.pckl", "wb") as fw:
        pickle.dump(plazas, fw)

    return ocupacion

def retirar_vehiculo_abonado(matricula, plaza_abonado, pin, plazas, ocupaciones):

    flag = False

    for ocupacion in ocupaciones:
        if ocupacion.plaza.id == plaza_abonado.id\
                and not plaza_abonado.libre\
                and plaza_abonado.pin == pin\
                and ocupacion.vehiculo.matricula == matricula and not flag:
            o = ocupacion
            flag = True

    if flag:
        plaza_abonado.libre = True

    with open("recursos/pickle/plazas.pckl", "wb") as fw:
        pickle.dump(plazas, fw)

