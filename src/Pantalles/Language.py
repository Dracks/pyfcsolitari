#
#  Language.py
#  Solitari
#
#  Created by dracks on 11/07/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#

import ViewGL
import Widgets
import Pantalles


class Language(Pantalles.Menu):
    def __init__(self, father, recursos, opcions):
       # self.father=father;
        self.opcions=opcions
        imatge1=recursos.getimgBoto()
        font=recursos.getfont(1)
        font2=recursos.getfont(2)
        
        pla=Widgets.VerticalLayout(0)
        pla.addElement(Widgets.Center(Widgets.Image(font2.render('Choose Language',True, (100,100,100))), (300,35)))
        botons=Widgets.VerticalLayout(15)
        pla.addElement(Widgets.Center(botons,(300,365)))
        imatge=recursos.getmenuIdioma()
        contingut=Widgets.Background(Widgets.Image(imatge),pla)
        menu=Widgets.Center(contingut, opcions.getResolucio())
        
        boto=Widgets.Button(imatge1, 'Catala', font)
        boto.setOnClick(self.seleccionarIdioma, 'catala')
        botons.addElement(boto)
        
        boto=Widgets.Button(imatge1, 'Castellano', font)
        boto.setOnClick(self.seleccionarIdioma, 'castellano')
        botons.addElement(boto)
        
        #menu.update();
        
        Pantalles.Menu.__init__(self, father, menu)
    
    def seleccionarIdioma(self,idioma):
        self.opcions.setLanguage(idioma)
        self.opcions.save();
        self.father.reset();
        self.father.loadInici();
        