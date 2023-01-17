
import calendar
from model.parking import Parking
from model.plaza_parking import PlazaParking
from model.cliente import Cliente
from model.vehiculo import Vehiculo
from model.cliente_abonado import ClienteAbonado
from model.abono import Abono
from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
import pickle
from io import open
from gestion import zona_admin, zona_cliente
import menu
from servicios.parking_servicio import ParkingService
from repositorios.parking_repository import cargar_vehiculos, cargar_clientes
service = ParkingService()

setlocale(LC_ALL, 'es-ES')


plazas, vehiculos, clientes, abonos, cobros = service.cargar_parking()
# vehiculo = Vehiculo("5454HGF", "turismo")
# cliente = Cliente(1, vehiculo)
# abono = Abono("trimestral", datetime.now(), datetime.now() + timedelta(days=90))
# abonado = ClienteAbonado(1, vehiculo)
# abono.cliente = cliente
# vehiculo.owner = cliente
# abonado.dni = "45645645G"
# abonado.nombre= "Loquendo"
# abonado.tarjeta = "4444 4444 4444 4444"
# abonado.abono = abono

# print(vehiculo)
# print(abono)
# print(abonado)

for abono in abonos:
    print(abono)

for cliente in clientes:
    print(type(cliente))


for vehiculo, cliente in zip(vehiculos, clientes):
    print("VEHICULO")
    print("===============")
    print(vehiculo)
    print("===============")
    print("CLIENTE")
    print("===============")
    print(cliente)
    print("===============")

for cobro in cobros:
    print(cobro)




# print(calendar.month(2023, 1))
#
# plaza1 = PlazaParking(1, False)
# print(plaza1.isLibre)
#
# ahora = datetime.now()
#
# un_dia = timedelta(days=0, hours=24, minutes=0)
#
# tomorrow = ahora + un_dia
#
# print(ahora.strftime("%A %d de %B de %Y a las %I:%M:%S"))
#
# print(tomorrow.strftime("%A %d de %B de %Y a las %I:%M:%S"))


menu.mostrar_menu_login()
opcion_login = int(input())

while opcion_login != 0:
    if opcion_login == 1: # ZONA CLIENTE
        menu.mostrar_menu_cliente()
        opcion_cliente = int(input())
        while opcion_cliente != 0:
            if opcion_cliente == 1:
                break
        print("Volviendo a menú login...")
    elif opcion_login == 2: # ZONA ADMIN
        menu.mostrar_menu_administrador()
        opcion_admin = int(input())
        while opcion_admin != 0:
            if opcion_admin == 1:
                print(zona_admin.mostrar_estado(parking))
                menu.mostrar_menu_administrador()
                opcion_admin = int(input())
            elif opcion_admin == 2: # COMPROBAR FACTURACIÓN
                break
            elif opcion_admin == 3: # CONSULTAR ABONOS
                break
            elif opcion_admin == 4: # DAR DE ALTA UN ABONO
                break
            elif opcion_admin == 5: # MODIFICAR UN ABONO
                break
            elif opcion_admin == 6: # DAR DE BAJA UN ABONO
                break
            elif opcion_admin == 7: # CADUCIDAD ABONOS MES
                break
            elif opcion_admin == 8: # CADUCIDAD ABONOS PRÓXIMOS 10 DÍAS
                break
        print("Volviendo a menú login...")
    menu.mostrar_menu_login()
    opcion_login = int(input())


print("¡Vuelva pronto!")

