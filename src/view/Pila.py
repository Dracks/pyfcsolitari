from view import Ghost
from time import time
#import pygame

class Pila(Ghost):
    def __init__(self,senseelements=False,apartar=False,apartarmaxim=False, creixer=True, velositatDesplacament=1):
        self.posicio=(0,0) # on es colocara la llista (solucio Ylos)
        self.tam=(0,0) # tamany de la llista
        self.numero=0
        self.img_empty=senseelements
       # self.joc=joc    # Joc on esta jugant
        self.apartar=apartar
        self.maxdesp=apartarmaxim
        self.mouseover=False    # element sobre on esta el mouse
        self.despmouse=list()   # desplacament dels elements
        self.llista=list() # llista d'elements
        self.separacions=list() # llista de separacions entre cartes
        self.velositatDesplacament=velositatDesplacament # velositat que tindran les cartes al apartarse
        self.mostrar=list()  # si s'han de mostrar o no
        self.despacumulat=list() # indica l'acumulat que porten en el desplacament mouse
        self.onclick=False
        self.ondobleclick=False
        self.desplacament=True
        self.creixer=creixer
        self.deb=False
        self.timestamp=time()
        
    def getPosicio(self,p):
        ret=(0,0)
        for i in range(p):
            ret=(ret[0]+self.separacions[i][0], ret[1]+self.separacions[i][1])
        return ret
                
    def addElem(self,elem,separacio, mostrar):
        dim=self.getPosicio(self.numero)
        size=elem.getTamany()
        if (dim[0]+size[0])>self.tam[0]:
            self.tam=(dim[0]+size[0],self.tam[1])
            
        if ( dim[1]+size[1] )>self.tam[1]:
            self.tam=(self.tam[0],dim[1]+size[1])
        self.llista.append(elem)
        self.separacions.append(separacio)
        self.mostrar.append(mostrar)
        self.despmouse.append((0,0))
        self.despacumulat.append((0,0))
        self.numero+=1
        return self
        
    def getTamany(self):
        if self.creixer:
            return self.tam
        else:
            return self.img_empty.getTamany()
    
    def update(self):
        if self.numero==0:
            if not self.img_empty==False:
                self.img_empty.update()  # Per si les mosques!
                self.tam=self.img_empty.getTamany()
            else:
                self.tam=(0,0)
        else:
            pos=(0,0)
            max=(0,0)
            for i in range(self.numero):
                pos=(pos[0]+self.separacions[i][0],pos[1]+self.separacions[i][1])
                size=self.llista[i].getTamany()
                if (pos[0]+size[0])>max[0]:
                    max=(pos[0]+size[0],max[1])
                if (pos[1]+size[1])>max[1]:
                    max=(max[0],pos[1]+size[1])
               # self.despmouse[i]=(0,0)
            self.tam=max
    
    def addList(self, elem, separacions=False):
        self.llista.extend(elem[0])
        if separacions==False:
            self.separacions.extend(elem[1]) # Afegeixo les separacions que venien a la llista
        else:
            for i in range(len(elem[0])):
                self.separacions.append(separacions)    # o unes separacions fixes
        self.mostrar.extend(elem[2])
        for i in range(len(elem[0])):       # Afegeix els elements necessaris en la llista de desplacaments
            self.despmouse.append((0,0))
            self.despacumulat.append((0,0))
        self.numero=len(self.llista)
        self.update()
        
    def getLast(self):
        return (self.llista[self.numero-1], self.separacions[self.numero-1], self.mostrar[self.numero-1])
        
    def pop(self):
        if self.numero!=0:
            self.numero=self.numero-1;
            self.despacumulat.pop()
            return (self.llista.pop(),self.separacions.pop(), self.mostrar.pop())
    
    def setLast(self,elem):
        self.llista.pop()
        self.llista.append(elem[0])
        self.separacions.pop()
        self.separacions.append(elem[1])
        self.mostrar.pop()
        self.mostrar.append(elem[2])
        self.update()
        
    def subPila(self,posicio):
        ret=(self.llista[posicio:], self.separacions[posicio:], self.mostrar[posicio:])
        self.llista=self.llista[:posicio]
        self.separacions=self.separacions[:posicio]
        self.mostrar=self.mostrar[:posicio]
        self.numero=len(self.llista)
        self.despmouse=self.despmouse[:posicio]
        self.despacumulat=self.despacumulat[:posicio]
        self.update()
        return ret
    
    def getMouseOver(self):
        #if self.deb:
        #print "aqui >%i" % self.mouseover
        return self.mouseover
    
    def getEmpty(self):
        return self.img_empty
    
    def getAll(self):
        return self.llista
        
    def activaDesplacar(self):
        self.desplacament=True;
        
    def desactivaDesplacar(self):
        self.desplacament=False;
        
    def setOnClick(self, funct, params):
        self.onclick=funct
        self.onclick_params=params
    
    def setOnDobleClick(self, dobleclick):
        self.ondobleclick=dobleclick
    
    def click(self,(x,y)):
