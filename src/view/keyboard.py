#
#  keyboard.py
#  Solitari
#
#  Created by Dracks on 09/12/08.
#  Copyright (c) 2008 __MyCompanyName__. All rights reserved.
#
from pygame.locals import *
from time import time

class keyboard:
    def __init(self):
        self.listKeysDown=list();
        #None
    
    def keydown(self, event):
        self.listKeysDown.append({"key": event.key; "escrit": False; "timestamp": time}
        
    def keyup(self, event):