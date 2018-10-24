import sys
from Problema_1.main import problema as problema_1
from Problema_2.main import problema as problema_2
from Problema_4.main import problema as problema_4
from Problema_5.main import problema as problema_5
from Problema_6.main import problema as problema_6
from Problema_7.main import problema as problema_7
from Problema_8.main import problema as problema_8
from Problema_9.main import problema as problema_9 


numero_simulaciones = 1

for i in range(len(sys.argv)):
    if '-p' == sys.argv[i] or '--problem' == sys.argv[i]:
        if '1' == sys.argv[i + 1]:
            problema_a_correr = problema_1
        elif '2'  == sys.argv[i + 1]:
            problema_a_correr = problema_2
        elif '3'  == sys.argv[i + 1]:
            # import Problema_3.main
            print "No se pudo resolver este ejercicio"
        elif '4'  == sys.argv[i + 1]:
            problema_a_correr = problema_4
        elif '5'  == sys.argv[i + 1]:
            problema_a_correr = problema_5
        elif '6'  == sys.argv[i + 1]:
            problema_a_correr = problema_6
        elif '7'  == sys.argv[i + 1]:
            problema_a_correr = problema_7
        elif '8' == sys.argv[i + 1]:
            problema_a_correr = problema_8
        elif '9' in sys.argv:
            problema_a_correr = problema_9
    elif '-s' == sys.argv[i] or '--simuulaciones' == sys.argv[i]:
        numero_simulaciones = int(sys.argv[i + 1])
 
problema_a_correr(numero_simulaciones)
