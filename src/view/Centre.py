class Centre:
    def __init__(self, elem, centre):
        self.elem= elem
        self.coordenades=centre
        self.update()
    
    def update(self):
        self.elem.update()
        tamany=self.elem.getTamany()
        self.posicio=((self.coordenades[0]-tamany[0])/2,(self.coordenades[1]-tamany[1])/2)
        self.tamany=self.coordenades
        if self.tamany[0]<tamany[0]:
            self.tamany=(tamany[0],self.tamany[1])
        if self.tamany[1]<tamany[1]:
            self.tamany=(self.tamany[0],tamany[1])
       # print self.tamany
       # print self.posicio
                    
    def getTamany(self):
        return self.tamany
    
    def setCoordenades(self, centre):
        self.coordenades=centre
    
    def frame(self):
        self.elem.frame()
    
    def click(self, coordenades):
        coordenades=(coordenades[0]-self.posicio[0], coordenades[1]-self.posicio[1])
        if (coordenades[0] >0 and coordenades[1]>0 and coordenades[0]<self.tamany[0] and coordenades[1]<self.tamany[1]):
            return self.elem.click(coordenades)
        else: return False
    
    def dobleclick(self, coordenades):
        coordenades=(coordenades[0]-self.posicio[0], coordenades[1]-self.posicio[1])
        if (coordenades[0] >0 and coordenades[1]>0 and coordenades[0]<self.tamany[0] and coordenades[1]<self.tamany[1]):
            return self.elem.dobleclick(coordenades)
        else: return False
        
    def pinta(self, sdl_surface, coordenades,mouse, z):
        self.elem.pinta(sdl_surface,(coordenades[0]+self.posicio[0],coordenades[1]+self.posicio[1]),mouse, z)