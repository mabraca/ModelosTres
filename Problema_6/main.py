from simulacion import iniciar_simulacion
from random import sample
from commons.estadistica import error_95_prcnt

def problema(numero_simulaciones):

    print "********************************** Problema 6 **********************************"
    print ""


    print "------------------- Preparando la simulacion! ------------------"
    print ""

    Nemb = [127,162,179,75,223,186,124,45,100,171,235,176,130,159,117,100,92,68,242,122,184,84,240,319,61,78,20,141,202, 
        213,204,360,169,206,326,210,335,233,102,243,135,310,138,95,216,99,346,220,191,230,219,225,271,270,110,305,157,
        128,163,90,148,70,40,80,105,159,141,150,164,200,213,195,134,141,107,177,109,48,145,114,400,212,258,198,229,175,
        199,177,194,185,303,335,310,104,374,190,211,160,138,227,122,230,97,166,232,187,212,125,119,90,286,310,115,277,
        189,159,266,170,28,141,155,309,152,122,262,111,254,124,138,190,136,110,396,96,86,111,81,226,50,134,131,120,112,
        140,280,145,208,333,250,221,318,120,72,166,194,87,94,170,65,190,359,312,205,77,197,359,174,140,167,181,143,99,
        297,92,246,211,275,224,171,290,291,220,239,126,89,66,35,26,129,234,181,180,58,40,54,123,78,319,389,121]

    
    tiempoFinal = 0
    promedioPasajeros = 0
    maximoPasajeros = 0
    tiempoArray = []
    promedioPasajerosArray = []
    maximoPasajerosArray = []

    print "------------------- Iniciando la simulacion! -------------------"
    print ""

    for i in range(numero_simulaciones):
        embarques = sample(Nemb, 9)
        result = iniciar_simulacion(embarques)

        tiempoFinal += result[0]
        promedioPasajeros += result[1]
        maximoPasajeros += result[2]

        tiempoArray.append(result[0])
        promedioPasajerosArray.append(result[1])
        maximoPasajerosArray.append(result[2])
    
    mediaTiempoFinal = tiempoFinal/numero_simulaciones
    mediaPromedioPasajeros = promedioPasajeros/numero_simulaciones
    mediaMaximoPasajeros = maximoPasajeros/numero_simulaciones

    m_error_95tiempoFinal = error_95_prcnt(tiempoArray, mediaTiempoFinal)
    m_error_95promedioPasajeros = error_95_prcnt(promedioPasajerosArray, mediaPromedioPasajeros)
    m_error_95maximoPasajeros = error_95_prcnt(maximoPasajerosArray, media_maximo_pasajero)

    print "---------------- Se ha terminado la simulacion! ----------------"
    print "Analisis de resultados: "
    print "(a) El tiempo total del recorrido en segundos: %0.2f " % (mediaTiempoFinal)
    print "(b) El nro de pasajeros promedio a bordo del tren es: %0.2f" % (mediaPromedioPasajeros)  
    print "(c) El nro maximo de pasajeros embarcados es: %d " % (media_maximo_pasajero)
    print ""
    print "Intervalo de Confianza: "
    print "El intervalo de confianza de 95 por ciento del tiempo total esta entre (%0.2f , %0.2f)" % (mediaTiempoFinal-m_error_95tiempoFinal,mediaTiempoFinal+m_error_95tiempoFinal)
    print "El intervalo de confianza de 95 por ciento del promedio de pasajeros esta entre (%0.2f , %0.2f)" % (mediaPromedioPasajeros-m_error_95promedioPasajeros,mediaPromedioPasajeros+m_error_95promedioPasajeros)
    print "El intervalo de confianza de 95 por ciento del maximo de pasajeros esta entre (%0.2f , %0.2f)" % (media_maximo_pasajero-m_error_95maximoPasajeros,media_maximo_pasajero+m_error_95maximoPasajeros)
    print ""
