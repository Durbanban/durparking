from model.parking import Parking
from model.plaza_parking import PlazaParking
from model.cliente import Cliente
from model.abono import Abono
from model.vehiculo import Vehiculo
from model.cliente_abonado import ClienteAbonado

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

    print("Leyenda: L = Libre, O = Ocupada, A = Plaza de abonado")

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
        if inicio < cobro.fecha < fin:
            cobros_objetivo.append(cobro)
            resultado += cobro.cantidad

    return cobros_objetivo, round(resultado, 2)

def obtener_abonos(abonos):

    resultado = 0

    for abono in abonos:
        resultado += abono.tarifa

    return round(resultado, 2)

def alta_abonado(abonado):
    pass

def modificacion_abonado:
    pass

def baja_abonado():
    pass

def caducidad_abonos_mes():
    pass

def caducidad_abonos_10_dias(abonos):
    resultados = []
    for abono in abonos:
        if date.today() - timedelta(days=10) < abono.fecha_cancelacion < date.today():
            resultados.append(abono)

    return resultados






