#        print "hi4"
        if not self.onclick==False:
            if not self.mouseover==False:
                self.onclick(self.onclick_params, self.mouseover)
    
    def dobleclick(self,(x,y)):
#        print "hi4"
        if not self.ondobleclick==False:
            if not self.mouseover==False:
                self.ondobleclick[0](self.ondobleclick[1], self.mouseover)
                
    def __len__(self):
       # print self.numero
        return self.numero
    
    def test(self, (x,y)):
        posicio=self.coordenades_actuals;
        if (x<posicio[0] or y < posicio[1]):
            return False
        if(x>posicio[0]+self.tam[0] or y>posicio[1]+self.tam[1]):
            return False
        return True;
        
    def frame2(self, posicio, (x,y), time2):
        self.coordenades_actuals=posicio;
        if (x<posicio[0] or y < posicio[1]):
            self.mouseover=False
            for i in range(self.numero):
                self.despmouse[i]=(0,0)
                self.despacumulat[i]=(0,0)
            return
        if(x>posicio[0]+self.tam[0] or y>posicio[1]+self.tam[1]):
            self.mouseover=False
            for i in range(self.numero):
                self.despmouse[i]=(0,0)
                self.despacumulat[i]=(0,0)
            return
        if self.desplacament==False:
            self.mouseover=(self.numero+1,(0,0))
           # print "passem %i" % self.mouseover
            return
        ultima=False
        pos=posicio
        for i in range(self.numero):
            if x>pos[0] and y>pos[1]:
                tam=self.llista[i].getTamany()
                if x<pos[0]+tam[0] and y<pos[1]+tam[1]:
                    ultima=(i+1,(x-pos[0],y-pos[1])) # es aquesta, per tant agafem la carta i li fiquem les coordenades on em clicat
            pos=(pos[0]+self.separacions[i][0],pos[1]+self.separacions[i][1])
        if ultima!=False:
            self.mouseover=ultima;
        mostrar=False
        
        factor=(time2-self.timestamp)*60*self.velositatDesplacament
        
        for i in range(self.numero):
            desp=self.despmouse[i]
            if self.mouseover==False or i<self.mouseover[0] or self.apartar==False or not mostrar:
                desp=(0,0)
                self.despacumulat[i]=(0,0)
            else:
                acumulat=self.despacumulat[i]
                acumulat=(acumulat[0]+(self.apartar[0]*factor),acumulat[1]+(self.apartar[1]*factor))
                self.despacumulat[i]=acumulat
                desp=(int(acumulat[0]), int(acumulat[1])) # No n'estic gaire segur d'aixo...
                if abs(desp[0])>abs(self.maxdesp[0]):
                    desp=(self.maxdesp[0],desp[1])
                if abs(desp[1])>abs(self.maxdesp[1]):
                    desp=(desp[0],self.maxdesp[1])
            self.despmouse[i]=desp
            mostrar=self.mostrar[i]
    
    def pinta(self,sdl_surface,coordenades,mouse, z):
        pos=coordenades
        time2=time()
        self.frame2(coordenades,mouse, time2)
        self.timestamp=time2
           # print "aqui %i (%i,%i)" % (self.mouseover,self.tam[0],self.tam[1])
            
        if self.numero==0:
            if not self.img_empty==False:
                self.img_empty.pinta(sdl_surface,coordenades,mouse,z)
              #  print self.mouseover
        else:
            for i in range(self.numero):
                if False != self.mouseover:
                    if i == self.mouseover[0]:
                        while (len(sdl_surface))<z+10+i:
                            #print "hi"
                            sdl_surface.append(list())
                        z=z+9
                #print self.despmouse[i][0]
                self.llista[i].pinta( sdl_surface, (pos[0]+self.despmouse[i][0], pos[1]+self.despmouse[i][1]),mouse, z+i)
                pos=(pos[0]+self.separacions[i][0],pos[1]+self.separacions[i][1])  