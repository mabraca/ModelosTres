from __future__ import division

from aleatorio import tiempo_de_falla, tiempo_de_reparacion
from commons.cola import Cola


def iniciar_simulacion(maquinas_funcionando, maquinas_repuesto):

    cola_maquina_repuesto = Cola()
    tiempo_en_fallar_maquina = [0] * 4
    tiempo_falla = 0
    tiempo_reparo = 0
    falla_sistema = False

    for i in range(maquinas_funcionando):
        tiempo_en_fallar_maquina[i] = tiempo_de_falla()

    while not falla_sistema:

        tiempo_falla += 1
        tiempo_reparo -= 1

        # Revisamos el estado de todas las maquinas
        for i in range(maquinas_funcionando):

            if tiempo_en_fallar_maquina[i] <= 0:
                # Si no hay repuesto la maquina falla
                if maquinas_repuesto <= 0:
                    falla_sistema = True
                else:
                    cola_maquina_repuesto.encolar(tiempo_de_reparacion())
                    maquinas_repuesto -= 1
                    tiempo_en_fallar_maquina[i] = tiempo_de_falla()

            tiempo_en_fallar_maquina[i] -= 1

        # Maquinas en Reparacion
        if tiempo_reparo <= 0:

            if tiempo_reparo == 0:
                maquinas_repuesto += 1

            if cola_maquina_repuesto.tamano() > 0:
                tiempo_reparo = cola_maquina_repuesto.primero()
                cola_maquina_repuesto.desencolar()
                if tiempo_reparo == 0:
                    maquinas_repuesto = 1

    print "----------------------------------------------------------------"
    print "----------------------- Resultados! ----------------------------"
    print "----------------------------------------------------------------"
    print "(a) El tiempo de falla: %0.2f " % (tiempo_falla)
    print "----------------------------------------------------------------"
    return tiempo_falla/10
