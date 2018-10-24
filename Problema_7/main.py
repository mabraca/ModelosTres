# *** coding: utf*8 ***
from __future__ import division

from simulacion import iniciar_simulacion
from commons.estadistica import error_95_prcnt

def problema(numero_simulaciones):

    print ""
    print "********************************** Problema 7 **********************************"
    print ""

    diasMax = 360
    Q = 100
    reorden = 0
    costoPorUnidad = 0

    print "------------------- Preparando la simulacion! ------------------"
    print "Parametros: "
    print "(a) diasMax %d" % (diasMax)
    print "(b) reordenCota %d" % (Q)
    print ""

    print "------------------- Iniciando la simulacion! -------------------"
    print ""

    reordenArray = []
    costoPorUnidadArray = []

    for i in range(numero_simulaciones):
        result = iniciar_simulacion(diasMax,Q)

        reorden += result[0]
        reordenArray.append(result[0])
        costoPorUnidad += result[1]
        costoPorUnidadArray.append(result[1])

    mediaReorden = reorden/numero_simulaciones
    mediaCostoPorUnidad = costoPorUnidad/numero_simulaciones
    m_error_95Reorden = error_95_prcnt( reordenArray, mediaReorden)
    m_error_95RostoPorUnidad = error_95_prcnt( costoPorUnidadArray, mediaCostoPorUnidad)

    print "---------------- Se ha terminado la simulacion! ----------------"
    print "Analisis de resultados: "
    print "(a) El punto de reorden optimo es %d unidades con costo $%d " % (mediaReorden, mediaCostoPorUnidad)
    print ""

    print "Intervalo de Confianza: "
    print ""
    print "El intervalo de confianza de 95 por ciento del punto de reorden optimo esta entre (%f , %f)" % (mediaReorden-m_error_95Reorden,mediaReorden+m_error_95Reorden)
    print "El intervalo de confianza de 95 por ciento de las unidades de costo esta entre (%f , %f)" % (mediaCostoPorUnidad-m_error_95RostoPorUnidad,mediaCostoPorUnidad+m_error_95RostoPorUnidad)
    print ""

