
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

# fichero_plazas = open("recursos/pickle/plazas.pckl", "wb")
#
# pickle.dump(parking.plazas, fichero_plazas)
#
# fichero_plazas.close()

# for i in range(1, 41):
#     if(i <= 28):
#         plaza = PlazaParking(i, True, "turismo", 0.12)
#         parking.addPlaza(plaza)
#     elif(i <= 34):
#         plaza = PlazaParking(i, True, "moto", 0.08)
#         parking.addPlaza(plaza)
#     else:
#         plaza = PlazaParking(i, True, "movilidad", 0.10)
#         parking.addPlaza(plaza)

setlocale(LC_ALL, 'es-ES')

parking = Parking(plazas=[])


lista = (pickle.load(open("recursos/pickle/plazas.pckl", "rb")))

parking.plazas = lista

# open("recursos/pickle/plazas.pckl", "rb").close()

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

while(opcion_login != 0):
    if(opcion_login == 0):
        menu.mostrar_menu_login()
        opcion_login = int(input())
    if(opcion_login == 1):# ZONA CLIENTE
        menu.mostrar_menu_cliente()
        opcion_cliente = int(input())
        while(opcion_cliente != 0):
            if(opcion_cliente == 1):
                break

    elif(opcion_login == 2):
        menu.mostrar_menu_administrador()
        opcion_admin = int(input())
        while(opcion_admin != 0):
            if(opcion_admin == 1):
                print(zona_admin.mostrar_estado(parking))
                menu.mostrar_menu_administrador()
                opcion_admin = int(input())
            elif(opcion_admin == 2): # COMPROBAR FACTURACIÓN
                opcion_login == 0
                break
            elif(opcion_admin == 3): # CONSULTAR ABONOS
                break
            elif(opcion_admin == 4): # DAR DE ALTA UN ABONO
                break
            elif(opcion_admin == 5): # MODIFICAR UN ABONO
                break
            elif(opcion_admin == 6): # DAR DE BAJA UN ABONO
                break
            elif(opcion_admin == 7): # CADUCIDAD ABONOS MES
                break
            elif(opcion_admin == 8): # CADUCIDAD ABONOS PRÓXIMOS 10 DÍAS
                break
            elif(opcion_admin == 0):
                opcion_login == 0
                break




print("¡Vuelva pronto!")

