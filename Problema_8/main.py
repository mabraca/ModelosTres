# *** coding: utf*8 ***
from __future__ import division

from simulacion import iniciar_simulacion
import math
from commons.estadistica import error_95_prcnt

def problema(numero_simulaciones=1):
    
    print "********************************** Problema 8 **********************************"
    print ""
    
    vendedores = 5
    promedio = 0
    ventasArray = []
    
    for i in range(numero_simulaciones):
        x = iniciar_simulacion(vendedores)
        ventasArray.append(x)
        promedio += x
    
    promedio /= numero_simulaciones
        
    m_error_95 = error_95_prcnt(ventasArray, promedio)
    
    print ""
    print "El promedio de ventas TOTAL es: %f" % (promedio)
    
    print "El intervalo de confianza de 95 por ciento esta entre %f y %f" % (promedio-m_error_95,promedio+m_error_95)
    print ""
