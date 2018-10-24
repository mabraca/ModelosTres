import numpy
import random
from commons.servidor import Servidor
from Problema_9.centro import Centro

CLIENTS_PER_HOUR = 60
UNIFORM_LOW = 6
UNIFORM_HIGH = 10

LEFT = 1
MODE = 3
RIGHT = 5

def proximo_evento(proxima_llegada, cajeros):
    servidores_validos = Centro.tiempo_servicio_valido(cajeros)

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

def random_arrival_time():
    return numpy.random.exponential(scale=12)

def random_cola():
    proc_cola = random.random()
    print proc_cola
    return 1

def random_service_time_A():
    return numpy.random.uniform(low=UNIFORM_LOW, high=UNIFORM_HIGH)
   
def random_service_time_B():
	return numpy.random.triangular(LEFT,MODE,RIGHT)