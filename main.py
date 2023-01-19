
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
from menu import mostrar_menu_cliente, mostrar_menu_administrador, mostrar_menu_login
from servicios.parking_servicio import ParkingService
from gestion.zona_cliente import depositar_vehiculo,\
    retirar_vehiculo,\
    depositar_vehiculo_abonado,\
    retirar_vehiculo_abonado
import threading
import time

service = ParkingService()

plazas, vehiculos, clientes, abonos, cobros, ocupaciones = service.cargar_parking()
def temporizador():
    while True:
        with open("recursos/pickle/plazas.pckl", "wb") as fw:
            pickle.dump(plazas, fw)
        with open("recursos/pickle/vehiculos.pckl", "wb") as fw:
            pickle.dump(vehiculos, fw)
        with open("recursos/pickle/clientes.pckl", "wb") as fw:
            pickle.dump(clientes, fw)
        with open("recursos/pickle/abonos.pckl", "wb") as fw:
            pickle.dump(abonos, fw)
        with open("recursos/pickle/cobros.pckl", "wb") as fw:
            pickle.dump(cobros, fw)
        with open("recursos/pickle/ocupaciones.pckl", "wb") as fw:
            pickle.dump(ocupaciones, fw)
        time.sleep(120)

target = threading.Thread(target=temporizador)
target.start()



setlocale(LC_ALL, 'es-ES')

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

# for abono in abonos:
#     print(abono)
#
# for cliente in clientes:
#     print(type(cliente))
#
#
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

for ocupacion in ocupaciones:
    print(ocupacion)

for plaza in plazas:
    print(plaza)








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



mostrar_menu_login()
opcion_login = int(input())

