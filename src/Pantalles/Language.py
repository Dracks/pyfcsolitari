#
#  Language.py
#  Solitari
#
#  Created by dracks on 11/07/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#

from view import *
from Pantalles import Menu
class Language(Menu):
    def __init__(self, father, recursos, opcions):
       # self.father=father;
        self.opcions=opcions
        imatge1=recursos.getimgBoto()
        font=recursos.getfont(1)
        font2=recursos.getfont(2)
        
        pla=VArea(0)
        pla.addElem(Centre(Imatge(font2.render('Choose Language',True, (100,100,100))), (300,35)))
        botons=VArea(15)
        pla.addElem(Centre(botons,(300,365)))
        imatge=recursos.getmenuIdioma()
        contingut=Fons(Imatge(imatge),pla)
        menu=Centre(contingut, opcions.getResolucio())
        
        boto=Boto(imatge1, 'Catala', font)
        boto.setOnClick(self.seleccionarIdioma, 'catala')
        botons.addElem(boto)
        
        boto=Boto(imatge1, 'Castellano', font)
        boto.setOnClick(self.seleccionarIdioma, 'castellano')
        botons.addElem(boto)
        
        #menu.update();
        
        Menu.__init__(self, father, menu)
    
    def seleccionarIdioma(self,idioma):
        self.opcions.setLanguage(idioma)
        self.opcions.save();
        self.father.reset();
        self.father.loadInici();
        