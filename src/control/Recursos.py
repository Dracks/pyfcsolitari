#
#  Recursos.py
#  Solitari
#
#  Created by Dracks on 17/08/08.
#  Copyright (c) 2008 __MyCompanyName__. All rights reserved.
#
import  pygame
from pygame.locals import *
import yaml
#CARTA_ALTURA=154;
#CARTA_AMPLADA=100; 
class Recursos:
    def __init__(self, theme):
        self.folder="Data/"+theme;
        self.config=yaml.load(file(self.folder+"/index.ythm",'rb').read())
        self.fonts=(False,False,False,False)
        self.imgBoto=False
        self.fonsMenu=False
        self.menuIdioma=False
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
                self.fonts=(self.fonts[0],pygame.font.Font(self.folder+"/"+self.config["fonts"]["middle"]["file"],self.config["fonts"]["middle"]["size"]),self.fonts[2], self.fonts[3])
            elif size==2:
                self.fonts=(self.fonts[0],self.fonts[1],pygame.font.Font(self.folder+"/"+self.config["fonts"]["large"]["file"],self.config["fonts"]["large"]["size"]), self.fonts[3])
            else:
                None
                
        return self.fonts[size]
            
    def getimgBoto(self):
        if self.imgBoto==False:
            self.imgBoto=pygame.image.load(self.folder+"/"+self.config["button"]).convert_alpha()
                
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
        
    def getmenuIdioma(self):
        if self.menuIdioma==False:
            self.menuIdioma=pygame.Surface((300,400))
            self.menuIdioma.fill(0x444400)
        return self.menuIdioma
        
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
            self.oculta=pygame.image.load(self.folder+"/"+self.config["cartas"]["hidden"]).convert_alpha()
        return self.oculta;
    
    def generaPal(self, image):
        ret=list()
        incrusta=self.config["carta"]["numbers"]["incrustat"]
        if incrusta:
            posicio_numero=(self.config["carta"]["numbers"]["x"],self.config["carta"]["numbers"]["y"])
        for j in range(0,12):
            carta=pygame.Surface((self.config["carta"]["width"],self.config["carta"]["height"]), HWSURFACE|SRCALPHA)
            carta.blit(image,(0,0),pygame.Rect( j*self.config["carta"]["width"], 0, self.config["carta"]["width"], self.config["carta"]["height"] ))
            if incrusta:
                carta.blit(self.fonts[1].render("%d" % (j+1),True,(0,0,0),posicio_numero))
            # carta.convert_alpha()
            ret.append(carta)
        return ret
            
            
    def getCarta(self,pal,num):
        if self.cartes==False:
            oros=pygame.image.load(self.folder+"/"+self.config["cartas"]["oros"])
            copes=pygame.image.load(self.folder+"/"+self.config["cartas"]["copas"])
            espases=pygame.image.load(self.folder+"/"+self.config["cartas"]["espadas"])
            bastos=pygame.image.load(self.folder+"/"+self.config["cartas"]["bastos"])
            self.cartes=(self.generaPal(oros),self.generaPal(copes),self.generaPal(espases),self.generaPal(bastos))
        return self.cartes[pal-1][num-1]
        
    def getCartaNull(self):
        if self.cartanull==False:
            self.cartanull=pygame.image.load(self.folder+"/"+self.config["cartas"]["null"]).convert_alpha()
        return self.cartanull
    
    def getImatgeMarca(self):
        if self.imatgeMarca==False:
            self.imatgeMarca=pygame.Surface((self.config["carta"]["width"]+6,self.config["carta"]["height"]+6))
            self.imatgeMarca.fill(0xAA0000)
            self.imatgeMarca.get_rect().center=(3,3)
        return self.imatgeMarca
                    
                    
        
    