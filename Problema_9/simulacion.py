# -*- coding: utf-8 -*-
from __future__ import division

from commons.servidor import Servidor
from persona import Persona
from Problema_9.aleatorio import (proximo_evento, random_service_time_A,
    random_service_time_B, random_arrival_time)


def iniciar_simulacion(maximo_de_tiempo):

    personas_fuera_del_sistema = []
    lista_servidores = [Servidor(), Servidor()]
    centro_a = lista_servidores[0]
    centro_b = lista_servidores[1]
    tiempo_actual = 0
    numeros_de_trabajos = 0
    tiempo_interrupcion_A = 0
    tiempos_finalizacion_trabajo = []
    persona_recien_llegada_A = None
    persona_recien_llegada_B = None
    
    
    proxima_llegada = random_arrival_time() 

    while (tiempo_actual < maximo_de_tiempo or not Servidor.todos_servidores_disponibles(lista_servidores) or centro_b.cola_por_atender.tamano() > 0
           or not Servidor.todos_servidores_disponibles(lista_servidores) or centro_b.cola_por_atender.tamano() > 0):

        persona_recien_llegada_A = None
        persona_recien_llegada_B = None

        # print "Tiempo Actual: %0.6f" % (tiempo_actual)
        # Verificamos cual es el evento mas proximo
        tiempo_para_evento = proximo_evento(
            proxima_llegada,
            lista_servidores)

        if tiempo_para_evento == 0:
            print "Error tiempo para evento invalido"
            exit()

        tiempo_actual += tiempo_para_evento

        # Manejamos las llegadas al sistema
        proxima_llegada -= tiempo_para_evento
        # Verificamos si un cliente ha llegado
        if proxima_llegada == 0:
            # Si llego un cliente, no hay cola y hay servidor disponible, lo
            # aceptamos
            if centro_a.cola_por_atender.esta_vacia(
            ) and centro_a.disponible:
                # Encontramos el proximo servidor disponible
                centro_a.tiempo_servicio = random_service_time_A()
                centro_a.persona_atendida = Persona()
                centro_a.disponible = False
                persona_recien_llegada_A = centro_a.persona_atendida
            else:
                centro_a.cola_por_atender.encolar(
                    Persona())
                
            proxima_llegada = random_arrival_time()
        # Manejamos las llegadas de la cola A
        if (centro_a.persona_atendida and centro_a.persona_atendida !=
                persona_recien_llegada_A):
            #
            centro_a.persona_atendida.tiempo_sistema += tiempo_para_evento
            if centro_b.cola_por_atender.tamano() < 4:
                centro_a.tiempo_servicio -= tiempo_para_evento
                centro_a.tiempo_servicio_total += tiempo_para_evento
                if centro_a.tiempo_servicio == 0:
                #
                    if centro_b.cola_por_atender.esta_vacia(
                    ) and centro_b.disponible:
                        # Encontramos el proximo servidor disponible
                        centro_b.tiempo_servicio = random_service_time_B()
                        centro_b.persona_atendida = centro_a.persona_atendida
                        centro_b.disponible = False
                        persona_recien_llegada_B = centro_a.persona_atendida
                    else:
                        centro_b.cola_por_atender.encolar(
                            centro_a.persona_atendida)
                    #
                    if not centro_a.cola_por_atender.esta_vacia():
                        centro_a.persona_atendida = centro_a.cola_por_atender.desencolar()
                        centro_a.tiempo_servicio = random_service_time_A()
                        centro_a.disponible = False
                    else:
                        centro_a.persona_atendida = None
                        centro_a.disponible = True
            elif centro_b.cola_por_atender.tamano() >= 4:
                tiempo_interrupcion_A += tiempo_para_evento
            
                    
        # Manejamos las llegadas de la cola B
        if (centro_b.persona_atendida and centro_b.persona_atendida !=
                persona_recien_llegada_B):
            centro_b.tiempo_servicio -= tiempo_para_evento
            centro_b.tiempo_servicio_total += tiempo_para_evento
            centro_b.persona_atendida.tiempo_sistema += tiempo_para_evento
            if centro_b.tiempo_servicio == 0:
                tiempos_finalizacion_trabajo.append(centro_b.persona_atendida.tiempo_sistema)
                numeros_de_trabajos += 1
                if centro_b.cola_por_atender.tamano() > 0:
                    personas_fuera_del_sistema.append(
                        centro_b.persona_atendida)
                    centro_b.persona_atendida = centro_b.cola_por_atender.desencolar()
                    centro_b.tiempo_servicio = random_service_time_B()
                    centro_b.disponible = False
                else:
                    personas_fuera_del_sistema.append(
                        centro_b.persona_atendida)
                    centro_b.persona_atendida = None
                    centro_b.disponible = True
                
                
    p_desocupado_a = (
        tiempo_actual -
        lista_servidores[0].tiempo_servicio_total)
    p_desocupado_b = (
        tiempo_actual -
        lista_servidores[1].tiempo_servicio_total)
    esperanza_terminacion_trabajo = reduce(lambda x, y: x + y, tiempos_finalizacion_trabajo) / len(tiempos_finalizacion_trabajo)
    
    
    print "----------------------------------------------------------------"
    print "Analisis de resultados: "
    print "----------------------------------------------------------------"
    print "(a) El número esperado de trabajos en el taller en cualquier momento: %0.2f" % (numeros_de_trabajos)
    print "(c) El porcentaje de tiempo que se para el centro A por falta de espacio en la cola del centro B %0.2f" % (tiempo_interrupcion_A)
    print "(c) El tiempo esperado de terminación de un trabajo: %0.2f" % (esperanza_terminacion_trabajo)
    print "(d) El porcentaje de tiempo desocupado de cada terminal"
    print "    Terminal A: %0.6f" % (p_desocupado_a)
    print "    Terminal B: %0.6f" % (p_desocupado_b)
    print "---------------------------------------------------------------- "

    return [numeros_de_trabajos, tiempo_interrupcion_A, esperanza_terminacion_trabajo, p_desocupado_a, p_desocupado_b]
