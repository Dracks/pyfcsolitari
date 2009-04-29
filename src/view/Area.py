class Area:
    def __init__(self, separacio=0):
        self.content=list()
        self.sep=separacio
        self.tamany=(0,0)
        
    def addElem(self,elem):
        self.content.append(elem)
        
    def getTamany(self):
        return self.tamany
        
  #  def setTamany(self,tamany):
   #     self.tamany=tamany
    
    def getTamMin(self,xoy):
        tam=0
        for i in self.content:
            tam+=i.getTamany()[xoy]
        return tam
    
    def frame(self):
        for elem in self.content:
            elem.frame()
        
    def setSeparacio(self, separacio):
        self.sep=separacio

class VArea(Area):
    def getTamMin(self):
        self.getTamMin(1)
        
    def click(self,coordenades):
        for i in self.content:
            tam=i.getTamany()
            #print tam
            if coordenades[0]>0 and coordenades[1]>0:
                if coordenades[0]<tam[0] and coordenades[1]<tam[1]+self.sep:
                    return i.click(coordenades)
                else: 
                    coordenades=(coordenades[0], coordenades[1]-tam[1]-self.sep)
            else:
                return False
        return False
    
    def dobleclick(self,coordenades):
        for i in self.content:
            tam=i.getTamany()
            if coordenades[0]>0 and coordenades[1]>0:
                if coordenades[0]<tam[0] and coordenades[1]<tam[1]+self.sep:
                    return i.dobleclick(coordenades)
                else: 
                    coordenades=(coordenades[0], coordenades[1]-tam[1]-self.sep)
            else:
                return False
        return False
        
    def update(self):
       # print "hi"
        desp=-self.sep
        max=0
        for i in self.content:
            i.update()
            tam=i.getTamany()
            desp+=tam[1]+self.sep
            if max<tam[0]:
                max=tam[0]
        self.tamany=(max,desp)

    def pinta(self,sdl_surface, posicio,mouse, z):
        desp=-self.sep
        for i in self.content:
            desp+=self.sep
            i.pinta(sdl_surface, (posicio[0],posicio[1]+desp),mouse, z)
            desp+=i.getTamany()[1]
            
class HArea(Area):        
    def getTamMin(self):
        self.getTamMin(0)
        
    def click(self,coordenades):
        #print coordenades;
        for i in self.content:
            tam=i.getTamany()
            if coordenades[0]>0 and coordenades[1]>0:
                if coordenades[0]<(tam[0]+self.sep) and coordenades[1]<tam[1]:  # AIXO (+self.sep[]) DONARA PER EL CUL, MOLTTTT!!!!!! 
                    return i.click(coordenades)
                else: 
                    coordenades=(coordenades[0]-tam[0]-self.sep, coordenades[1])
            else:
                return False
                
    def dobleclick(self,coordenades):
        for i in self.content:
            tam=i.getTamany()
            if coordenades[0]>0 and coordenades[1]>0:
                if coordenades[0]<(tam[0]+self.sep) and coordenades[1]<tam[1]:  # AIXO (+self.sep[]) DONARA PER EL CUL, MOLTTTT!!!!!! 
                    return i.dobleclick(coordenades)
                else: 
                    coordenades=(coordenades[0]-tam[0]-self.sep, coordenades[1])
            else:
                return False
        
    def update(self):
        desp=-self.sep
        max=0
        for i in self.content:
            i.update()
            tam=i.getTamany()
            desp+=tam[0]+self.sep
            if max<tam[1]:
                max=tam[1]
        self.tamany=(desp,max)

    def pinta(self,sdl_surface, posicio, mouse, z):
        desp=-self.sep
        for i in self.content:
            desp+=self.sep
            i.pinta(sdl_surface, (posicio[0]+desp,posicio[1]), mouse ,z)
            desp+=i.getTamany()[0]
        