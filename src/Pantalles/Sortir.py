#
#  Sortir.py
#  Solitari
#
#  Created by dracks on 11/07/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#
from view import *
from Pantalles import Menu

class Sortir(Menu):
    def __init__(self, father, recursos, opcions):
        imatge1=recursos.getimgBoto()
        font=recursos.getfont(1)
        font2=recursos.getfont(2)
        
        pla=VArea(0)
        pla.addElem(Centre(Imatge(font2.render(opcions.getText('exit','title'), True, (100,100,100))), (500,35)))
        content=VArea(15)
        pla.addElem(Centre(content,(500,145)))
        botons=HArea(20)
        content.addElem(Centre(Imatge(font.render(opcions.getText('exit','text'), True, (255,255,255))),(500,20)))
        content.addElem(Centre(botons,(500,40)))
        boto=Boto(imatge1, opcions.getText('Generic','yes'), font)
        boto.setOnClick(self.actionButtonYes,None)
        botons.addElem(boto)
        boto=Boto(imatge1, opcions.getText('Generic','no'), font)
        boto.setOnClick(self.actionButtonNo,None)
        botons.addElem(boto)
        imatge=recursos.getmenuSortir()
        contingut=Fons(Imatge(imatge),pla)
        #self.preguntarSortida=Centre(contingut,self.opcions.resolucio)
       # self.sortint=False
        #menu.update()
        
        #self.menu=Centre(contingut,self.opcions.resolucio);
        menu=Centre(contingut,opcions.getResolucio());
        
        Menu.__init__(self, father, menu)
        
    def actionButtonYes(self,params):
        self.father.sortir(2);
        
    def actionButtonNo(self, params):
        self.father.sortir(0)
