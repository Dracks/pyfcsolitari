#
#  Reomple.py
#  Solitari
#
#  Created by Dracks on 06/12/08.
#  Copyright (c) 2008 __MyCompanyName__. All rights reserved.
#

from view import Ghost

class Reomple(Ghost):
    def __init__(self, elem, tam_final):
        self.pare=elem;
        self.recursiu=False
        self.tamany= tam_final
        
    def getTamany(self):
        if self.recursiu:
            return (0,0)
        else:
            return self.size
            
    def update(self):
        if not self.recursiu:
            self.recursiu=True;
            self.pare.update()
            tam=self.pare.getTamany()
            self.recursiu=False
            tamx=self.tamany[0]-tam[0]
            tamy=self.tamany[1]-tam[1]
            if tamx<0:
                tamx=0
            if tamy<0:
                tamy=0
            self.size=(tamx,tamy)
        