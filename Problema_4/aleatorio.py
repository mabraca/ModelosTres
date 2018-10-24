#! /usr/bin/python
# -*- encoding: utf-8 -*-
from __future__ import division

from math import log
from random import randint


def tiempo_de_falla():
	x = randint(1,100)*1.0/100.0
	if x == 1.0:
		x = 0.99	
	falla = - log(1-x)
	return falla*10

def tiempo_de_reparacion():
	x = randint(1,100)*1.0/100.0
	if x == 1.0:
	    x = 0.99
	tiempo = - (log(1-x))/2
	return tiempo*10