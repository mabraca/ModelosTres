from random import randint, sample
from collections import deque
from math import log
import random

Nemb = [127,162,179,75,223,186,124,45,100,171,235,176,130,159,117,100,92,68,242,122,184,84,240,319,61,78,20,141,202, 
        213,204,360,169,206,326,210,335,233,102,243,135,310,138,95,216,99,346,220,191,230,219,225,271,270,110,305,157,
        128,163,90,148,70,40,80,105,159,141,150,164,200,213,195,134,141,107,177,109,48,145,114,400,212,258,198,229,175,
        199,177,194,185,303,335,310,104,374,190,211,160,138,227,122,230,97,166,232,187,212,125,119,90,286,310,115,277,
        189,159,266,170,28,141,155,309,152,122,262,111,254,124,138,190,136,110,396,96,86,111,81,226,50,134,131,120,112,
        140,280,145,208,333,250,221,318,120,72,166,194,87,94,170,65,190,359,312,205,77,197,359,174,140,167,181,143,99,
        297,92,246,211,275,224,171,290,291,220,239,126,89,66,35,26,129,234,181,180,58,40,54,123,78,319,389,121]

#Con esta funcion se calcula la distribucion empirica acumulada de la muestra
def distribucion_empirica(Demb):
        m = len(Demb)
        a = Demb[0]
        b = Demb[m-1]
        i = 0
        y = []

        while i < m:
                yt = 0
                j = 0
                while j < m:
                        xu = cota_superior(a,b,m,i)
                        if Demb[j] < xu:
                                yt = yt + 1/m
                                j = j+1
                        else:
                                j = j+1
                y.append(yt)
                i = i+1

        return y
#Aqui se utiliza un loop para obtener el valor correcto de embarcados
def obtener_embarcados(x):
        xs = sorted(x)
        m = len(xs)
        y = distribucion_empirica(xs)
        rng = random.random()
        j = 0
        while j < m:
                if rng <= y[j]:
                        return calcular_distribucion(rng,y,xs,j)
                else:
                        j = j+1

#Ecuacion de la recta despejada para obtener el valor de los embarcados
def calcular_distribucion(u,y,x,j):
        xl = cota_inferior(x[0],x[199],200,j)
        xu = cota_superior(x[0],x[199],200,j)
        xf = xl + (u-y[j-1]/y[j]-y[j-1]) * (xu - xl)

        return xf

#La cota inferior del valor X                        
def cota_inferior(a,b,m,i):
        xl = a + (b-a/m) * i
        return xl

#La cota superior del valor X
def cota_superior(a,b,m,i):
        xu = a + (b-a/m) * (i+1)
        return xu



def cantidad_desembargues(emb):
    desembarques = 0

    while emb > 0:
        x = randint(1,100)
        if 1 <= x < 50:
            desembarques += 1
        emb -= 1
        return desembarques

def iniciar_simulacion(embarques):

    NpasVect = [0,0,0,0,0,0,0,0,0,0]
    NpasTotal = 0
    estacion = 0

    tiempoT1 = 0
    tiempoT2 = 0
    tiempoTotal = 0

    while 0 <= estacion < 10:
        if estacion == 0:
            Npas = embarques[0]
        #    print('cantidad de embarques en la estacion 0 '+str(Npas))
            Tint0 = 100*(1+(0.1*log(Npas)))
        #    print('tiempo en segundos desde estacion 0 a 1' +str(Tint0))
            Nemb = Npas
            Ndes = 0
            Tde0 = 20*(1+(0.1*log(Ndes+Nemb)))
        #    print('tiempo en segundos emb en la estacion 0 ' +str(Tde0))
            tiempoT0 = Tint0 + Tde0 
        #    print ('tiempo T0' +str(tiempoT0))
            NpasVect[0] = Npas
            NpasTotal = Npas
        #    print ('Npas' +str(Npas))
            
        else:
            if 1 <= estacion <= 8:
                Nemb = embarques[estacion]
            #    print('cantidad de embarques en la estacion'+str(Nemb))
                Ndes = cantidad_desembargues(NpasVect[estacion-1])
            #    print('cantidad de desembarques en la estacion' +str(Ndes))
                Npas1 = NpasVect[estacion-1] + Nemb - Ndes
            #    print ('cantidad de psajeros actual' +str(Npas1))
                Tint1 = 100*(1+(0.1*log(Npas1)))
            #    print('tiempo en segundos ' +str(Tint1))
                Tde1 = 20*(1+(0.1*log(Ndes+Nemb)))
            #    print('tiempo en segundos emb/desemb' +str(Tde1))
                tiempoT1 += Tint1 + Tde1
            #    print ('tiempo T1' +str(tiempoT1))
                NpasVect[estacion]=Npas1
                NpasTotal += Npas1
            #    print ('Npas1' +str(Npas1))

            else:
                Npas3 = NpasVect[8]
            #    print ('el numero de pasajeros antes de la ult estacion es ' +str(Npas3))
                Ndes3 = Npas3
                Tde2 = 20*(1+(0.1*log(Ndes3)))
            #    print('tiempo en segundos emb/desemb estacion final' +str(Tde2))
                tiempoT2 = Tde2  
            #print ('tiempo T2' +str(tiempoT2))

        estacion += 1

    tiempoTotal = tiempoT0 + tiempoT1 + tiempoT2
    promPasajeros = NpasTotal/9
    maximoPasajeros = max(embarques)

    print "----------------------------------------------------------------"
    print "----------------------- Resultados! ----------------------------"
    print "----------------------------------------------------------------"
    print "(a) El tiempo total del recorrido en segundos: %0.2f " % (tiempoTotal)
    print "(b) El nro de pasajeros promedio a bordo del tren es: %0.2f" % (promPasajeros)  
    print "(c) El nro maximo de pasajeros embarcados es: %d " % (maximoPasajeros)
    print ""

    return [tiempoTotal, promPasajeros, maximoPasajeros]

