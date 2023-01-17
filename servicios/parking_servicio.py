from model.parking import Parking
from model.plaza_parking import PlazaParking
from model.cliente_abonado import ClienteAbonado
from repositorios.parking_repository import cargar_plazas, \
    cargar_vehiculos,\
    cargar_clientes,\
    cargar_abonos,\
    cargar_cobros



class ParkingService:

    def cargar_parking(self):
        plazas = cargar_plazas()
        vehiculos = cargar_vehiculos()
        clientes = cargar_clientes()
        abonos = cargar_abonos()
        cobros = cargar_cobros()

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

        for cliente, abono in zip(clientes_abonados, abonos):
            cliente.abono = abono
            abono.abonado = cliente


        for cliente, vehiculo in zip(clientes, vehiculos):
            cliente.vehiculo = vehiculo
            vehiculo.owner = cliente





        return plazas, vehiculos, clientes, abonos, cobros


    def find_plaza_by_id(self, id):
        return id
