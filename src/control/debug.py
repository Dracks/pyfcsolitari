#
#  proves.py
#  Solitari
#
#  Created by Dracks on 22/06/08.
#  Copyright (c) 2008 __MyCompanyName__. All rights reserved.
#
#from Proves import *
from view import *
from model import *
from control import *
from random import Random
#from control import Recursos
import  pygame

class Jocproves:
    def __init__(self):
        self.taulell= Taulell(8,4,1)

    def arrencaJoc(self):
        self.generaCartes()
        self.mourecartes()
        self.mostraPartida()
    
    def generaCartes(self):
        self.cartes= list()
        rand=Random()
        for i in range(1,4+1):
            for j in range(1,12+1):
                print "pal: %d numero: %d" % (i, j)
                self.cartes.append(Carta(j,i))
        # per cada pila, insertarem el numero de cartes necessaries
        for j in range(1,6+1):
            for i in range(1,8+1):
                k=len(self.cartes)-1
                if (k==0):
                    u=0;
                else:
                    u=rand.randint(0,k)
              #  print " j= %d i=%d longitud=%d valor=%d" % (j, i, k, u)
                carta=self.cartes.pop(u)
                carta.setVisible(i>j-1)
                self.taulell.ficaCartaColumna(carta,j)
                        
                    
    def mostraPartida(self):
        columnes=[]
        taulell=self.taulell
        max=0;
        for i in range(0,taulell.ncolumnes()):
            columnes.append(taulell.llistaCartesColumna(i))
            if (max<len(columnes[i])):
                max=len(columnes[i])
        print max
        i=0
        while i<max:
            linea=[]
            separador=""
           # print "------------------------------------------------"
            for j in range(1,taulell.ncolumnes()):
                if (len(columnes[j])>i):
                    separador=separador+"--------"
                    if (columnes[j][i].visible):
                        carta="| %d %d " % (columnes[j][i].pal,columnes[j][i].num)
                        if (len(carta)==6):
                            linea.append(carta+" |")
                        else:
                            linea.append(carta+"|")
                    else :
                        linea.append("| X XX |")
                else:
                    linea.append("        ")
                    separador=separador+"        "
            print separador
            print "".join(linea)
            i=i+1
        
    
    def mourecartes(self):
        self.taulell.mouCartesEntreColumnes(6,2,2)
        self.taulell.mouCartesEntreColumnes(1,7,6)
        
        print "echo"
        
class Jocproves3:
    def __init__(self):
        self.recursos=Recursos()
        self.interficie=Finestra((800,600))
        imatge1=self.recursos.getimgBoto().convert_alpha()
        font=self.recursos.getfont(1)
        font2=self.recursos.getfont(2)
        
        self.interficie.pushBackground(Imatge(self.recursos.getfonsMenu(),0))
        
        
   ############
   # Menu Principal!
   ###########     
        pla=VArea(0)
        pla.addElem(Centre(Imatge(font2.render("Menu principal", True, (100,100,100)),0), (300,35)))
        botons=VArea(15)
        pla.addElem(Centre(botons,(300,365)))
        imatge=pygame.Surface((300,400))
        contingut=Fons(Imatge(imatge,0), pla)
        imatge.fill(0x444400)
        menu=Centre(contingut,(800,600))
        self.interficie.setPrimerPla(menu)
        boto=Boto(imatge1, "Partida nova", font, 0)
        boto.setOnClick(self.aEscullirJoc, None)
        botons.addElem(boto)
        boto=Boto(imatge1, "Recuperar partida", font, 0)
        botons.addElem(boto)
        boto=Boto(imatge1, "Opcions", font, 0)
        botons.addElem(boto)
        self.menuPrincipal=menu
        boto=Boto(imatge1, "Surt del joc", font, 0)
        boto.setOnClick(self.sortir,1)
        botons.addElem(Ghost())
        botons.addElem(boto)
        self.interficie.showFPS(True)
        self.menuPrincipal=menu
        
        
    #############
    # Sortir?
    #############
        pla=VArea(0)
        pla.addElem(Centre(Imatge(font2.render("Esteu segurs?", True, (100,100,100)),0), (500,35)))
        content=VArea(15)
        pla.addElem(Centre(content,(500,145)))
        botons=HArea(20)
        content.addElem(Centre(Imatge(font.render("Esteu segurs de voler sortir?", True, (255,255,255)),0),(500,20)))
        content.addElem(Centre(botons,(500,40)))
        boto=Boto(imatge1, "Si", font, 0)
        boto.setOnClick(self.sortir,2)
        botons.addElem(boto)
        boto=Boto(imatge1, "No", font, 0)
        boto.setOnClick(self.sortir,0)
        botons.addElem(boto)
        imatge=pygame.Surface((500,200))
        imatge.fill(0x003300)
        contingut=Fons(Imatge(imatge,0),pla)
        self.preguntarSortida=Centre(contingut,(800,600))
        self.interficie.setFunctSortir(self.sortir,1)
        self.sortint=False
        menu.update()
        
    #############
    # Menu per escollir el tipus de joc
    #############
        pla=VArea(0)
        pla.addElem(Centre(Imatge(font2.render("Esculli el joc", True, (100,100,100)),0), (300,30)))
        botons=VArea(15)
        pla.addElem(Centre(botons,(300,270)))
        boto=Boto(imatge1, "Els 6 munts", font, 0)
        botons.addElem(boto)
        boto=Boto(imatge1, "Acordeo", font, 0)
        botons.addElem(boto)
        botons.addElem(Ghost())
        boto=Boto(imatge1, "Cancelar", font, 0)
        boto.setOnClick(self.aMenuPrincipal, None)
        botons.addElem(boto)
        imatge=pygame.Surface((300,300))
        imatge.fill(0x444400)
        contingut=Fons(Imatge(imatge,0),pla)
        self.escullirJoc=Centre(contingut,(800,600))
        self.escullirJoc.update()
        
        
    def executa(self):
        self.interficie.executa()
        
    def aMenuPrincipal(self,params):
        self.interficie.setPrimerPla(self.menuPrincipal)
        
    def acordeo(self):
        self.taulell=Taulell(6, 4, 0)
        self.joc=Acordeo(self, self.taulell)
        self.carregaPiles()
        
    def aEscullirJoc(self, params):
        self.interficie.setPrimerPla(self.escullirJoc)
        
    def sortir(self,params):
        if self.sortint==True and params==1:
            return
        if params==1:
            self.interficie.mostraFosc()
            self.interficie.pushBackground(self.interficie.getPrimerPla())
            self.interficie.setPrimerPla(self.preguntarSortida)
            self.sortint=True
        elif params==2:
            self.interficie.setSortir()
        elif params==0:
            self.interficie.ocultaFosc()
            self.interficie.setPrimerPla(self.interficie.popBackground())
            self.sortint=False
            
    def carregaPiles(self):
        self.accesdirecte=(list(),list(), Pila())   
        
                  
class Jocproves2:
    def __init__(self):
       # self.interficie=Interficie((800,600))
       # pila=Pila(0,(50,00),False,(-1,0),(-160,0))
       # self.menu=Menu()
        self.menu.addObject(pila)
        imatge1=pygame.image.load("Data/boto.png").convert_alpha()
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
        pila.addElem(elem(imatge1,(0,0)),(0,10))
    
    def executa(self):
        self.interficie.executa(self.menu)
        
        
        
    
        
    

