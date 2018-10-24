# -*- coding: utf-8 -*-
from __future__ import division

from simulacion import iniciar_simulacion
from commons.estadistica import error_95_prcnt

def problema(numero_simulaciones):

    print "********************************** Problema 1 **********************************"

    tiempoMax = 480
    servidoresMax = 4
    declinaronArray = []
    esperanzaArray = []
    promedioDeclinaron = 0
    promedioEsperanza = 0
    promedioCajero1 = 0
    promedioCajero2 = 0
    promedioCajero3 = 0
    promedioCajero4 = 0
    cajero1Array = []
    cajero2Array = []
    cajero3Array = []
    cajero4Array = []
    
    print "------------------- Preparando la simulacion! ------------------"
    print "Parametros: "
    print "tiempoMax %d" % (tiempoMax)
    print "servidoresMax %d" % (servidoresMax)
    print ""
    
    for i in range(numero_simulaciones):
        x = iniciar_simulacion(tiempoMax, servidoresMax)
        declinaronArray.append(x[0])
        esperanzaArray.append(x[1])
        promedioDeclinaron += x[0]
        promedioEsperanza += x[1]
        cajero1Array.append(x[2][0])
        cajero2Array.append(x[2][1])
        cajero3Array.append(x[2][2])
        cajero4Array.append(x[2][3])
        promedioCajero1 += x[2][0]
        promedioCajero2 += x[2][1]
        promedioCajero3 += x[2][2]
        promedioCajero4 += x[2][3]

    promedioDeclinaron /= numero_simulaciones
    promedioEsperanza /= numero_simulaciones    

    m_error_95_esp = error_95_prcnt(esperanzaArray, promedioEsperanza)

    print ""
    print "El tiempo esperado que un cliente pasa en el sistema es: %0.2f" % (promedioEsperanza)
    print "El intervalo de confianza de 95 por ciento de la esperanza esta entre %0.4f y %0.4f" % (promedioEsperanza-m_error_95_esp,promedioEsperanza+m_error_95_esp)

    m_error_95_decl = error_95_prcnt(declinaronArray, promedioDeclinaron)

    print ""
    print "El promedio de porcentaje en que declinaron es: %0.2f" % (promedioDeclinaron)
    print "El intervalo de confianza de 95 por ciento de la declinación esta entre %f y %f" % (promedioDeclinaron-m_error_95_decl,promedioDeclinaron+m_error_95_decl)


    promedioCajero1 /= numero_simulaciones 
    promedioCajero2 /= numero_simulaciones 
    promedioCajero3 /= numero_simulaciones 
    promedioCajero4 /= numero_simulaciones 

    m_error_95_cajero1 = error_95_prcnt(cajero1Array, promedioCajero1)
    m_error_95_cajero2 = error_95_prcnt(cajero2Array, promedioCajero2)
    m_error_95_cajero3 = error_95_prcnt(cajero3Array, promedioCajero3)
    m_error_95_cajero4 = error_95_prcnt(cajero4Array, promedioCajero4)

    print ""
    print "El intervalo de confianza de 95 por ciento del tiempo desocupado del :" 
    print "*primer cajero: (%f,%f)" % (promedioCajero1 - m_error_95_cajero1, promedioCajero1 + m_error_95_cajero1 )
    print "*segundo cajero: (%f,%f)" % (promedioCajero2 - m_error_95_cajero2, promedioCajero2 + m_error_95_cajero2 )
    print "*tercer cajero: (%f,%f)" % (promedioCajero3 - m_error_95_cajero3, promedioCajero3 + m_error_95_cajero3 )
    print "*cuarto cajero: (%f,%f)" % (promedioCajero4 - m_error_95_cajero4, promedioCajero4 + m_error_95_cajero4 )
    

