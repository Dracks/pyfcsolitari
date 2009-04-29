from view import Ghost

class Fons(Ghost):
    def __init__(self,fons, contingut, mostrarFons=True):
        self.fons=fons
        self.contingut=contingut
        self.update()
        self.mostrarFons=mostrarFons;
        
    def update(self):
        self.fons.update()
        self.contingut.update()
        (tamx,tamy)=self.fons.getTamany()
        tam2=self.contingut.getTamany()
        if tamx<tam2[0]:
            tamx=tam2[0]
        if tamy<tam2[1]:
            tamy=tam2[1]
        self.tamany=(tamx,tamy)
        
#    def frame(self):
 #       self.contingut.frame()
    def setMostrarFons(self, mostrarFons):
        self.mostrarFons=mostrarFons
        
    def getTamany(self):
        return self.tamany
        
    def click(self, coordenades):
        self.contingut.click(coordenades)
    
    def dobleclick(self,coordenades):
        self.contingut.dobleclick(coordenades)
        
    def pinta(self, sdl_surface, posicio, mouse, z):
        if (len(sdl_surface)-1)==z:
            sdl_surface.append(list())
        if self.mostrarFons:
            self.fons.pinta(sdl_surface, posicio, mouse, z)
        self.contingut.pinta(sdl_surface, posicio, mouse, z+1)
        