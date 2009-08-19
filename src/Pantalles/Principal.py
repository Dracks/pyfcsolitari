#
#  untitled.py
#  Solitari
#
#  Created by dracks on 11/07/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#
from view import *
from Pantalles import Menu

class Principal(Menu):
    def __init__(self,father, recursos, opcions):
        imatge1=recursos.getimgBoto()
        font=recursos.getfont(1)
        font2=recursos.getfont(2)
        
        pla=VArea(0)
        pla.addElem(Centre(Imatge(font2.render(opcions.getText('principal','title'), True, (100,100,100))), (300,35)))
        botons=VArea(15)
        pla.addElem(Centre(botons,(300,365)))
        imatge=recursos.getmenuPrincipal()
        contingut=Fons(Imatge(imatge), pla)
        menu=Centre(contingut,opcions.getResolucio())
        boto=Boto(imatge1, opcions.getText('principal','6munts'), font)
        boto.setOnClick(self.actionGame,"Sismunts")
        botons.addElem(boto)
        boto=Boto(imatge1, opcions.getText('principal','acordio'), font)
        boto.setOnClick(self.actionGame,"Acordeo")
        botons.addElem(boto)
        boto=Boto(imatge1, opcions.getText('principal','load'), font)
        boto.setOnClick(self.actionLoad, None)
        botons.addElem(boto)
        boto=Boto(imatge1, opcions.getText('principal','exit'), font)
        boto.setOnClick(self.actionExit,1)
        botons.addElem(Ghost())
        botons.addElem(Ghost())
        botons.addElem(boto)
        
        Menu.__init__(self, father, menu)
        
    def actionGame(self, params):
        self.father.createGame(params);
        
    def actionLoad(self, params):
        self.father.aCarregarJoc()
        
    def actionExit(self, params):
        self.father.sortir(1)