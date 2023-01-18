from model.parking import Parking
from model.plaza_parking import PlazaParking
from model.cliente_abonado import ClienteAbonado
from datetime import datetime
from repositorios.parking_repository import cargar_plazas, \
    cargar_vehiculos,\
    cargar_clientes,\
    cargar_abonos,\
    cargar_cobros,\
    cargar_ocupaciones

class ParkingService:

    def cargar_parking(self):
        plazas = cargar_plazas()
        vehiculos = cargar_vehiculos()
        clientes = cargar_clientes()
        abonos = cargar_abonos()
        cobros = cargar_cobros()
        ocupaciones = cargar_ocupaciones()

        clientes_abonados = []

        for cliente in clientes:
            if isinstance(cliente, ClienteAbonado):
                clientes_abonados.append(cliente)

        clientes_abonados[0].dni = "54687653Q"
        clientes_abonados[1].dni = "65887410L"
        clientes_abonados[2].dni = "99874102H"
        clientes_abonados[3].dni = "44147885F"

        clientes_abonados[0].nombre = "Pepito Pérez"
        clientes_abonados[1].nombre = "Miguel Campos"
        clientes_abonados[2].nombre = "Vlad Mihalcea"
        clientes_abonados[3].nombre = "Guido Van Rossum"

        clientes_abonados[0].tarjeta = "1234 5465 5478 5495"
        clientes_abonados[1].tarjeta = "6698 5547 5589 6652"
        clientes_abonados[2].tarjeta = "2254 8256 4287 8877"
        clientes_abonados[3].tarjeta = "63325 89987 1325 3214"

        clientes_abonados[0].email = "hola_soy_pepito@gmail.com"
        clientes_abonados[1].email = "miguel.campos@triana.salesianos.edu"
        clientes_abonados[2].email = "backend_master@jpa.com"
        clientes_abonados[3].email = "python.van.rossum@hotmail.com"



        for cliente, abono in zip(clientes_abonados, abonos):
            cliente.abono = abono
            abono.abonado = cliente

        plazas[5].abonado = clientes_abonados[0]
        plazas[5].generar_pin()
        plazas[15].abonado = clientes_abonados[1]
        plazas[15].generar_pin()
        plazas[25].abonado = clientes_abonados[2]
        plazas[25].generar_pin()
        plazas[35].abonado = clientes_abonados[3]
        plazas[35].generar_pin()

        for cliente, vehiculo in zip(clientes, vehiculos):
            cliente.vehiculo = vehiculo
            vehiculo.owner = cliente

        ocupaciones[0].plaza = plazas[5]
        ocupaciones[0].vehiculo = vehiculos[1]

        ocupaciones[1].plaza = plazas[8]
        ocupaciones[1].vehiculo = vehiculos[2]

        ocupaciones[2].plaza = plazas[3]
        ocupaciones[2].vehiculo = vehiculos[6]

        ocupaciones[3].plaza = plazas[31]
        ocupaciones[3].vehiculo = vehiculos[6]

        ocupaciones[4].plaza = plazas[38]
        ocupaciones[4].vehiculo = vehiculos[8]

        return plazas, vehiculos, clientes, abonos, cobros, ocupaciones

