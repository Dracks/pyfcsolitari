#
#  Desactualitzat.py
#  Solitari
#
#  Created by dracks on 11/07/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#

from view import *
from Pantalles import Menu

class Desactualitzat(Menu):
    def __init__(self, father, recursos, opcions, lastVersion, VERSIO):
        #self.father=father
        
        imatge1=recursos.getimgBoto()
        font=recursos.getfont(1)
        font2=recursos.getfont(2)
        
        pla=VArea(0)
        pla.addElem(Centre(Imatge(font2.render(opcions.getText('update','title'), True, (100,100,100))), (500,35)))
        content=VArea(15)
        pla.addElem(Centre(content,(500,145)))
        botons=HArea(20)
        text_actualitzacio=opcions.getText('update','text').replace('<~old~>', VERSIO).replace('<~new~>',lastVersion)
        content.addElem(Centre(Imatge(font.render(text_actualitzacio, True, (255,255,255))),(500,20)))
        content.addElem(Centre(botons,(500,40)))
        boto=Boto(imatge1, opcions.getText('Generic','accept'), font)
        boto.setOnClick(self.actionAccept,None)
        botons.addElem(boto)
        imatge=recursos.getmenuSortir()
        contingut=Fons(Imatge(imatge),pla)
        
        Menu.__init__(self, father, Centre(contingut, opcions.getResolucio()))

    def actionAccept(self,params):
        self.father.aPrincipaldesdeActualitzacio()
