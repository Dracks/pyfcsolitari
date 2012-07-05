#
#  Desactualitzat.py
#  Solitari
#
#  Created by dracks on 11/07/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#

import ViewGL
import Widgets
import Pantalles

class Desactualitzat(Pantalles.Menu):
    def __init__(self, father, recursos, opcions, lastVersion, VERSIO):
        #self.father=father
        
        imatge1=recursos.getimgBoto()
        font=recursos.getfont(1)
        font2=recursos.getfont(2)
        
        pla=Widgets.VerticalLayout(0)
        pla.addElement(Widgets.Center(ViewGL.Image(font2.render(opcions.getText('update','title'),(100,100,100))), (500,35)))
        content=Widgets.VerticalLayout(15)
        pla.addElement(Widgets.Center(content,(500,145)))
        botons=Widgets.VerticalLayout(20)
        text_actualitzacio=opcions.getText('update','text').replace('<~old~>', VERSIO).replace('<~new~>',lastVersion)
        content.addElem(Widgets.Center(ViewGL.Image(font.render(text_actualitzacio, (255,255,255))),(500,20)))
        content.addElem(Widgets.Centre(botons,(500,40)))
        boto=Widgets.Button(imatge1, opcions.getText('Generic','accept'), font)
        boto.setOnClick(self.actionAccept,None)
        botons.addElement(boto)
        imatge=recursos.getmenuSortir()
        contingut=Fons(Widgets.Imatge(imatge),pla)
        
        Pantalles.Menu.__init__(self, father, Widgets.Center(contingut, opcions.getResolucio()))

    def actionAccept(self,params):
        self.father.aPrincipaldesdeActualitzacio()
