from __future__ import division

from commons.estadistica import error_95_prcnt
from simulacion import iniciar_simulacion

def problema(numero_simulaciones):

    print "********************************** Problema 4 **********************************"
    print ""

    esperanzaFinal = 0
    maquinasFuncionando = 4
    maquinasRepuesto = 3
    esperanza = 0
    esperanzaArray = []

    print "------------------- Preparando la simulacion! ------------------"
    print "Parametros: "
    print "maquinasFuncionando %d" % (maquinasFuncionando)
    print "maquinasRepuesto    %d" % (maquinasRepuesto)

    print "------------------- Iniciando la simulacion! -------------------"
    print ""

    for i in range(numero_simulaciones):
        esperanza = iniciar_simulacion(maquinasFuncionando, maquinasRepuesto)
        esperanzaFinal += esperanza

        esperanzaArray.append(esperanza)

    esperanzaMedia = esperanzaFinal / numero_simulaciones

    m_error_95 = error_95_prcnt(esperanzaArray, esperanzaMedia)

    print "---------------- Se ha terminado la simulacion! ----------------"
    print "Analisis de resultados: "
    print "Tiempo de falla esperado del sistema: %0.2f horas" % (esperanzaMedia)
    print ""
    print "Intervalo de Confianza: "
    print "El intervalo de confianza de 95 por ciento esta entre (%f , %f)" % (esperanzaMedia - m_error_95, esperanzaMedia + m_error_95)
