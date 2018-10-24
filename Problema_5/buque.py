from __future__ import division
from commons.usuario import Usuario


class Buque(Usuario):
    
    BOAT = 'buque'
    MEDIUM_BOAT = 'buque mediano'
    SMALL_BOAT = 'buque pequeno'

    def __init__(self, tipo, llegada=0):
        self.tipo = tipo
        self.tiempo_sistema = 0
        self.tiempo_llegada = llegada


