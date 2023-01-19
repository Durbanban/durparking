import pickle

from model.parking import Parking
from model.plaza_parking import PlazaParking
from model.cliente import Cliente
from model.abono import Abono
from model.vehiculo import Vehiculo
from model.cliente_abonado import ClienteAbonado
from model.cobro_abonado import CobroAbonado

from dateutil.relativedelta import relativedelta
from datetime import date, datetime, timedelta
from locale import setlocale, LC_ALL

setlocale(LC_ALL, 'es-ES')


def mostrar_estado(plazas):
    filas = []

    for plaza in plazas:
        if plaza.abonado is None and plaza.libre:
            if plaza.id <= 9:
                filas.append(f"  *******  \n  *  {plaza.id}  *  \n  *  L  *  \n  *     *  \n  *******  ")
            else:
                filas.append(f"  *******  \n  *  {plaza.id} *  \n  *  L  *  \n  *     *  \n  *******  ")
        elif plaza.abonado is None and not plaza.libre:
            if plaza.id <= 9:
                filas.append(f"  *******  \n  *  {plaza.id}  *  \n  *  O  *  \n  *     *  \n  *******  ")
            else:
                filas.append(f"  *******  \n  *  {plaza.id} *  \n  *  O  *  \n  *     *  \n  *******  ")
        elif plaza.abonado is not None and plaza.libre:
            if plaza.id <= 9:
                filas.append(f"  *******  \n  *  {plaza.id}  *  \n  *  L  *  \n  *  A  *  \n  *******  ")
            else:
                filas.append(f"  *******  \n  *  {plaza.id} *  \n  *  L  *  \n  *  A  *  \n  *******  ")
        elif plaza.abonado is not None and not plaza.libre:
            if plaza.id <= 9:
                filas.append(f"  *******  \n  *  {plaza.id}  *  \n  *  O  *  \n  *  A  *  \n  *******  ")
            else:
                filas.append(f"  *******  \n  *  {plaza.id} *  \n  *  O  *  \n  *  A  *  \n  *******  ")

    primera_fila = filas[:10]
    segunda_fila = filas[10:20]
    tercera_fila = filas[20:30]
    cuarta_fila = filas[30:40]

    for lines in zip(*map(str.splitlines, primera_fila)):
        print(*(line.ljust(5) for line in lines))
    for lines in zip(*map(str.splitlines, segunda_fila)):
        print(*(line.ljust(5) for line in lines))
    for lines in zip(*map(str.splitlines, tercera_fila)):
        print(*(line.ljust(5) for line in lines))
    for lines in zip(*map(str.splitlines, cuarta_fila)):
        print(*(line.ljust(5) for line in lines))

    print()
    print("Leyenda: L = Libre, O = Ocupada, A = Plaza de abonado")
    print()


def plazas_libres(plazas):
    turismos = 0
    motos = 0
    movilidades = 0
    for plaza in plazas:
        if plaza.tipo == "turismo" and plaza.abonado is None and plaza.libre:
            turismos += 1
        elif plaza.tipo == "moto" and plaza.abonado is None and plaza.libre:
            motos += 1
        elif plaza.tipo == "movilidad" and plaza.abonado is None and plaza.libre:
            movilidades += 1
    return turismos, motos, movilidades


def comprobar_abonado(dni, clientes):
    flag = False
    resultado = None
    for cliente in clientes:
        if not flag:
            if isinstance(cliente, ClienteAbonado):
                if cliente.dni == dni:
                    resultado = cliente
                    flag = True
    return flag, resultado


def obtener_facturacion(inicio, fin, cobros):

    cobros_objetivo = []
    resultado = 0

    for cobro in cobros:
        if not isinstance(cobro, CobroAbonado) and inicio < cobro.fecha < fin:
            cobros_objetivo.append(cobro)
            resultado += cobro.cantidad

    return cobros_objetivo, round(resultado, 2)


def obtener_abonos(abonos, cobros):

    resultado = 0
    cobros_abonados = []
    ab = []

    for abono in abonos:
        if abono.fecha_cancelacion > date.today():
            ab.append(abono)

    for cobro in cobros:
        if isinstance(cobro, CobroAbonado):
            cobros_abonados.append(cobro)
            resultado += cobro.cantidad

    return round(resultado, 2), cobros_abonados, ab


