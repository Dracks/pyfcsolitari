#
#  CancelarPartida.py
#  Solitari
#
#  Created by dracks on 11/07/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#
from view import *
from Pantalles import Menu

class CancelarPartida(Menu):
    def __init__(self, father, recursos, opcions):
        imatge1=recursos.getimgBoto()
        font=recursos.getfont(1)
        font2=recursos.getfont(2)
        
        pla=VArea(0)
        pla.addElem(Centre(Imatge(font2.render(opcions.getText('cancel','title'), True, (100,100,100))), (500,35)))
        content=VArea(15)
        pla.addElem(Centre(content,(500,145)))
        botons=HArea(20)
        content.addElem(Centre(Imatge(font.render(opcions.getText('cancel','text'), True, (255,255,255))),(500,20)))
        content.addElem(Centre(botons,(500,40)))
        boto=Boto(imatge1, opcions.getText('Generic','yes'), font)
        boto.setOnClick(self.actionButtonYes,False)
        botons.addElem(boto)
        boto=Boto(imatge1, opcions.getText('Generic','no'), font)
        boto.setOnClick(self.actionButtonNo,False)
        botons.addElem(boto)
        imatge=recursos.getmenuSortir()
        contingut=Fons(Imatge(imatge),pla)
        menu=Centre(contingut,opcions.getResolucio())
        menu.update()
        
        Menu.__init__(self, father, menu)
        
    def actionButtonYes(self,params):
        self.father.deJocaMenu();
        
    def actionButtonNo(self, params):
        self.father.aJocdesdeMenu()
