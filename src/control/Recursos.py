#
#  Recursos.py
#  Solitari
#
#  Created by Dracks on 17/08/08.
#  Copyright (c) 2008 __MyCompanyName__. All rights reserved.
#
import  pygame
from pygame.locals import *
CARTA_ALTURA=154;
CARTA_AMPLADA=100; 
class Recursos:
    def __init__(self):
        self.fonts=(False,False,False,False)
        self.imgBoto=False
        self.fonsMenu=False
        self.menuPrincipal=False
        self.menuSortir=False
        self.menuOpcions=False
        self.menuGuardariCarregar=False
        self.menuJoc=False
        self.menuPartida=False
        self.partidaGuardarCarregar=False
        self.menuEscollirJoc=False
        self.fonsJoc=False
        self.cartes=False
        self.cartanull=False
        self.oculta=False
        self.imatgeMarca=False
        
    def getfont(self,size):
        if self.fonts[size]==False:
            if size==0:
                None
            elif size==1:
                self.fonts=(self.fonts[0],pygame.font.Font("Data/font3.ttf",15),self.fonts[2], self.fonts[3])
            elif size==2:
                self.fonts=(self.fonts[0],self.fonts[1],pygame.font.Font("Data/font3.ttf",28), self.fonts[3])
            else:
                None
                
        return self.fonts[size]
            
    def getimgBoto(self):
        if self.imgBoto==False:
            self.imgBoto=pygame.image.load("Data/boto.png").convert_alpha()
                
        return self.imgBoto
            
    def getfonsMenu(self):
        if self.fonsMenu==False:
            self.fonsMenu=pygame.Surface((1440,900))
            self.fonsMenu.fill(0x113311)
        return self.fonsMenu
        
    def getmenuPrincipal(self):
        if self.menuPrincipal==False:
            self.menuPrincipal=pygame.Surface((300,400))
            self.menuPrincipal.fill(0x444400)
        return self.menuPrincipal
        
    def getmenuSortir(self):
        if self.menuSortir==False:
            self.menuSortir=pygame.Surface((500,200))
            self.menuSortir.fill(0x003300)
        return self.menuSortir
        
    def getPartidaGuardarCarregar(self):
        if self.partidaGuardarCarregar==False:
            self.partidaGuardarCarregar=pygame.Surface((500,30))
            self.partidaGuardarCarregar.fill(0x419511)
        return self.partidaGuardarCarregar

    def getmenuGuardariCarregar(self):
        if self.menuGuardariCarregar==False:
            self.menuGuardariCarregar=pygame.Surface((600,400))
            self.menuGuardariCarregar.fill(0x444400)
        return self.menuGuardariCarregar
        
        
    def getmenuOpcions(self):
        None

    def getmenuJoc(self):
        None
    
    def getmenuPartida(self):
        None
    
    def getPartidaFinalitzada(self):
        return self.getmenuSortir()
    def getmenuEscollirJoc(self):
        if self.menuEscollirJoc==False:
            self.menuEscollirJoc=pygame.Surface((300,300))
            self.menuEscollirJoc.fill(0x444400)
        return self.menuEscollirJoc
        
    def getfonsJoc(self):False
    
    def getCartaOculta(self):
        if self.oculta==False:
            self.oculta=pygame.image.load("Data/oculta.png").convert_alpha()
        return self.oculta;
    
    def generaPal(self, image):
        ret=list()
        for j in range(0,12):
            carta=pygame.Surface((CARTA_AMPLADA,CARTA_ALTURA), HWSURFACE|SRCALPHA)
            carta.blit(image,(0,0),pygame.Rect( j*CARTA_AMPLADA, 0, CARTA_AMPLADA, CARTA_ALTURA ))
            # carta.convert_alpha()
            ret.append(carta)
        return ret
            
            
    def getCarta(self,pal,num):
        if self.cartes==False:
            oros=pygame.image.load("Data/oros.png")
            copes=pygame.image.load("Data/copes.png")
            espases=pygame.image.load("Data/espases.png")
            bastos=pygame.image.load("Data/bastos.png")
            self.cartes=(self.generaPal(oros),self.generaPal(copes),self.generaPal(espases),self.generaPal(bastos))
            
            
         #   self.getCartaNull()
         #   self.getfont(1)
         #   self.cartes=list()
         #   for i in range(1,5):
         #       cartetes=list()
         #       for j in range(1,13):
                   # print "%d : %d" % (i,j)
         #           imatge=self.cartanull.copy()
         #           imatge.blit(self.fonts[1].render("P=%d - n=%d" % (i,j), True, (0,0,0)),(15,15))
         #           cartetes.append(imatge)
         #       self.cartes.append(cartetes)
#        print "%d - %d" % (pal, num)
#        print "%d :-: %d" % (len(self.cartes), len(self.cartes[pal-1]))
        return self.cartes[pal-1][num-1]
        #return pygame.Surface((CARTA_AMPLADA+6,CARTA_ALTURA+6),HWSURFACE|SRCALPHA)
        
    def getCartaNull(self):
        if self.cartanull==False:
            self.cartanull=pygame.image.load("Data/nula.png").convert_alpha()
           # self.cartanull=pygame.image.load("Data/base.png").convert_alpha()#pygame.Surface((120,170))
           # self.cartanull.fill(0xFFFFFF)
        return self.cartanull
    
    def getImatgeMarca(self):
        if self.imatgeMarca==False:
            """caracteristiques=pygame.Rect()
            caracteristiques.center=(3,3)
            self.imatgeMarca=pygame.Surface(caracteristiques,HWSURFACE|SRCALPHA)"""
            #self.imatgeMarca=pygame.Surface((CARTA_AMPLADA+6,CARTA_ALTURA+6),HWSURFACE|SRCALPHA)
            self.imatgeMarca=pygame.Surface((CARTA_AMPLADA+6,CARTA_ALTURA+6))
            self.imatgeMarca.fill(0xAA0000)
            self.imatgeMarca.get_rect().center=(3,3)
        return self.imatgeMarca
                    
                    
        
    