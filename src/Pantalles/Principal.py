#
#  untitled.py
#  Solitari
#
#  Created by dracks on 11/07/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#
import Widgets
import Pantalles

class Principal(Pantalles.Menu):
    def __init__(self,father, recursos, opcions):
        imatge1=recursos.getimgBoto()
        font=recursos.getfont(1)
        font2=recursos.getfont(2)
        
        pla=Widgets.VerticalLayout(0)
        pla.addElement(Widgets.Center(contents=Widgets.Image(font2.render(opcions.getText('principal','title'), (100,100,100))), surface=(300,35)))
        botons=Widgets.VerticalLayout(15)
        pla.addElement(Widgets.Center(contents=botons,surface=(300,365)))
        imatge=recursos.getmenuPrincipal()
        contingut=Widgets.Background(Widgets.Image(imatge), pla)
        boto=Widgets.Button(imatge1, opcions.getText('principal','6munts'), font)
        boto.setOnMouseClick(self.actionGameSixMounts)
        botons.addElement(boto)
        boto=Widgets.Button(imatge1, opcions.getText('principal','acordio'), font)
        boto.setOnMouseClick(self.actionGameAcordeo)
        botons.addElement(boto)
        boto=Widgets.Button(imatge1, opcions.getText('principal','load'), font)
        boto.setOnMouseClick(self.actionLoad)
        botons.addElement(boto)
        boto=Widgets.Button(imatge1, opcions.getText('principal','exit'), font)
        boto.setOnMouseClick(self.actionExit)
        botons.addElement(Widgets.Empty())
        botons.addElement(Widgets.Empty())
        botons.addElement(boto)#"""

        """print "Creem pla"
        pla=Widgets.VerticalLayout(0)
        print "Afegim titol"
        pla.addElement(Widgets.Center(contents=Widgets.Image(font2.render(opcions.getText('principal','title'), (100,100,100))), surface=(300,35)))
        print "Creem Boto"
        boto=Widgets.Button(imatge1, opcions.getText('principal','6munts'), font)
        boto.setOnMouseClick(self.actionGameSixMounts)
        print "Afegim Boto"
        pla.addElement(boto)


        imatge=recursos.getmenuPrincipal()
        contingut=Widgets.Background(Widgets.Image(imatge), pla)"""

        menu=Widgets.Center(contents=contingut,surface=opcions.getResolucio())
        
        Pantalles.Menu.__init__(self, father, menu)
        
    def actionGameSixMounts(self, button):
        print "Sis Munts"
        self.father.createGame("Sismunts");

    def actionGameAcordeo(self, button):
        print "Acordeo"
        self.father.createGame("Acordeo");

    def actionLoad(self, button):
        print "Load"
        self.father.aCarregarJoc()
        
    def actionExit(self, button):
        print "Exit"
        self.father.sortir(0)