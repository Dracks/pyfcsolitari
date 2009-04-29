# -*- coding: UTF-8 -*-
#
#  Carta.py
#  Solitari
#
#  Created by Dracks on 30/05/08.
#  Copyright (c) 2008 __MyCompanyName__. All rights reserved.
#

class Carta:
    """ implementació del objecte carta, amb algun extra """
    def __init__(self,num,pal, visible=False):
        self.num=num;
        self.pal=pal;
        self.visible=visible;
        self.carta_seguent=self.num+1;
        self.carta_anterior=self.num-1;
        
    """ Retorna el numero de la seguent carta """
    def seguent(self):
        return self.carta_seguent
    
    """ Retorna el numero de la carta anterior """
    def anterior(self): 
        return self.carta_anterior
    
    """ Defineix la seguent carta, per parametre se li passa la carta """
    def setSeguent(self, carta):
        self.carta_seguent=carta;
    
    """ Defineix la carta anterior, per parametre se li passa la carta """
    def setAnterior(self, carta):
        self.carta_anterior=carta;
        
    def getVisible(self):
        return self.visible;
        
    def setVisible(self, visible):
        self.visible=visible
        return self;
    
    def getPal(self): # ens retorna el pal al que pertany
        return self.pal
        
    def getNum(self): # ens retorna el numero de carta que es
        return self.num
        
    def carta(self): # No se si el necessitare, per\362 mai se sap 
        return self.num,self.pal