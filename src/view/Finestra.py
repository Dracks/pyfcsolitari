import pygame
from pygame.locals import *
from time import time,sleep
#import time

class Finestra:
    def __init__(self, tamany, color=0x000000, alfa=170, tempsDobleClick=1):
        self.background=list()
        self.primerpla=False
        self.tamany=tamany
        self.sortir=False
        self.onSortir=False
        self.shortcurt=False
        
        pygame.init()
        pygame.font.init()
#        self.contingut=pygame.display.set_mode(tamany,FULLSCREEN|DOUBLEBUF)
        self.contingut=pygame.display.set_mode(tamany, DOUBLEBUF|HWSURFACE)
        
        self.capa=pygame.Surface(tamany,HWSURFACE)#.convert_alpha()
        self.capa.set_alpha(alfa)
        self.capa.fill(color)
        self.buffer=pygame.Surface(self.tamany,HWSURFACE)
        self.mostraCapa=0
        self.fps=False
        self.mouse=False
        
        self.forFrame=False
        self.onMouseMove=False
        
        self.button=(0,0,False)
        self.tempsDobleClick=tempsDobleClick
        
    def setPrimerPla(self, pla):
        self.primerpla=pla
        
    def getPrimerPla(self):
        return self.primerpla
        
    def pushBackground(self, background):
        self.background.append(background)
        
    def popBackground(self):
        return self.background.pop()
        
    def mostraFosc(self):
        self.mostraCapa+=1
    
    def ocultaFosc(self):
        self.mostraCapa-=1
        
    def tancar(self):
        self.sortir=True
        
    def setFunctSortir(self, funcio, params):
        self.onSortir=(funcio, params)
        
    def unsetSortir(self):
        self.onSortir=False
        
    def showFPS(self,bool):
        self.fps=bool;
        
    def setSortir(self):
        self.sortir=True
        
    def setMouse(self,mouse):
        self.mouse=mouse
        
    def getMouse(self):
        return self.mouse
    
    def setOnMouseMove(self, funcio):
        self.onMouseMove=funcio
        
    def setForFrame(self, funcs):
        self.forFrame=funcs;
        
    def setTitle(self, name):
        pygame.display.set_caption(name)
        
    def setIcon (self, name):
        pygame.display.set_icon(pygame.image.load(name))
    
    def setShortCut(self, func):
        self.shortcurt=func
        
    def pinta(self,llistat):
        for sublist in llistat:
            for e in sublist:
#                self.contingut.blit(e[0],e[1])
                self.buffer.blit(e[0],e[1])
                
        self.contingut.blit(self.buffer,(0,0))
        
    def executa(self):
        t1=time()
        fps=1
        font_fps=pygame.font.Font(None,15)
        img_fps=font_fps.render("%d" % 0,0,(255,255,255))
        t20=t1;
        while not self.sortir:
            for even in pygame.event.get():
                if even.type == pygame.QUIT:
                    if not self.onSortir==False:
                        self.onSortir[0](self.onSortir[1])
                    else: self.sortir=True
                elif even.type == pygame.MOUSEBUTTONDOWN:
                    t=time()
                    #print pygame.mouse.get_pos();
                    if t-self.button[1]>self.tempsDobleClick and self.button[2]==False:
                        self.primerpla.click(pygame.mouse.get_pos())
                        self.button=(even.button,time(), True);
                    elif self.button[0]==even.button and time()-self.button[1]<self.tempsDobleClick:
                      #  print "hello"
                        self.primerpla.dobleclick(pygame.mouse.get_pos())
                        
                elif even.type == pygame.MOUSEBUTTONUP:
                    if self.button[0]==even.button:
                        self.mouse.unClick()
                        self.button=(self.button[0], self.button[1], False);
                elif even.type == pygame.MOUSEMOTION:
                    if self.onMouseMove!= False:
                        self.onMouseMove(pygame.mouse.get_pos())
              #  elif even.type == pygame.KEYDOWN:
               #     if self.shortcurt!= False:
                #        self.shortcurt[0](event.key)
                   # if self.text!=False:
                    #    self.text[0](event.key)
                    #None
            if self.forFrame!=False:
                self.forFrame[0](self.forFrame[1])
           # self.mouse.frame()
           # self.primerpla.frame()
            t21=time()
            llistat1=list()
            z=0;
            for elem in self.background:
                llistat1.append(list())
                elem.pinta(llistat1,(0,0),(-1,-1),z)
                z=z+1
            if self.mostraCapa>0:
                llistat1.append([(self.capa,(0,0))])
                #self.contingut.blit(self.capa,(0,0))
            llistat2=[list()]
            
            self.primerpla.pinta(llistat2,(0,0),pygame.mouse.get_pos(),0)
           # print llistat2;
            llistat2.append(list())
            self.mouse.pinta(llistat2,len(llistat2)-1)
            t22=time()
            if self.fps==True:
                t2=time()
                if (t2-t1<1):
                    fps+=1;
                else:
                    img_fps=font_fps.render("%d" % fps,0,(0,0,0))
                    fps=1
                    t1=t2
                llistat2.append([(img_fps,(10,10))])
            t23=time()
            self.pinta(llistat1+llistat2)
            pygame.display.update()
            t24=time()
            ac1=t21-t20
            ac2=t22-t21
            ac3=t23-t22
            ac4=t24-t23
            t20=t24
            #sleep(0.5)
        print "Events: %f\nMontar: %f\nExtres: %f\nPintar: %f" % (ac1/(ac1+ac2+ac3+ac4),ac2/(ac1+ac2+ac3+ac4),ac3/(ac1+ac2+ac3+ac4),ac4/(ac1+ac2+ac3+ac4))
