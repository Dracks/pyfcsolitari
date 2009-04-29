#
#  config.py
#  Solitari
#
#  Created by Dracks on 08/07/08.
#  Copyright (c) 2008 __MyCompanyName__. All rights reserved.
#

class Config:
    def __init__(self):
        # Carregarem la configuracio per defecte
        self.idioma="catala"
        self.resolucio=(800, 600)
        
    def __init__(self, file):
        open(file)
        
    def getIdioma(self):
        return self.idioma
        
    def getResolucio(self):
        return self.resolucio
        