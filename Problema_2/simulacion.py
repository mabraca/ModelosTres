# -*- coding: utf-8 -*-
from __future__ import division

from aleatorio import (random_arrival_time, proximo_evento, random_service_time,
                       random_decline)
from cajero import Cajero, cajero_con_menos_cola
from commons.cola import Cola
from persona import Persona


def iniciar_simulacion(maximo_de_tiempo, maximo_servidores):
    

    cola_por_atender = Cola()

    tiempo_actual = 0
    personas_que_declinaron = 0
    lista_cajeros = maximo_servidores * [Cajero()]
    personas_fuera_del_sistema = []


    for i in range(maximo_servidores):
        lista_cajeros[i] = Cajero()
        
    proxima_llegada = random_arrival_time()

    # SIMULACION
    while (tiempo_actual < maximo_de_tiempo or not Cajero.todos_servidores_disponibles(
            lista_cajeros) or cola_por_atender.tamano() > 0):
        servidor_recien_asignado = 10
    #     print "Tiempo Actual: %0.6f" % (tiempo_actual)
        # Verificamos cual es el evento mas proximo
        tiempo_para_evento = proximo_evento(
            proxima_llegada,
            lista_cajeros)
        if tiempo_para_evento == 0:
            print "Error tiempo para evento invalido"
            exit()
    #     print "El proximo evento ocurrira en %0.6f" % (tiempo_para_evento)
    #     print "En la cola inicial hay: %d" % (cola_por_llegar.tamano())
    #     print "En la cola de espera hay: %d" % (cola_por_atender.tamano())
        tiempo_actual += tiempo_para_evento
        # Manejamos las llegadas al sistema
        if proxima_llegada > 0:
            proxima_llegada -= tiempo_para_evento
            # Verificamos si un cliente ha llegado
            if proxima_llegada == 0:
                # Seleccionamos el cajero con menos cola
                cajero_seleccionado = cajero_con_menos_cola(lista_cajeros)
                # Si el cajero seleccionado esta vacio procedemos a atender
                if cajero_seleccionado.cola_por_atender.tamano() == 0:
                    cajero_seleccionado.tiempo_servicio = random_service_time()
                    cajero_seleccionado.persona_atendida = Persona()
                    cajero_seleccionado.disponible = False
                    servidor_recien_asignado = cajero_seleccionado
                # Si no esta vacia pero la cola es corta entonces lo encolamos en
                # el cajero
                elif cajero_seleccionado.cola_por_atender.tamano() < 6:
                    cajero_seleccionado.cola_por_atender.encolar(
                        Persona())
                #
                else:
                    personas_que_declinaron = random_decline(
                        cajero_seleccionado.cola_por_atender,
                        personas_que_declinaron,
                        personas_fuera_del_sistema)
                    
                proxima_llegada = random_arrival_time()
        # Manejo de servidores
        for i in range(maximo_servidores):
            if (lista_cajeros[i].tiempo_servicio > 0
                    and not lista_cajeros[i].disponible
                    and servidor_recien_asignado != lista_cajeros[i]):
                # Disminuimos el tiempo de servicio restante para el cliente
                # actual
                lista_cajeros[i].tiempo_servicio -= tiempo_para_evento
                # Le sumamos tiempo de servicio al cajero
                lista_cajeros[i].tiempo_servicio_total += tiempo_para_evento
                # Le sumamos tiempo de sistema a la persona siendo atendida por el
                # cajero
                lista_cajeros[i].persona_atendida.tiempo_sistema += tiempo_para_evento
                # Verificamos si el cajero termino te atender a alguien
                if lista_cajeros[i].tiempo_servicio == 0:
                    if lista_cajeros[i].cola_por_atender.tamano() > 0:
                        personas_fuera_del_sistema.append(
                            lista_cajeros[i].persona_atendida)
                        lista_cajeros[
                            i].persona_atendida = lista_cajeros[i].cola_por_atender.desencolar()
                        lista_cajeros[
                            i].tiempo_servicio = random_service_time()
                        lista_cajeros[i].disponible = False
                    else:
                        personas_fuera_del_sistema.append(
                            lista_cajeros[i].persona_atendida)
                        lista_cajeros[i].persona_atendida = None
                        lista_cajeros[i].disponible = True
        # Agregamos tiempo en el sistema a las personas en la cola
        for persona in cola_por_atender.items:
            persona.tiempo_sistema += tiempo_para_evento

    

    porcentaje_declinaron = (personas_que_declinaron * 100 / len(personas_fuera_del_sistema))
    tiempo_esperado_cliente = (Persona.tiempo_promedio_en_sistema(personas_fuera_del_sistema))
    porcentaje_tiempo_clista = []
    print "----------------------------------------------------------------"
    print "Analisis de resultados: "
    print "----------------------------------------------------------------"
    print "(a) El tiempo esperado que un cliente pasa en el sistema %0.2f minutos" % (tiempo_esperado_cliente)
    print "(b) Porcentaje de personas que declinaron  %0.2f" % (porcentaje_declinaron)
    print "(c) El porcentaje de tiempo desocupado de cada cajero"
    for i in range(maximo_servidores):
        tiempo_total = tiempo_actual - lista_cajeros[i].tiempo_servicio_total
        aux = (tiempo_total * 100 / tiempo_actual)
        porcentaje_tiempo_clista.append(aux)
        print "    Cajero %d: %0.6f" % (i, aux)
    print "---------------------------------------------------------------- "

    return [porcentaje_declinaron, tiempo_esperado_cliente, porcentaje_tiempo_clista[0],porcentaje_tiempo_clista[1],porcentaje_tiempo_clista[2],porcentaje_tiempo_clista[3]]