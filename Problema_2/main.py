# -*- coding: utf-8 -*-
from simulacion import iniciar_simulacion
from commons.estadistica import error_95_prcnt

def problema(numero_simulaciones):

    print "********************************** Problema 2 **********************************"

    tiempoMax = 450
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
        cajero1Array.append(x[2])
        cajero2Array.append(x[3])
        cajero3Array.append(x[4])
        cajero4Array.append(x[5])
        promedioDeclinaron += x[0]
        promedioEsperanza += x[1]
        promedioCajero1 += x[2]
        promedioCajero2 += x[3]
        promedioCajero3 += x[4]
        promedioCajero4 += x[5]

    promedioDeclinaron /= numero_simulaciones
    promedioEsperanza /= numero_simulaciones
    promedioCajero1 /= numero_simulaciones
    promedioCajero2 /= numero_simulaciones
    promedioCajero3 /= numero_simulaciones
    promedioCajero4 /= numero_simulaciones
    
    m_error_95_decl = error_95_prcnt(
        declinaronArray,
        promedioDeclinaron)

    print ""
    print "El promedio de porcentaje de declinación TOTAL es: %0.2f" % (promedioDeclinaron)

    print "El intervalo de confianza de 95 por ciento de la declinación esta entre %f y %f" % (promedioDeclinaron - m_error_95_decl, promedioDeclinaron + m_error_95_decl)
    print ""

    m_error_95_esp = error_95_prcnt(
        esperanzaArray,
        promedioEsperanza)

    print ""
    print "El tiempo esperado que un cliente pasa en el sistema TOTAL es: %0.2f" % (promedioEsperanza)

    print "El intervalo de confianza de 95 por ciento de la esperanza esta entre %0.4f y %0.4f" % (promedioEsperanza - m_error_95_esp, promedioEsperanza + m_error_95_esp)
    print ""
    
    promedioCajerosTotal = [promedioCajero1,
                                     promedioCajero2,
                                     promedioCajero3,
                                     promedioCajero4]
    
    cajeros = [cajero1Array,
                     cajero2Array,
                     cajero3Array,
                     cajero4Array]
    for i in range(servidoresMax):
        m_error_95_esp = error_95_prcnt(
            lista_cajeros[i],
            promedioCajerosTotal[i])
            
        
        print ""
        print "El tiempo esperado de porcentaje de desocupacion del cajero %d TOTAL es: %0.2f" % (i,promedioCajerosTotal[i])
    
        print "El intervalo de confianza de 95 por ciento de este cajero esta entre %0.4f y %0.4f" % (promedioCajerosTotal[i] - m_error_95_esp, promedioCajerosTotal[i] + m_error_95_esp)
        print ""
        
    
