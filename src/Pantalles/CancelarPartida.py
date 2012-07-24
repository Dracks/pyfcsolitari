#
#  CancelarPartida.py
#  Solitari
#
#  Created by dracks on 11/07/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#
import ViewGL
import Pantalles
import Widgets

class CancelarPartida(Pantalles.Menu):
    def __init__(self, father, recursos, opcions):
        imatge1=recursos.getimgBoto()
        font=recursos.getfont(1)
        font2=recursos.getfont(2)
        
        pla=Widgets.VerticalLayout(0)
        pla.addElement(Widgets.Center((500,35),Widgets.Image(font2.render(opcions.getText('cancel','title'), (100,100,100)))))
        content=Widgets.VerticalLayout(15)
        pla.addElement(Widgets.Center((500,145),content))
        botons=Widgets.HorizontalLayout(20)
        content.addElement(Widgets.Center((500,20), Widgets.Image(font.render(opcions.getText('cancel','text'), (255,255,255)))))
        content.addElement(Widgets.Center((500,40),botons))
        boto=Widgets.Button(imatge1, opcions.getText('Generic','yes'), font)
        boto.setOnMouseClick(self.actionButtonYes)
        botons.addElement(boto)
        boto=Widgets.Button(imatge1, opcions.getText('Generic','no'), font)
        boto.setOnMouseClick(self.actionButtonNo)
        botons.addElement(boto)
        imatge=recursos.getmenuSortir()
        contingut=Widgets.Background(Widgets.Image(imatge),pla)
        menu=Widgets.Center(opcions.getResolucio(),contingut)
        menu.update()
        
        Pantalles.Menu.__init__(self, father, menu)
        
    def actionButtonYes(self,params):
        self.father.deJocaMenu();
        
    def actionButtonNo(self, params):
        self.father.aJocdesdeMenu()
