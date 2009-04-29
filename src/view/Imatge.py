from view import Ghost

class Imatge(Ghost):
    def __init__(self,imatge, fons=False, centre=(0,0)):
        self.imatge = imatge
        self.tamany = imatge.get_size()
        self.isFons = fons
        self.centre = centre
       # self.z      = z
        
    def getTamany(self):
        if self.isFons:
            return (0,0)
        else:
            return self.tamany
            
    def set(self, imatge):
        self.imatge=imatge
        self.tamany=imatge.get_size()
                
    def pinta(self, sdl_surface, coordenades, mouse,z):
        #sdl_surface.blit(self.imatge, coordenades)
      #  print z;
      #  print sdl_surface
        coordenades=(coordenades[0]-self.centre[0],coordenades[1]-self.centre[1])
        sdl_surface[z].append((self.imatge,coordenades))
      #  print sdl_surface
    