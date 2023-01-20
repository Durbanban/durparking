
from datetime import datetime
from locale import setlocale, LC_ALL
import pickle
from io import open
from gestion import zona_admin
from model.cliente_abonado import ClienteAbonado
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

main_thread = threading.current_thread()


def temporizador():
    flag = False
    while not flag:

        sec = 1
        while sec < 300:
            if main_thread.is_alive():
                time.sleep(1)
                sec += 1

            else:
                sec = 999
                flag = True

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


target = threading.Thread(target=temporizador)
target.start()

setlocale(LC_ALL, 'es-ES')
mostrar_menu_login()
opcion_login = int(input())


while opcion_login != 0:
    if opcion_login == 1: # ZONA CLIENTE
        mostrar_menu_cliente()
        opcion_cliente = int(input())
        while opcion_cliente != 0:

            if opcion_cliente == 1: # DEPOSITAR VEHÍCULO
                ticket = None
                zona_admin.mostrar_estado(plazas)
                libres_turismo, libres_moto, libres_movilidad = zona_admin.plazas_libres(plazas)
                print(f"Actualmente quedan {libres_turismo} plazas libres para turismos, "
                      f"{libres_moto} plazas libres para motocicletas, "
                      f"y {libres_movilidad} plazas libres para movilidad reducida")
                matricula_deposito = input("Introduzca la matrícula de su vehículo: ")

                flag = False
                flag_2 = False
                while not flag and not flag_2:
                    for ocupacion in ocupaciones:
                        if not ocupacion.plaza.libre and ocupacion.vehiculo.matricula == matricula_deposito and not flag:
                            o = ocupacion
                            flag = True
                    flag_2 = True
                if not flag:
                    print("Introduzca el tipo del vehículo: ")
                    print("1 para turismo")
                    print("2 para motocicleta")
                    print("3 para movilidad reducida")
                    opcion_tipo = int(input())
                    while opcion_tipo not in [1, 2, 3]:
                        print("Por favor, introduzca un número válido")
                        opcion_tipo = int(input())

                    ticket = depositar_vehiculo(matricula_deposito, opcion_tipo,
                                                        plazas, clientes, ocupaciones, vehiculos)
                    if ticket is not None:
                        print(ticket)
                    else:
                        print("Lo sentimos, no existen plazas libres para su tipo de vehículo ahora mismo")
                else:
                    print(f"El vehículo con matrícula: {matricula_deposito} está en la plaza: {o.plaza.id}")


            elif opcion_cliente == 2: # RETIRAR VEHÍCULO
                cobro = None
                matricula = input("Introduzca la matrícula de su vehículo: ")
                check = list(filter(lambda vehiculo: vehiculo.matricula == matricula, vehiculos))
                if len(check) > 0:
                    identificador = int(input("Introduzca el id de la plaza donde está estacionado su vehículo: "))
                    if 1 <= identificador <= 40:
                        plaza_cliente = plazas[identificador -1]
                        check = list(filter(lambda plaza: plaza_cliente.abonado is not None, plazas))
                        if len(check) == 0:
                            pin = input("Introduzca el pin asociado a dicha plaza: ")
                            if plaza_cliente.pin == pin:
                                if not plaza_cliente.libre:
                                    cobro = retirar_vehiculo(matricula, plaza_cliente, pin, cobros, ocupaciones)
                                    if cobro is not None:
                                        print(f"El importe es: {cobro.cantidad} €")
                                    else:
                                        print("No se ha podido retirar el vehículo")
                                elif plaza.libre:
                                    print("El vehículo no está estacionado en la plaza")
                            else:
                                print("PIN incorrecto. Inténtelo de nuevo")
                        else:
                            print("Esa plaza pertenece a un cliente abonado")
                    else:
                        print("Lo sentimos, la plaza no existe")
                else:
                    print("Lo sentimos, esa matrícula no existe")

            elif opcion_cliente == 3: # DEPOSITAR VEHÍCULO ABONADO
                dni = input("Introduzca su dni: ")
                auth, abonado = zona_admin.comprobar_abonado(dni, clientes)
                if auth:
                    print(f"¡Bienvenido {abonado.nombre}!")
                    matricula = input("Introduzca la matrícula del vehículo: ")
                    check_vehiculos = list(filter(lambda vehiculo: vehiculo.matricula == matricula, vehiculos))
                    check_plazas = list(filter(lambda plaza: plaza.abonado is not None
                                                             and plaza.abonado.id == abonado.id
                                                             and plaza.libre, plazas))

                    if len(check_vehiculos) > 0 and len(check_plazas) > 0:
                        ticket_abonado = depositar_vehiculo_abonado(abonado, plazas, ocupaciones)
                    elif len(check_vehiculos) == 0:
                        print("Lo sentimos, esa matrícula no existe")
                    elif len(check_plazas) == 0:
                        print(f"{abonado.nombre}, su plaza ya está ocupada")
                else:
                    print("Lo sentimos, no es usted abonado")

            elif opcion_cliente == 4: # RETIRAR VEHÍCULO ABONADO
                matricula = input("Introduzca la matrícula del vehículo: ")
                flag = False
                for vehiculo in vehiculos:
                    if vehiculo.matricula == matricula and not flag:
                        vehiculo_abonado = vehiculo
                        flag = True
                if flag:
                    identificador = int(input("Introduzca el id de la plaza donde está estacionado su vehículo"))
                    if 1 <= identificador <= 40:
                        plaza = plazas[identificador -1]
                        pin = input("Introduzca el pin asociado a dicha plaza: ")
                        if plaza.pin == pin:
                            if not plaza.libre:
                                retirar_vehiculo_abonado(matricula, plaza, pin, plazas, ocupaciones)
                                print(f"Ya puede retirar su vehículo, {vehiculo_abonado.owner.nombre}")
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

            if opcion_admin == 1: # MOSTRAR ESTADO DE LAS PLAZAS
                zona_admin.mostrar_estado(plazas)

            elif opcion_admin == 2: # MOSTRAR FACTURACIÓN
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
                importe, cobros_abonados, abonos_sin_caducar = zona_admin.obtener_abonos(abonos, cobros)
                print("*********C*O*B*R*O*S*********")
                for cobro in cobros_abonados:
                    print(cobro)
                    print("****************************")
                print("*********A*B*O*N*O*S*********")
                for abono in abonos_sin_caducar:
                    print(abono)
                    print("******************************")
                print(f"El importe total de todos los abonos es: {importe} €")

            elif opcion_admin == 4: # DAR DE ALTA UN ABONO
                matricula = input("Introduzca la matrícula del vehículo del abonado: ")
                lista = list(filter(lambda cliente: isinstance(cliente, ClienteAbonado)
                                                    and cliente.vehiculo.matricula == matricula, clientes))
                if len(lista) == 0:
                    print("Introduzca el tipo del vehículo: ")
                    print("1 para turismo")
                    print("2 para motocicleta")
                    print("3 para movilidad reducida")
                    opcion_tipo = int(input())
                    while opcion_tipo not in [1, 2, 3]:
                        print("Por favor introduzca un número válido")
                        opcion_tipo = int(input())
                    if opcion_tipo == 1:
                        tipo_vehiculo = "turismo"
                    elif opcion_tipo == 2:
                        tipo_vehiculo = "moto"
                    elif opcion_tipo == 3:
                        tipo_vehiculo = "movilidad"
                    dni = input("Introduzca el dni del abonado: ")
                    lista = list(filter(lambda cliente: isinstance(cliente, ClienteAbonado) and cliente.dni == dni, clientes))
                    if len(lista) == 0:

                        nombre = input("Introduzca el nombre del abonado: ")
                        tarjeta = input("Introduzca el número de tarjeta del abonado")
                        email = input("Introduzca el email del abonado: ")
                        zona_admin.mostrar_estado(plazas)
                        id_plaza = int(input("Introduzca el identificador de la plaza asignada: "))
                        flag = False
                        while not flag:
                            for plaza in plazas:
                                if plaza.id == id_plaza:
                                    if plaza.tipo == tipo_vehiculo and plaza.libre and plaza.abonado is None and not flag:
                                        plaza_abonado = plaza
                                        flag = True
                            if not flag:
                                zona_admin.mostrar_estado(plazas)
                                print("La plaza con ese identificador no está disponible o no es de su tipo de vehículo")
                                id_plaza = int(input("Introduzca el identificador de la plaza asignada: "))

                        print("Introduzca el tipo de abono del abonado: ")
                        print("1 para el abono mensual (25 €)")
                        print("2 para el abono trimestral (70 €)")
                        print("3 para el abono semestral (130 €)")
                        print("4 para el abono anual (200 €)")
                        print("0 para abandonar el proceso (¡¡¡tieso alert!!!)")
                        opcion_abono = int(input())
                        while opcion_abono not in [1, 2, 3, 4, 0]:
                            print("Por favor, introduzca un número válido")
                            opcion_abono = int(input())
                        if opcion_abono != 0:
                            abonado, plaza_asignada, checker = zona_admin.alta_abonado(matricula, tipo_vehiculo, dni,
                                                                        nombre, tarjeta, email, opcion_abono,
                                                                        plaza_abonado, vehiculos, clientes, abonos, cobros)
                            if checker:
                                print(f"Asegúrese de que {abonado.nombre} conoce las normas del parking y"
                                      f" que el pin de la plaza es: {plaza_asignada.pin}")
                            else:
                                print("El tipo de vehículo no coincide con el vehículo del cliente")
                        else:
                            print("Abortando alta de abonado...")
                    else:
                        print("Ya existe un abonado con ese dni")

                else:
                    print("Ya existe un vehículo asociado a un abonado con ese dni")
            elif opcion_admin == 5: # RENOVAR ABONO
                dni_abonado = input("Introduzca el dni del abonado a renovar: ")
                flag = False
                for ab in abonados:
                    if ab.dni == dni_abonado:
                        abonado = ab
                        flag = True
                if flag:
                    cobro = zona_admin.renovar_abono(abonado, cobros)
                    print("Abono renovado con éxito")
                    print(f"{abonado.nombre} podrá disfrutar de su abono hasta {abonado.abono.fecha_cancelacion}")
                else:
                    print("Abonado no encontrado")
            elif opcion_admin == 6: # MODIFICAR DATOS PERSONALES ABONADO
                abonados = []
                for cliente in clientes:
                    if isinstance(cliente, ClienteAbonado):
                        abonados.append(cliente)
                        print(cliente)
                dni_abonado = input("Introduzca el dni del abonado a modificar: ")
                flag = False
                for ab in abonados:
                    if ab.dni == dni_abonado:
                        abonado = ab
                        flag = True
                if flag:
                    nombre = input("Introduzca el nuevo nombre del abonado: ")
                    tarjeta = input("Introuduzca el nuevo número de tarjeta del abonado: ")
                    email = input("Introduzca el nuevo email del abonado: ")
                    zona_admin.modificar_abonado(nombre, tarjeta, email, abonado)
                    print("Datos modificados con éxito")
                else:
                    print("Abonado no encontrado")

            elif opcion_admin == 7: # DAR DE BAJA UN ABONO
                dni = input("Introduzca el dni del abonado: ")
                auth, abonado = zona_admin.comprobar_abonado(dni, clientes)
                if auth:
                    zona_admin.baja_abonado(abonado, vehiculos, abonos, clientes, plazas)
                    print("Abonado borrado con éxito")
                else:
                    print("Abonado no encontrado")

            elif opcion_admin == 8: # CADUCIDAD ABONOS MES
                mes = int(input("Introduzca el mes del año que sea consultar: "))
                if mes in range(1, 13):
                    abonos_mes = zona_admin.caducidad_abonos_mes(abonos, mes)
                    if len(abonos_mes) == 0:
                        print("No hay ningún abono que caduque ese mes")
                    else:
                        for abono in abonos_mes:
                            print(abono)
                else:
                    print("Mes no válido, por favor, introduzca un mes del 1 al 12")

            elif opcion_admin == 9: # CADUCIDAD ABONOS PRÓXIMOS 10 DÍAS
                abonos_10_dias = zona_admin.caducidad_abonos_10_dias(abonos)
                if len(abonos_10_dias) == 0:
                    print("No hay ningún abono que caduque en los próximos 10 días")
                else:
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

