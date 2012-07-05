#
#  Sortir.py
#  Solitari
#
#  Created by dracks on 11/07/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#
import Widgets
import Pantalles

class Sortir(Pantalles.Menu):
    def __init__(self, father, recursos, opcions):
        imatge1=recursos.getimgBoto()
        font=recursos.getfont(1)
        font2=recursos.getfont(2)
        
        pla=Widgets.VerticalLayout(0)
        pla.addElement(Widgets.Center(contents=Widgets.Image(font2.render(opcions.getText('exit','title'), (100,100,100))), surface=(500,35)))
        content=Widgets.VerticalLayout(15)
        pla.addElement(Widgets.Center(contents=content,surface=(500,145)))
        botons=Widgets.HorizontalLayout(20)
        content.addElement(Widgets.Center(contents=Widgets.Image(font.render(opcions.getText('exit','text'), (255,255,255))),surface=(500,20)))
        content.addElement(Widgets.Center(contents=botons,surface=(500,40)))
        boto=Widgets.Button(imatge1, opcions.getText('Generic','yes'), font)
        boto.setOnMouseClick(self.actionButtonYes)
        botons.addElement(boto)
        boto=Widgets.Button(imatge1, opcions.getText('Generic','no'), font)
        boto.setOnMouseClick(self.actionButtonNo)
        botons.addElement(boto)
        imatge=recursos.getmenuSortir()
        contingut=Widgets.Background(Widgets.Image(imatge),pla)
        #self.preguntarSortida=Centre(contingut,self.opcions.resolucio)
       # self.sortint=False
        #menu.update()
        
        #self.menu=Centre(contingut,self.opcions.resolucio);
        menu=Widgets.Center(contents=contingut,surface=opcions.getResolucio());
        menu.update()
        
        Pantalles.Menu.__init__(self, father, menu)
        
    def actionButtonYes(self, button):
        self.father.sortir(1);
        
    def actionButtonNo(self, button):
        self.father.sortir(-1)
