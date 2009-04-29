from view import Ghost

class Boto(Ghost):
    def __init__(self, imatge, text, font):
        self.imatge     = imatge
        self.tam_img    = imatge.get_size()
        self.txt        = text
        self.font       = font
        self.img_txt    = font.render(text,True,(0,0,0))
        self.tam_txt    = self.img_txt.get_size()
        self.desp       = ((self.tam_img[0]-self.tam_txt[0])/2,(self.tam_img[1]-self.tam_txt[1])/2)
    #    self.z          = z
        self.onclick    = False
        
        
    def getTamany(self):
        return self.tam_img
            
    def setOnClick(self, onclick, onclick_params):
        self.onclick=onclick
        self.onclick_params=onclick_params
        #print self.onclick_params
    
    def setText(self, text):
        self.txt     = text
        self.img_txt = self.font.render(text, True, (0,0,0))
        self.tam_txt = self.img_txt.get_size()
        self.desp    = ((self.tam_img[0]-self.tam_txt[0])/2,(self.tam_img[1]-self.tam_txt[1])/2)
    
    def click(self,coordenades):
        if not self.onclick==False:
            if (coordenades[0]<self.tam_img[0] and coordenades[1]<self.tam_img[1]): # inferior a 0 no ho sera mai
                self.onclick(self.onclick_params)
            #print "Me clicaron y soy: %s" % self.txt
        
        
    def pinta(self, sdl_surface, posicio,mouse, z):
        #print self.desp
        #sdl_surface.blit(self.imatge,posicio)
        #sdl_surface.blit(self.img_txt,(posicio[0]+self.desp[0],posicio[1]+self.desp[1]))
        if (len(sdl_surface)-1)==z:
            sdl_surface.append(list())
        sdl_surface[z].append((self.imatge, posicio))
        sdl_surface[z+1].append((self.img_txt,(posicio[0]+self.desp[0],posicio[1]+self.desp[1])))
        