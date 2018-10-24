# -*- coding: utf-8 -*-
# import numpy
import random

from cajero import Cajero
from Problema_1.persona import Persona
import numpy


CLIENTS_PER_HOUR = 60
UNIFORM_LOW = 3
UNIFORM_HIGH = 5


def random_arrival_time():
	return numpy.random.exponential(scale=1)

def random_service_time():
	return numpy.random.uniform(low=UNIFORM_LOW, high=UNIFORM_HIGH)
	

def random_decline(cola_por_atender, personas_que_declinaron,
                   personas_fuera_del_sistema):
    resp = random.random()
    if 6 <= cola_por_atender.tamano(
    ) and cola_por_atender.tamano() <= 8:
        if resp <= 0.20:
            personas_que_declinaron += 1
            personas_fuera_del_sistema.append(Persona())
        else:
            cola_por_atender.encolar(
                Persona())

    elif 9 <= cola_por_atender.tamano() and cola_por_atender.tamano() <= 10:
        if resp <= 0.40:
            personas_que_declinaron += 1
            personas_fuera_del_sistema.append(Persona())
        else:
            cola_por_atender.encolar(
                Persona())

    elif 11 <= cola_por_atender.tamano() and cola_por_atender.tamano() <= 14:
        if resp <= 0.60:
            personas_que_declinaron += 1
            personas_fuera_del_sistema.append(Persona())
        else:
            cola_por_atender.encolar(
                Persona())

    elif 15 <= cola_por_atender.tamano():
        if resp <= 0.80:
            personas_que_declinaron += 1
            personas_fuera_del_sistema.append(Persona())
        else:
            cola_por_atender.encolar(
                Persona())
    return personas_que_declinaron


def proximo_evento(proxima_llegada, cajeros):
    servidores_validos = Cajero.tiempo_servicio_valido(
        cajeros)
    if servidores_validos == [] and proxima_llegada == 0:
        print "Error"
        exit()
    if len(servidores_validos) > 0 and proxima_llegada is not None:
        if min(servidores_validos) == 0:
            print "Error"
            exit()
        if proxima_llegada <= min(servidores_validos):
            return proxima_llegada
        elif proxima_llegada > min(servidores_validos):
            return min(servidores_validos)
    elif proxima_llegada is None:
        return min(servidores_validos)
    else:
        return proxima_llegada
