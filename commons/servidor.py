from cola import Cola


class Servidor:

    def __init__(self):
        self.disponible = True
        self.persona_atendida = None
        self.cola_por_atender = Cola()
        self.tiempo_servicio = 0
        self.tiempo_servicio_total = 0

    @staticmethod
    def existe_servidor_disponible(lista):
        for servidor in lista:
            if servidor.disponible:
                return True
        return False

    @staticmethod
    def todos_servidores_disponibles(lista):
        for servidor in lista:
            if not servidor.disponible:
                return False
        return True

    @staticmethod
    def tiempo_servicio_valido(servidors):
        lista = []
        for x in range(len(servidors)):
            if not servidors[x].disponible:
                lista.append(servidors[x].tiempo_servicio)
        return lista

    @staticmethod
    def servidor_con_menos_cola(lista_servidors):
        min_servidor_cola = lista_servidors[0]
        for servidor in lista_servidors:
            if servidor.cola_por_atender.tamano(
            ) < min_servidor_cola.cola_por_atender.tamano():
                min_servidor_cola = servidor
        return min_servidor_cola
    
    def __str__(self):
        return "Tiempo Servicio %0.6f - Disponible %b" % (
            self.tiempo_servicio, self.disponible)

    def __unicode__(self):
        return "Tiempo Servicio %0.6f - Disponible %b" % (
            self.tiempo_servicio, self.disponible)
