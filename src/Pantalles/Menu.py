#
#  Menu.py
#  Solitari
#
#  Created by dracks on 12/07/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#

class Menu:
    def __init__(self, father, menu):
        self.father=father
        self.menu=menu
        
    def get(self):
        self.menu.update();
        return self.menu