#!/bin/env python
# Aix\362 nom\351s creara el objecte de control, tot el demes es fara per objectes.
try:
    import psyco
    #psyco.full()
except:
    print 'sin acelerar con psyco...'

from control import joc
from model import Opcions
#from finestra import *

if __name__ == "__main__":
    joc(Opcions('config.cfg')).executa()