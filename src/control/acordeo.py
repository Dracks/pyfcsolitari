#
#  acordeo.py
#  Solitari
#
#  Created by Dracks on 07/07/08.
#  Copyright (c) 2008 __MyCompanyName__. All rights reserved.
#
from model import Taulell
from random import Random
from control import Partida

class Acordeo(Partida):
    def __init__(self, taulell=False):
        if (taulell==False):
            taulell=Taulell(6,4,0)
        Partida.__init__(self, taulell)
        self.aratenimrei=(False,-1)
        
    def reparteixCartes(self):
        Partida.reparteixCartes(self)
        rand=Random()
        
        for j in range(1,6+1):
            for i in range(1,8+1):
                k=len(self.cartes)-1
                if (k==0):
                    u=0;
                else:
                    u=rand.randint(0,k)
              #  print " j= %d i=%d longitud=%d valor=%d" % (j, i, k, u)
                carta=self.cartes.pop(u)
                carta.setVisible(i>(j-1))
                self.taulell.ficaCartaColumna(carta,j-1)
                
    def actualitzaReisVisibles(self):
        if self.aratenimrei[1]!=self.NumMoviments:
            for i in range(0,6):
                posicio=0
                for carta in self.taulell.llistaCartesColumna(i):
                    if posicio>0:
                        if carta.getVisible() and carta.getNum()==12:
                            self.aratenimrei=(True, self.NumMoviments)
                            return
                    posicio=posicio+1
            self.aratenimrei=(False,self.NumMoviments)
                
    def comprovaMovimentColumnaAColumna(self,columna1,columna2,p_carta=-1):
        carta1=self.taulell.cartaColumna(columna1,p_carta-1)
        carta2=self.taulell.cartaColumna(columna2)
        if carta2 == False:         # Significa que no hi han cartes
            if carta1.getNum()==12:    # es la mes alta
                return True
            else:
                self.actualitzaReisVisibles()
                if self.aratenimrei[0]==False:
                    return True
                else:
                    return False
                
        if not carta2.getVisible():
            return False;
        #print "carta1 %d- carta2 %d" % (carta1.anterior(), carta2.getNum())
        if carta1.seguent()!=carta2.getNum():
            return False;
        if carta1.getPal()!=carta2.getPal():
            return False;        
        return True;
    
    def comprovaMovimentMuntAColumna(self, munt, columna, p_carta):
        return False
        """carta1=self.taulell.cartaColuma(columna1)
        carta2=self.taulell.cartaMunt(munt)
        
        if carta2 == False:         # Significa que no hi han cartes
            if carta1.num()==12:    # es la mes alta
                return True
            else :
                return False
                
        if not carta2.getVisible():
            return False;
       # print "carta1 %d- carta2 %d" % (carta1.anterior(), carta2.getNum())
        if carta1.seguent()!=carta2.getNum():
            return False;
        if carta1.getPal()==carta2.getPal():
            return False;        
        return True; """
        
    def buidaCache(self):
        self.aratenimrei=(False,-1)

