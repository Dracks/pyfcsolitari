#
#  siscolumnes.py
#  Solitari
#
#  Created by Dracks on 07/07/08.
#  Copyright (c) 2008 __MyCompanyName__. All rights reserved.
#
from model import Taulell
from random import Random
from control import Partida

class Sismunts(Partida):
    def __init__(self, taulell=False):
        if (taulell==False):
            taulell=Taulell(6,4,1)
        Partida.__init__(self, taulell)
    
    def reparteixCartes(self):
        Partida.reparteixCartes(self)
        rand=Random()
        for j in range(1,6+1):
            for i in range(1,j+1):
                k=len(self.cartes)-1
                if (k==0):
                    u=0;
                else:
                    u=rand.randint(0,k)
              #  print " j= %d i=%d longitud=%d valor=%d" % (j, i, k, u)
                carta=self.cartes.pop(u)
                carta.setVisible(i==j)
                self.taulell.ficaCartaColumna(carta,j-1)
        k=len(self.cartes)
        for i in range(k):
            c=rand.randint(0,(k-i-1))
            c=self.cartes.pop(c)
            c.setVisible(False)
            self.taulell.ficaCartaSobrantOculta(c)
                
    def comprovaClickCartaPila(self, columna, carta):
        if Partida.comprovaClickCartaPila(self, columna, carta):
            if carta==len(self.taulell.llistaCartesColumna(columna))-1:
                return True
            elif carta==len(self.taulell.llistaCartesColumna(columna))-2 and len(self.getMovimentsFromPila(columna, carta+2))>0:
                return True
                    
        return False
        
    def comprovaMovimentAvancat(self, columna1, columna2, carta):
        #print "merda %d -%d" % (len(self.taulell.llistaCartesColumna(columna1)), carta)
        if len(self.taulell.llistaCartesColumna(columna1))-1==carta:
            #print "hola"
            moviments=self.getMovimentsFromPila(columna1, carta+1)
            #print moviments
            if len(moviments)>0:
                if moviments[0][0]!=0:
                    return self.comprovaMovimentColumnaAColumna(columna1,columna2,carta,False)
                if moviments[0][1]!=columna2:
                    return self.comprovaMovimentColumnaAColumna(columna1,columna2,carta,False)
                if len(moviments)>1:
                    return self.comprovaMovimentColumnaAColumna(columna1,columna2,carta,False)
        return False
        
    def comprovaMovimentColumnaAColumna(self,columna1,columna2,p_carta, testUltim=True):
        if len(self.taulell.llistaCartesColumna(columna1))!=p_carta and testUltim:
            #print "die %d-%d" % (p_carta, len(self.taulell.llistaCartesColumna(columna1)))
            return False
        carta1=self.taulell.cartaColumna(columna1,p_carta-1)
        carta2=self.taulell.cartaColumna(columna2)
        if carta2 == False:         # Significa que no hi han cartes
            return True
        if not carta2.getVisible():
            return False;
        #print "carta1 %d- carta2 %d" % (carta1.anterior(), carta2.getNum())
        if carta1.seguent()!=carta2.getNum():
            return False;
        if carta1.getPal()==carta2.getPal():
            return False;        
        return True;
    
    def comprovaMovimentMuntAColumna(self, munt, columna, p_carta):
        carta1=self.taulell.cartaMunt(munt)
        carta2=self.taulell.cartaColumna(columna)
        if carta2 == False:         # Significa que no hi han cartes
            return True
        if not carta2.getVisible():
            return False;
        #print "carta1 %d- carta2 %d" % (carta1.anterior(), carta2.getNum())
        if carta1.seguent()!=carta2.getNum():
            return False;
        if carta1.getPal()==carta2.getPal():
            return False;  
        return True;
        
    def comprovaMovimentExtresAColumna(self, res, columna, p_carta):
        carta1=self.taulell.cartaSobrantVisible()
        carta2=self.taulell.cartaColumna(columna)
        if carta2 == False:         # Significa que no hi han cartes
            return True
        if not carta2.getVisible():
            return False;
        #print "carta1 %d- carta2 %d" % (carta1.anterior(), carta2.getNum())
        if carta1.seguent()!=carta2.getNum():
            return False;
        if carta1.getPal()==carta2.getPal():
            return False;
        return True;
        
    ## S'ha d'arreglar
    def comprovaMovimentExtresAMunt(self, res, munt):
        carta1=self.taulell.cartaSobrantVisible()
        carta2=self.taulell.cartaMunt(munt)
        if carta2 == False:         # Significa que no hi han cartes
            if carta1.getNum()==1:
                return True
            else:
                return False
        if carta1.anterior()!=carta2.getNum():
            return False;
        if carta1.getPal()==carta2.getPal():
            return True;
        return False;
    
    def getMoviments(self):
        moviments=Partida.getMoviments(self)
        num_columnes=self.taulell.ncolumnes()
        num_munts=self.taulell.nmunts()
        num_extres=len(self.taulell.llistaCartesSobrantsVisibles())
        if num_extres>0:
            for i in range(num_columnes):
                if self.comprovaMovimentExtresAColumna(0,i,num_extres-1):
                    moviments.append((2,1,num_extres-1))
                    return moviments
            for i in range(num_munts):
                if self.comprovaMovimentExtresAMunt(0,i):
                    moviments.append((2,1,num_extres-1))
                    return moviments
        return moviments;
    
    def getMovimentsFromExtres(self):
        moviments=list()
        num_columnes=self.taulell.ncolumnes()
        num_munts=self.taulell.nmunts()
        num_extres=len(self.taulell.llistaCartesSobrantsVisibles())
        if num_extres>0:
            for i in range(num_columnes):
                if self.comprovaMovimentExtresAColumna(0,i,num_extres-1):
                    moviments.append((0,i,len(self.taulell.llistaCartesColumna(i))-1))
            for i in range(num_munts):
                if self.comprovaMovimentExtresAMunt(0,i):
                    moviments.append((1,i,len(self.taulell.llistaCartesMunt(i))-1))
        return moviments;