from view import Ghost
import pygame
from pygame.locals import *
from time import time;

class Scroll(Ghost):
    def __init__(self,dimensions,type=0):
        #print dimensions;
        self.size=dimensions;
        self.type=type;
        self.scroll=(0,0);
        self.content=False;
        self.zona=pygame.Surface(self.size, HWSURFACE)
        
        
    def assign(self,content):
        self.content=content;
    
    def getTamany(self):
        return self.size
    
    def getTamContents(self):
        return self.content.getTamany();
    
    def desplaca(self, (x,y)):
        self.scroll=(self.scroll[0]+x,self.scroll[1]+y)
        
    def getPos(self):
        return self.scroll;
        
    def pintals(self,llistat):
        for sublist in llistat:
            for e in sublist:
                self.zona.blit(e[0],e[1])

    def click(self,(x,y)):
       # print (x-self.scroll[0],y-self.scroll[1]);
        self.content.click((x+self.scroll[0],y+self.scroll[1]))
    
    def dobleclick(self, (x,y)):
        self.content.dobleclick((x+self.scroll[0],y+self.scroll[1]))
    
    def update(self):
        if self.content!=False:
            self.content.update();
    """
        @funcio: pinta
        @params: coordenades a pintar, mouse, profunditat
    """
    def pinta(self,objectes,posicio,(x,y),z):
        llistat=[list()]
        #t1=time()
       # print (posicio, (x,y), self.size)
        if posicio[0]>x or posicio[0]+self.size[0]<x:
            x=-self.scroll[0];
        if posicio[1]>y or posicio[1]+self.size[1]<y:
            y=-self.scroll[1]
        self.zona.fill(0x000000)
        self.content.pinta(llistat,(-self.scroll[0],-self.scroll[1]),(x-posicio[0],y-posicio[1]),0)
        #t2=time()
        self.pintals(llistat)
        #t3=time()
#        print (x-self.scroll[0],y-self.scroll[1]);
        objectes[z].append((self.zona,posicio))
        #print "temps z1:%f z2:%f z3:%f " % ((t2-t1),(t3-t2),(time()-t3))
        
        
        
        
        