#
#  Recursos.py
#  Solitari
#
#  Created by Dracks on 17/08/08.
#  Copyright (c) 2008 __MyCompanyName__. All rights reserved.
#

import ViewGL
import Image, ImageDraw, ImageFont
import yaml

class Font:
    def __init__(self, font, size):
        self.font=ImageFont.truetype(font, size);

    def render(self, text, color=(0,0,0)):
        size = self.font.getsize(text) # Returns the width and height of the given text, as a 2-tuple.
        im = Image.new('RGBA', size, (0, 0, 0, 0)) # Create a blank image with the given size
        draw = ImageDraw.Draw(im)
        draw.text((0, 0), text, font=self.font, fill=color) #Draw text
        return ViewGL.Image(im)

    def renderText(self, text, width, align,color=(0,0,0)):
        pass

#CARTA_ALTURA=154;
#CARTA_AMPLADA=100; 
class Recursos:
    def __init__(self, theme):
        self.folder="Data/"+theme;
        self.config=yaml.load(file(self.folder+"/index.ythm",'rb').read())
        print self.config;
        self.fonts=(False,False,False)
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
        
    def getfont(self,type):
        """
        Check cache and if don't has this font charge that
        @type type: number
        """
        if not self.fonts[type]:
            if type==1:
                self.fonts=(self.fonts[0], Font(self.folder+"/"+self.config["fonts"]["middle"]["file"],self.config["fonts"]["middle"]["size"]),self.fonts[2])
            elif type==2:
                self.fonts=(self.fonts[0], self.fonts[1], Font(self.folder+"/"+self.config["fonts"]["large"]["file"],self.config["fonts"]["large"]["size"]))
                
        return self.fonts[type]
            
    def getimgBoto(self):
        if not self.imgBoto:
            self.imgBoto=ViewGL.Image(Image.open(self.folder+"/"+self.config["button"]))
                
        return self.imgBoto
            
    def getfonsMenu(self):
        if not self.fonsMenu:
            self.fonsMenu=ViewGL.Drawable(1440, 900) #ViewGL.Drawable((1440,900))
            self.fonsMenu.setColor(0.1,0.4, 0.1)
        return self.fonsMenu
        
    def getmenuPrincipal(self):
        if not self.menuPrincipal:
            self.menuPrincipal=ViewGL.Drawable(300,400)
            self.menuPrincipal.setColor(0.3, 0.3, 0) #(0x444400)
        return self.menuPrincipal
        
    def getmenuIdioma(self):
        if not self.menuIdioma:
            self.menuIdioma=ViewGL.Drawable(300,400)
            self.menuIdioma.setColor(0.3, 0.3, 0)
        return self.menuIdioma
        
    def getmenuSortir(self):
        if not self.menuSortir:
            self.menuSortir=ViewGL.Drawable(500,200)
            self.menuSortir.setColor(0, 0.25, 0)
        return self.menuSortir
        
    def getPartidaGuardarCarregar(self):
        if not self.partidaGuardarCarregar:
            self.partidaGuardarCarregar=ViewGL.Drawable(500,30)
            self.partidaGuardarCarregar.setColor(0.3, 0.7, 0.05)
        return self.partidaGuardarCarregar

    def getmenuGuardariCarregar(self):
        if not self.menuGuardariCarregar:
            self.menuGuardariCarregar=ViewGL.Drawable(600,400)
            self.menuGuardariCarregar.setColor(0.3,0.3, 0)
        return self.menuGuardariCarregar
        
        
    def getmenuOpcions(self):
        return None

    def getmenuJoc(self):
        return None
    
    def getmenuPartida(self):
        return None
    
    def getPartidaFinalitzada(self):
        return self.getmenuSortir()

    def getmenuEscollirJoc(self):
        if not self.menuEscollirJoc:
            self.menuEscollirJoc=ViewGL.Drawable(300,300)
            self.menuEscollirJoc.setColor(0.3, 0.3, 0)
        return self.menuEscollirJoc
        
    def getfonsJoc(self):
        return False
    
    def getCartaOculta(self):
        if self.oculta==False:
            self.oculta=ViewGL.Image(Image.open(self.folder+"/"+self.config["cartas"]["hidden"]))
        return self.oculta;
    
    def generaPal(self, image):
        ret=list()
        #incrusta=self.config["carta"]["numbers"]["incrustat"]
        #if incrusta:
        #    posicio_numero=(self.config["carta"]["numbers"]["x"],self.config["carta"]["numbers"]["y"])
        for j in range(0,12):
            #carta=ViewGL.Drawable((self.config["carta"]["width"],self.config["carta"]["height"]), HWSURFACE|SRCALPHA)
            #carta.blit(image,(0,0),pygame.Rect( j*self.config["carta"]["width"], 0, self.config["carta"]["width"], self.config["carta"]["height"] ))
            box=(j*self.config["carta"]["width"], 0, (j+1)*self.config["carta"]["width"], self.config["carta"]["height"])
            carta=ViewGL.Image(image.crop(box))
            #if incrusta:
            #    carta.blit(self.fonts[1].render("%d" % (j+1),True,(0,0,0),posicio_numero))
            # carta.convert_alpha()
            ret.append(carta)
        return ret
            
            
    def getCarta(self,pal,num):
        if self.cartes==False:
            oros=Image.open(self.folder+"/"+self.config["cartas"]["oros"])
            copes=Image.open(self.folder+"/"+self.config["cartas"]["copas"])
            espases=Image.open(self.folder+"/"+self.config["cartas"]["espadas"])
            bastos=Image.open(self.folder+"/"+self.config["cartas"]["bastos"])
            self.cartes=(self.generaPal(oros),self.generaPal(copes),self.generaPal(espases),self.generaPal(bastos))
        return self.cartes[pal-1][num-1]
        
    def getCartaNull(self):
        if self.cartanull==False:
            self.cartanull=ViewGL.Image(Image.open(self.folder+"/"+self.config["cartas"]["null"]))
        return self.cartanull
    
    def getImatgeMarca(self):
        if self.imatgeMarca==False:
            self.imatgeMarca=ViewGL.Drawable(self.config["carta"]["width"]+6,self.config["carta"]["height"]+6)
            self.imatgeMarca.setColor(1.0, 0.0, 0.0)
            #self.imatgeMarca.get_rect().center=(3,3)
        return self.imatgeMarca
                    
                    
        
    