while opcion_login != 0:
    if opcion_login == 1: # ZONA CLIENTE
        mostrar_menu_cliente()
        opcion_cliente = int(input())
        while opcion_cliente != 0:

            if opcion_cliente == 1:
                zona_admin.mostrar_estado(plazas)
                libres_turismo, libres_moto, libres_movilidad = zona_admin.plazas_libres(plazas)
                print(f"Actualmente quedan {libres_turismo} plazas libres para turismos, "
                      f"{libres_moto} plazas libres para motocicletas, "
                      f"y {libres_movilidad} plazas libres para movilidad reducida")
                matricula_deposito = input("Introduzca la matrícula de su vehículo: ")
                print("Introduzca el tipo del vehículo: ")
                print("1 para turismo")
                print("2 para motocicleta")
                print("3 para movilidad reducida")
                opcion_tipo = int(input())
                if opcion_tipo in [1, 2, 3]:
                    ticket, plazas, ocupaciones, clientes, vehiculos = depositar_vehiculo(matricula_deposito, opcion_tipo,
                                                        plazas, clientes, ocupaciones, vehiculos)
                    print(ticket)
                else:
                    print("Por favor, introduzca un número válido")

            elif opcion_cliente == 2:
                matricula = input("Introduzca la matrícula de su vehículo: ")
                flag = False
                for vehiculo in vehiculos:
                    if vehiculo.matricula == matricula and not flag:
                        vehiculo_cliente = vehiculo
                        flag = True
                if flag:
                    identificador = int(input("Introduzca el identificador de la plaza donde está estacionado su vehículo: "))
                    if 1 <= identificador <= 40:
                        plaza = plazas[identificador -1]
                        pin = input("Introduzca el pin asociado a dicha plaza: ")
                        if plaza.pin == pin:
                            if not plaza.libre:
                                cobro, cobros, plazas = retirar_vehiculo(matricula, plaza, pin, plazas, cobros, ocupaciones)
                                print(f"El importe es: {cobro.cantidad} €")
                            elif plaza.libre:
                                print("El vehículo no está estacionado en la plaza")
                        else:
                            print("PIN incorrecto. Inténtelo de nuevo")
                    else:
                        print("Lo sentimos, la plaza no existe")
                else:
                    print("Lo sentimos, esa matrícula no existe")

            elif opcion_cliente == 3:
                dni = input("Introduzca su dni: ")
                auth, abonado = zona_admin.comprobar_abonado(dni, clientes)
                if auth:
                    print(f"¡Bienvenido {abonado.nombre}!")
                    matricula = input("Introduzca la matrícula del vehículo: ")
                    flag = False
                    for vehiculo in vehiculos:
                        if vehiculo.matricula == matricula and not flag:
                            vehiculo_abonado = vehiculo
                            flag = True
                    flag_2 = False
                    for plaza in plazas:
                        if plaza.abonado is not None:
                            if plaza.abonado.id == abonado.id and plaza.libre:
                                flag_2 = True
                    if flag and flag_2:
                        ticket_abonado, plazas, ocupaciones = depositar_vehiculo_abonado(abonado, plazas, ocupaciones)
                        print(ticket_abonado)
                    elif not flag:
                        print("Lo sentimos, esa matrícula no existe")
                    elif not flag_2:
                        print(f"{abonado.nombre}, su plaza ya está ocupada")
                else:
                    print("Lo sentimos, no es usted abonado")

            elif opcion_cliente == 4:
                matricula = input("Introduzca la matrícula del vehículo: ")
                flag = False
                for vehiculo in vehiculos:
                    if vehiculo.matricula == matricula and not flag:
                        vehiculo_abonado = vehiculo
                        flag = True
                if flag:
                    identificador = int(input("Introduzca el identificador de la plaza donde está estacionado su vehículo"))
                    if 1 <= identificador <= 40:
                        plaza = plazas[identificador -1]
                        pin = input("Introduzca el pin asociado a dicha plaza: ")
                        if plaza.pin == pin:
                            if not plaza.libre:
                                plazas = retirar_vehiculo_abonado(matricula, plaza, pin, plazas, ocupaciones)
                                print
                            elif plaza.libre:
                                print("Su vehículo no está estacionado en la plaza")
                        else:
                            print("PIN incorrecto. Inténtelo de nuevo")
                    else:
                        print("Lo sentimos, la plaza no existe")
                else:
                    print("Lo sentimos esa matrícula no existe")

            else:
                print("Elija una opción correcta")

            mostrar_menu_cliente()
            opcion_cliente = int(input())

        print("Volviendo a menú login...")

    elif opcion_login == 2: # ZONA ADMIN
        mostrar_menu_administrador()
        opcion_admin = int(input())
        while opcion_admin != 0:

            if opcion_admin == 1:
                zona_admin.mostrar_estado(plazas)

            elif opcion_admin == 2:
                year_inicial = int(input("Introduzca el año de la fecha inicial: "))
                mes_inicial = int(input("Introduzca el mes del año: "))
                dia_inicial = int(input("Introduzca el día del mes: "))
                fecha_inicial = datetime(year_inicial, mes_inicial, dia_inicial, 0, 0, 0)

                year_final = int(input("Introduzca el año de la fecha final: "))
                mes_final = int(input("Introduzca el mes del año: "))
                dia_final = int(input("Introduzca el día del mes: "))
                fecha_final = datetime(year_final, mes_final, dia_final, 0, 0, 0)

                if fecha_inicial < fecha_final:
                    cobros_objetivo, importe = zona_admin.obtener_facturacion(fecha_inicial, fecha_final, cobros)
                    for cobro in cobros_objetivo:
                        print(cobro)
                    print(f"El importe total cobrado es de: {importe} €")
                else:
                    print("Lo sentimos. La fecha final no puede ser menor que la fecha inicial")

            elif opcion_admin == 3: # CONSULTAR ABONOS
                importe = zona_admin.obtener_abonos(abonos)
                print(f"El importe total de todos los abonos es: {importe} €")

            elif opcion_admin == 4: # DAR DE ALTA UN ABONO



                pass
                break

            elif opcion_admin == 5: # MODIFICAR UN ABONO
                pass
                break

            elif opcion_admin == 6: # DAR DE BAJA UN ABONO
                pass
                break

            elif opcion_admin == 7: # CADUCIDAD ABONOS MES
                pass
                break

            elif opcion_admin == 8: # CADUCIDAD ABONOS PRÓXIMOS 10 DÍAS
                abonos_10_dias = zona_admin.caducidad_abonos_10_dias(abonos)
                for abono in abonos_10_dias:
                    print(abono)

            else:
                print("Elija una opción correcta")

            mostrar_menu_administrador()
            opcion_admin = int(input())
        print("Volviendo a menú login...")
    else:
        print("Elija una opción correcta")
    mostrar_menu_login()
    opcion_login = int(input())


print("¡Vuelva pronto!")

