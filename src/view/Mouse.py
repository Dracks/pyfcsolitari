import pygame

class Mouse:
    def __init__(self):
        self.llista=False
        self.coordenades=(0,0)
        self.UnClickFunct= False
        self.overflow=(0,0)
        
    def frame(self):
        self.coordenades=pygame.mouse.get_pos()
    
    def arrastrar(self,llista, coordenades):
        self.llista=llista
        self.overflow=coordenades;
        
    def getLlista(self):
        return self.llista
        
    def getOverflow(self):
        return self.overflow
        
    def getTamany(self):
        self.llista.update()
        return self.llista.getTamany()
    
    def getCoordenades(self):
        return pygame.mouse.get_pos()
    
    def setOnUnClick(self, function, params):
        self.UnClickFunct=function
        self.UnClickParams=params
        
    def unClick(self):
        if self.UnClickFunct!= False:
            self.UnClickFunct(self.UnClickParams)
        
    def pinta(self, sdl_surface,z):
        if not self.llista == False:
            pos=pygame.mouse.get_pos();
            self.llista.pinta(sdl_surface,(pos[0]-self.overflow[0], pos[1]-self.overflow[1]) ,(0,0), z)
        