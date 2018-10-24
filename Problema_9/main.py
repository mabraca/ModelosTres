from simulacion import iniciar_simulacion
from commons.estadistica import error_95_prcnt


def problema(numero_simulaciones=1):

    print "********************************** Problema 9 **********************************"
    print ""

    tiempoMax = 2000
    cantidadTrabajosArray = []
    AInterrumpeArray = []
    esperanzaTrabajoArray = []
    promedioNumeroTrabajos = 0
    promedioInterrupcionesA = 0
    promedioEsperanzaTrabajo = 0

    print "------------------- Preparando la simulacion! ------------------"
    print "Parametros: "
    print "(a) maximo_de_tiempo %d" % (maximo_de_tiempo)

    for i in range(numero_simulaciones):
        x = iniciar_simulacion(maximo_de_tiempo)
        cantidadTrabajosArray.append(x[0])
        AInterrumpeArray.append(x[1])
        esperanzaTrabajoArray.append(x[2])
        promedioNumeroTrabajos += x[0]
        promedioInterrupcionesA += x[1]
        promedioEsperanzaTrabajo += x[2]


    promedioNumeroTrabajos /= numero_simulaciones
    promedioInterrupcionesA /= numero_simulaciones
    promedioEsperanzaTrabajo /= numero_simulaciones


    m_error_95_decl = error_95_prcnt(cantidadTrabajosArray, promedioNumeroTrabajos)

    print ""
    print "El promedio de trabajos en el taller es: %0.2f" % (promedioNumeroTrabajos)

    print "El intervalo de confianza de 95 por ciento del promedio de trabajos esta entre %f y %f" % (promedioNumeroTrabajos - m_error_95_decl, promedioNumeroTrabajos + m_error_95_decl)
    print ""

    m_error_95_decl = error_95_prcnt(AInterrumpeArray, promedioInterrupcionesA)

    print ""
    print "El promedio del porcentaje de tiempo que se para el A por falta de espacio en B es: %0.2f" % (promedioInterrupcionesA)

    print "El intervalo de confianza de 95 por ciento de este porcentaje esta entre %f y %f" % (promedioInterrupcionesA - m_error_95_decl, promedioInterrupcionesA + m_error_95_decl)
    print ""

    m_error_95_decl = error_95_prcnt(esperanzaTrabajoArray, promedioEsperanzaTrabajo)

    print ""
    print "El promedio esperado de la terminacion del trabajo es: %0.2f" % (promedioEsperanzaTrabajo)

    print "El intervalo de confianza de 95 por ciento de la terminacion del trabajo esta entre %f y %f" % (promedioEsperanzaTrabajo - m_error_95_decl, promedioEsperanzaTrabajo + m_error_95_decl)
    print ""


