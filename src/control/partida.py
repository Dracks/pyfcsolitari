#
#  partida.py
#  Solitari
#
#  Created by Dracks on 07/07/08.
#  Copyright (c) 2008 __MyCompanyName__. All rights reserved.
#
from model import Taulell,Carta

class Partida:
    def __init__(self,taulell):
        # generem el taulell i la baralla de cartes
        # self.taulell=Taulell(6,4,0) # Taulell de 6 columnes i 4 munts per cada pal
        self.NumMoviments=0
        self.taulell=taulell
        self.cartes=list()
        
    def reparteixCartes(self):
        baralla=list()
        for i in range(1,4+1): # El 4 pals diferents, 1,2,3,4 que concordaran amb les ratlles de les cartes
            for j in range(1,12+1): # El numero de la carta
                #print "pal: %d numero: %d" % (i, j)
                carta=Carta(j,i)
                carta.setAnterior(j-1); carta.setSeguent(j+1)
                baralla.append(carta)
        self.cartes=baralla
#        return baralla;

    def comprovaClickCartaPila(self, pila, carta):
        model_carta=self.taulell.cartaColumna(pila, carta)
        if model_carta!=False:
            return model_carta.getVisible()
        else: 
            return False
        
##### Com que tots els jocs que implementara el meu solitari coincideixen amb aquestes normes, doncs... ho deixo generic, i tira milles... :-P
    def comprovaMovimentColumnaAMunt(self,columna1,munt):
        carta1=self.taulell.cartaColumna(columna1)
        carta2=self.taulell.cartaMunt(munt)
        if carta2==False:
            if carta1==False:
                #print "%i - %i" % (columna1,munt)
                raise("error")
            if carta1.getNum()==1:
                return True
            else:
                return False
        if carta1.anterior()!=carta2.getNum():
            return False;
        if carta2.getPal()==carta1.getPal():
            return True;
        return False;
        
        
    def comprovaMovimentMuntAMunt(self, munt1, munt2):
        carta1=self.taulell.cartaMunt(munt1)
        carta2=self.taulell.cartaMunt(munt2)
        if carta2==False:
            if carta1.getNum()==1:
                return True
            else:
                return False
        if carta1.anterior()!=carta2.getNum():
            return False;
        if carta2.getPal()==carta1.getPal():
            return True;
        return False;
    
    def comprovaMovimentAvancat(self, columna1, columna2, carta):
        return False
    
    def buidaCache(self):
        None
    
    def partidaFinalitzada(self):
        finalitzada=True
        for i in range(self.taulell.nmunts()):
            last=self.taulell.cartaMunt(i)
            if last==False:
                finalitzada=False
                break;
            if last.getNum()!=12:
                finalitzada=False
                break;
        return finalitzada
    
    def getTaulell(self):
        return self.taulell
    
    def getNumMoviments(self):
        return self.NumMoviments;
    
    def setMoviments(self, moviments):
        self.NumMoviments=moviments
        
    def incrementaMoviments(self):
        self.NumMoviments=int(self.NumMoviments)+1;
        return self.NumMoviments;
    
    def getMoviments(self):
        moviments=list()
        num_columnes=self.taulell.ncolumnes()
        num_munts=self.taulell.nmunts()
        for i in range(num_columnes):
            num_cartes=len(self.taulell.llistaCartesColumna(i))
            for j in range(num_cartes):
                if self.comprovaClickCartaPila(i,j):
                    for k in range(num_columnes):
                        if k!=i and self.comprovaMovimentColumnaAColumna(i,k,j+1):
                            moviments.append((0,i,j))
            if num_cartes>0 and self.comprovaClickCartaPila(i,num_cartes-1):
                for k in range(num_munts):
                    if self.comprovaMovimentColumnaAMunt(i,k):
                        moviments.append((0,i,num_cartes-1))
        for i in range(num_munts):
            for j in range(num_columnes):
                num_cartes=len(self.taulell.llistaCartesMunt(i))
                if num_cartes>0:
                    if self.comprovaMovimentMuntAColumna(i,j,num_cartes-1):
                        moviments.append((1,i,num_cartes-1))
        return moviments
    
    def getMovimentsFromPila(self, pila, carta):
        moviments=list()
        num_columnes=self.taulell.ncolumnes()
        num_munts=self.taulell.nmunts()
        for i in range(num_columnes):
            if pila!=i and self.comprovaMovimentColumnaAColumna(pila,i,carta):
                moviments.append((0,i,len(self.taulell.llistaCartesColumna(i))-1))
        for i in range(num_munts):
            if self.comprovaMovimentColumnaAMunt(pila,i):
                moviments.append((1,i,len(self.taulell.llistaCartesMunt(i))-1))
        return moviments
    
    def getMovimentsFromMunt(self, munt):
        moviments=list()
        num_cartes=len(self.taulell.llistaCartesMunt(munt))
        num_columnes=self.taulell.ncolumnes()
        for i in range(num_columnes):
            if self.comprovaMovimentMuntAColumna(munt, i, munt-1):
                moviments.append((0,i,len(self.taulell.llistaCartesColumna(i))-1))
        return moviments

        
