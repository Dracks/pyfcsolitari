#
#  Guanyar.py
#  Solitari
#
#  Created by dracks on 11/07/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#
import ViewGL
import Pantalles

class Guanyar(Pantalles.Menu):
    def __init__(self, father, recursos, opcions):
        imatge1=recursos.getimgBoto()
        font=recursos.getfont(1)
        font2=recursos.getfont(2)
        
        pla=VArea(0)
        pla.addElem(Centre(Imatge(font2.render(self.opcions.getText('win','title'), True, (100,100,100))), (500,35)))
        content=VArea(15)
        pla.addElem(Centre(content,(500,145)))
#        botons=HArea(20)
        text=Imatge(font.render("", True, (100,100,100)))
        content.addElem(Centre(text,(500,20)))
        boto=Boto(imatge1,self.opcions.getText('win','button'), font)
        boto.setOnClick(self.deFinalitzadaaPrincipal, False)
        content.addElem(Centre(boto,(500,20)))
        menu=Centre(Fons(Imatge(self.recursos.getPartidaFinalitzada()),pla), self.opcions.resolucio)
        self.text=text
        
        Pantalles.Menu.__init__(self, father, menu)
        
    def getText(self):
        return self.text
        
    