def alta_abonado(matricula, tipo_vehiculo, dni, nombre, tarjeta, email,
                 opcion_abono, plaza, vehiculos, clientes, abonos, cobros):

    vehiculo = Vehiculo(matricula, tipo_vehiculo)
    abonado = ClienteAbonado(len(clientes) + 1, vehiculo)
    vehiculo.owner = abonado
    abonado.dni = dni
    abonado.nombre = nombre
    abonado.tarjeta = tarjeta
    abonado.email = email
    if opcion_abono == 1:
        tipo_abono = "mensual"
        tarifa_abono = 25.0
        fecha_activacion = date.today()
        fecha_cancelacion = date.today() + relativedelta(months=1)
    elif opcion_abono == 2:
        tipo_abono = "trimestral"
        tarifa_abono = 70.0
        fecha_activacion = date.today()
        fecha_cancelacion = date.today() + relativedelta(months=3)
    elif opcion_abono == 3:
        tipo_abono = "semestral"
        tarifa_abono = 130.0
        fecha_activacion = date.today()
        fecha_cancelacion = date.today() + relativedelta(months=6)
    elif opcion_abono == 4:
        tipo_abono = "anual"
        tarifa_abono = 200.0
        fecha_activacion = date.today()
        fecha_cancelacion = date.today() + relativedelta(months=12)

    abono = Abono(tipo_abono, tarifa_abono, fecha_activacion, fecha_cancelacion, abonado)

    abonado.abono = abono

    plaza.abonado = abonado

    plaza.generar_pin()

    cobro = CobroAbonado(abono.tarifa, datetime.now())
    cobro.abonado = abonado

    clientes.append(abonado)
    vehiculos.append(vehiculo)
    abonos.append(abono)
    cobros.append(cobro)


    with open("recursos/pickle/clientes.pckl", "wb") as fw:
        pickle.dump(clientes, fw)

    with open("recursos/pickle/vehiculos.pckl", "wb") as fw:
        pickle.dump(vehiculos, fw)

    with open("recursos/pickle/abonos.pckl", "wb") as fw:
        pickle.dump(abonos, fw)

    with open("recursos/pickle/cobros.pckl", "wb") as fw:
        pickle.dump(cobros, fw)

    return abonado, plaza


def modificar_abonado(nombre, tarjeta, email, abonado):
    abonado.nombre = nombre
    abonado.tarjeta = tarjeta
    abonado.email = email


def renovar_abono(abonado, cobros):
    if abonado.abono.tipo == "mensual":
        renovacion = relativedelta(months=1)
    elif abonado.abono.tipo == "trimestral":
        renovacion = relativedelta(months=3)
    elif abonado.abono.tipo == "semestral":
        renovacion = relativedelta(months=6)
    elif abonado.abono.tipo == "anual":
        renovacion = relativedelta(months=12)

    abonado.abono.fecha_cancelacion += renovacion
    cobro = CobroAbonado(abonado.abono.tarifa, datetime.now())
    cobro.abonado = abonado

    cobros.append(cobro)

    with open("recursos/pickle/cobros.pckl", "wb") as fw:
        pickle.dump(cobros, fw)

    return cobro


def baja_abonado(abonado, vehiculos, abonos, clientes, plazas):
    vehiculo = abonado.vehiculo
    abono = abonado.abono
    vehiculos.remove(vehiculo)
    abonos.remove(abono)
    for plaza in plazas:
        if plaza.abonado is not None:
            if plaza.abonado.id == abonado.id:
                plaza_abonado = plaza
    plaza_abonado.borrar_abonado()
    plaza_abonado.pin = ''
    if not plaza_abonado.libre:
        plaza_abonado.libre = True
    flag = False
    for cliente in clientes:
        if not flag:
            if cliente == abonado:
                flag = True
        else:
            cliente.id = cliente.id - 1

    clientes.remove(abonado)

    with open("recursos/pickle/vehiculos.pckl", "wb") as fw:
        pickle.dump(vehiculos, fw)

    with open("recursos/pickle/abonos.pckl", "wb") as fw:
        pickle.dump(abonos, fw)

    with open("recursos/pickle/clientes.pckl", "wb") as fw:
        pickle.dump(clientes, fw)


def caducidad_abonos_mes(abonos, mes):
    resultados = []
    for abono in abonos:
        if abono.fecha_cancelacion.month == mes:
            resultados.append(abono)

    return resultados


def caducidad_abonos_10_dias(abonos):
    resultados = []
    for abono in abonos:
        if abono.caducidad <= timedelta(days=10):
            resultados.append(abono)

    return resultados

