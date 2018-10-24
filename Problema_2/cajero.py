from commons.cola import Cola
from commons.servidor import Servidor


class Cajero(Servidor):

    def __init__(self):
        self.disponible = True
        self.persona_atendida = None
        self.cola_por_atender = Cola()
        self.tiempo_servicio = 0
        self.tiempo_servicio_total = 0

    def __str__(self):
        return "Tiempo Servicio %0.6f - Disponible %b" % (
            self.tiempo_servicio, self.disponible)

    def __unicode__(self):
        return "Tiempo Servicio %0.6f - Disponible %b" % (
            self.tiempo_servicio, self.disponible)


def cajero_con_menos_cola(lista_cajeros):
    min_cajero_cola = lista_cajeros[0]
    for cajero in lista_cajeros:
        if cajero.cola_por_atender.tamano() < min_cajero_cola.cola_por_atender.tamano():
            min_cajero_cola = cajero
        elif (cajero.cola_por_atender.tamano() == min_cajero_cola.cola_por_atender.tamano() and
              cajero.persona_atendida is None and min_cajero_cola.persona_atendida is not None):
            min_cajero_cola = cajero
    return min_cajero_cola
