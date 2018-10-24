'''
Created on Feb 12, 2017

@author: francisco
'''
from commons.servidor import Servidor
class Centro(Servidor):
    @staticmethod
    def tiempo_servicio_valido(servidors):
        lista = []
        
        if not servidors[0].disponible and servidors[1].cola_por_atender.tamano() < 4:
            lista.append(servidors[0].tiempo_servicio)
            
        if not servidors[1].disponible :
            lista.append(servidors[1].tiempo_servicio)
        return lista