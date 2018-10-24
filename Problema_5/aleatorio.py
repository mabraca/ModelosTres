# -*- coding: utf-8 -*-
import random

from buque import Buque
from puerto import Puerto

CLIENTS_PER_HOUR = 60
UNIFORM_LOW = 3
UNIFORM_HIGH = 5


def random_arrival_time():
    random_number = random.random()    
    if 0 <= random_number and random_number <= 0.20:
        return 1
    elif 0.20 < random_number and random_number <= 0.45:
        return 2
    elif 0.45 < random_number and random_number <= 0.80:
        return 3
    elif 0.80 < random_number and random_number <= 0.95:
        return 4
    elif 0.95 < random_number and random_number <= 1.00:
        return 5
    
def random_boat_type():
    random_number = random.random()    
    if 0 <= random_number and random_number <= 0.40:
        return Buque(Buque.BOAT,random_arrival_time())
    elif 0.40 < random_number and random_number <= 0.75:
        return Buque(Buque.MEDIUM_BOAT,random_arrival_time())
    elif 0.75 < random_number and random_number <= 1.00:
        return Buque(Buque.SMALL_BOAT,random_arrival_time())


def proximo_evento(proxima_llegada, cajeros):
    servidores_validos = Puerto.tiempo_servicio_valido(
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
