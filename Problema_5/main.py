# -*- coding: utf-8 -*-
from __future__ import division

from simulacion import iniciar_simulacion
from commons.estadistica import error_95_prcnt

def problema(numero_simulaciones=1):
    print "********************************** Problema 5 **********************************"
    print ""

    tiempoMax = 360
    lista_prombuque = []
    lista_promdiast = []
    lista_prct_desa = []
    lista_prct_desb = []
    prom_lista_prombuque = 0
    prom_lista_promdiast = 0
    prom_lista_prct_desa = 0
    prom_lista_prct_desb = 0

    print "------------------- Preparando la simulacion! ------------------"
    print "Parametros: "
    print "tiempoMax %d" % (tiempoMax)
    print ""

    for i in range(numero_simulaciones):
        x = iniciar_simulacion(tiempoMax)
        lista_prombuque.append(x[0])
        lista_promdiast.append(x[1])
        lista_prct_desa.append(x[2])
        lista_prct_desb.append(x[3])
        prom_lista_prombuque += x[0]
        prom_lista_promdiast += x[1]
        prom_lista_prct_desa += x[2]
        prom_lista_prct_desb += x[3]

    prom_lista_prombuque /= numero_simulaciones
    prom_lista_promdiast /= numero_simulaciones
    prom_lista_prct_desa /= numero_simulaciones
    prom_lista_prct_desb /= numero_simulaciones

    m_error_95_decl = error_95_prcnt(lista_prombuque, prom_lista_prombuque)

    print ""
    print "El promedio de buques tanque en el puerto TOTAL es: %0.2f" % (prom_lista_prombuque)

    print "El intervalo de confianza de 95 por ciento de los tanques en el puerto esta entre %f y %f" % (prom_lista_prombuque - m_error_95_decl, prom_lista_prombuque + m_error_95_decl)
    print ""

    m_error_95_decl = error_95_prcnt(lista_promdiast, prom_lista_promdiast)

    print ""
    print "El promedio de dias que pasa un buque tanque en el puerto TOTAL es: %0.2f" % (prom_lista_promdiast)

    print "El intervalo de confianza de 95 por ciento de los dias que pasa un buque tanque esta entre %f y %f" % (prom_lista_promdiast - m_error_95_decl, prom_lista_promdiast + m_error_95_decl)
    print ""

    m_error_95_decl = error_95_prcnt(lista_prct_desa, prom_lista_prct_desa)

    print ""
    print "El promedio de porcentaje de tiempo de desocupado del terminal A TOTAL es: %0.2f" % (prom_lista_prct_desa)

    print "El intervalo de confianza de 95 por ciento del tiempo de desocupado (A) esta entre %f y %f" % (prom_lista_prct_desa - m_error_95_decl, prom_lista_prct_desa + m_error_95_decl)
    print ""

    m_error_95_decl = error_95_prcnt(lista_prct_desb, prom_lista_prct_desb)

    print ""
    print "El promedio de porcentaje de tiempo de desocupado del terminal B es: %0.2f" % (prom_lista_prct_desb)

    print "El intervalo de confianza de 95 por ciento del tiempo de desocupado (B) esta entre %f y %f" % (prom_lista_prct_desb - m_error_95_decl, prom_lista_prct_desb + m_error_95_decl)
    print ""

