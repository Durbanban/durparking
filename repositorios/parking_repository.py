import os.path

from model.parking import Parking
from model.plaza_parking import PlazaParking
import pickle
from os import path
from io import open



def cargar_parking():

    lista_plazas = []


    if os.path.isfile("recursos/pickle/plazas.pckl"):

        # fr = open("recursos/pickle/plazas.pckl", "rb")
        # lista_plazas = pickle.load(fr)
        # fr.close()

        with open("recursos/pickle/plazas.pckl", "rb") as fr:
            lista_plazas = pickle.load(fr)

        return lista_plazas
    else:

        for i in range(1, 41):
                if i <= 28:
                    plaza = PlazaParking(i, True, "turismo", 0.12)
                    lista_plazas.append(plaza)
                elif i <= 34:
                    plaza = PlazaParking(i, True, "moto", 0.08)
                    lista_plazas.append(plaza)
                else:
                    plaza = PlazaParking(i, True, "movilidad", 0.10)
                    lista_plazas.append(plaza)

        # fw = open("recursos/pickle/plazas.pckl", "wb")
        # pickle.dump(lista_plazas, fw)
        # fw.close()

        with open("recursos/pickle/plazas.pckl", "wb") as fw:
            pickle.dump(lista_plazas, fw)

        print(lista_plazas[0])

        return lista_plazas

