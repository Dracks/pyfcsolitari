from view import Ghost
import pygame

class Pila(Ghost):
    def __init__(self,senseelements=False,apartar=False,apartarmaxim=False):
        self.posicio=(0,0) # on es colocara la llista (solucio Ylos)
        self.tam=(0,0) # tamany de la llista
        self.numero=0
        self.img_empty=senseelements
       # self.joc=joc    # Joc on esta jugant
        self.apartar=apartar
        self.maxdesp=apartarmaxim
        self.mouseover=False    # element sobre on esta el mouse
        self.despmouse=list()
        self.llista=list() # llista de cartes
        self.separacions=list() # llista de separacions entre cartes
        self.mostrar=list()
        self.onclick=False
        self.desplacament=True
        
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
        self.numero+=1
        return self
        
    def getTamany(self):
        return self.tam
    
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
    
    def addList(self, elem):
        self.llista.extend(elem[0])
        self.separacions.extend(elem[1])
        self.mostrar.extend(elem[2])
        for i in range(len(elem[0])):
            self.despmouse.append((0,0))
        self.numero=len(self.llista)
        self.update()
        
    def getLast(self):
        return (self.llista[self.numero-1], self.separacions[self.numero-1], self.mostrar[self.numero-1])
    
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
        self.update()
        return ret
    
    def getMouseOver(self):
        return self.mouseover
        
    def activaDesplacar(self):
        self.desplacament=True;
        
    def desactivaDesplacar(self):
        self.desplacament=False;
        
    def setOnClick(self, funct, params):
        self.onclick=funct
        self.onclick_params=params
    
    def click(self,(x,y)):
        if not self.onclick==False:
            if not self.mouseover==False:
                self.onclick(self.onclick_params, self.mouseover)
           
    def frame(self):
        #print "Hola?"
        #self.posicio=coordenades;
        (x,y)=pygame.mouse.get_pos()
        if (x<self.posicio[0] or y < self.posicio[1]):
            self.mouseover=False
            for i in range(self.numero):
                self.despmouse[i]=(0,0)
            return
        if(x>self.posicio[0]+self.tam[0] or y>self.posicio[1]+self.tam[1]):
            self.mouseover=False
            for i in range(self.numero):
                self.despmouse[i]=(0,0)
            return
        if self.desplacament==False:
            self.mouseover=-1
            return
            
        ultima=False
        pos=self.posicio
        for i in range(self.numero):
            if (x>pos[0] and y>pos[1]):
                tam=self.llista[i].getTamany()
                if (x<(pos[0]+tam[0]) and y<(pos[1]+tam[1])): # significa que esta dins
                    ultima=i+1
            pos=(pos[0]+self.separacions[i][0],pos[1]+self.separacions[i][1])
        self.mouseover=ultima;
      #  return ultima
        mostrar=False
        for i in range(self.numero):
            desp=self.despmouse[i]
            if self.mouseover==False or i<self.mouseover or self.apartar==False or not mostrar:
                desp=(0,0)
            else:
                desp=(desp[0]+self.apartar[0],desp[1]+self.apartar[1])
                if abs(desp[0])>abs(self.maxdesp[0]):
                    desp=(self.maxdesp[0],desp[1])
                if abs(desp[1])>abs(self.maxdesp[1]):
                    desp=(desp[0],self.maxdesp[1])
            self.despmouse[i]=desp
            mostrar=self.mostrar[i]
    
    def pinta(self,sdl_surface,coordenades, z):
        pos=coordenades
        self.posicio=coordenades # Solucio Ylos
        #self.frame()
        (x,y)=pygame.mouse.get_pos()
        if (x<self.posicio[0] or y < self.posicio[1]):
            self.mouseover=False
            for i in range(self.numero):
                self.despmouse[i]=(0,0)
            return
        if(x>self.posicio[0]+self.tam[0] or y>self.posicio[1]+self.tam[1]):
            self.mouseover=False
            for i in range(self.numero):
                self.despmouse[i]=(0,0)
            return
        if self.desplacament==False:
            self.mouseover=-1
            return
            
        ultima=False
        pos=self.posicio
        for i in range(self.numero):
            if (x>pos[0] and y>pos[1]):
                tam=self.llista[i].getTamany()
                if (x<(pos[0]+tam[0]) and y<(pos[1]+tam[1])): # significa que esta dins
                    ultima=i+1
            pos=(pos[0]+self.separacions[i][0],pos[1]+self.separacions[i][1])
        self.mouseover=ultima;
      #  return ultima
        mostrar=False
        for i in range(self.numero):
            desp=self.despmouse[i]
            if self.mouseover==False or i<self.mouseover or self.apartar==False or not mostrar:
                desp=(0,0)
            else:
                desp=(desp[0]+self.apartar[0],desp[1]+self.apartar[1])
                if abs(desp[0])>abs(self.maxdesp[0]):
                    desp=(self.maxdesp[0],desp[1])
                if abs(desp[1])>abs(self.maxdesp[1]):
                    desp=(desp[0],self.maxdesp[1])
            self.despmouse[i]=desp
            mostrar=self.mostrar[i]
            
            
        if (len(sdl_surface)-1)==z:
            sdl_surface.append(list())
        if self.numero==0:
            if not self.img_empty==False:
                self.img_empty.pinta(sdl_surface,coordenades,z)
        else:
            for i in range(self.numero):
                if i == self.mouseover:
                    z=z+1
                self.llista[i].pinta(sdl_surface,(pos[0]+self.despmouse[i][0], pos[1]+self.despmouse[i][1]),z)
                pos=(pos[0]+self.separacions[i][0],pos[1]+self.separacions[i][1])  