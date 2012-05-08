__author__ = 'dracks'

from Widgets import Empty

class Layout(Empty):
    """
        Abstract Class Layout for administrate the common functions between Vertical and Horizontal Layout
        It contain a list of elements
    """
    def __init__(self, margin=0):
        Empty.__init__(self);
        self.contentList=list()
        self.margin=margin
        self.overElement=False;
        self.nearElements=(-1,-1);

    def addElem(self,elem):
        self.contentList.append(elem)
        self.update();

    def onMouseMove(self, x, y):
        newOver=False;
        if (self.overElement!=False):
            self.overElement.onMouseMove(x,y)
            if self.overElement.checkMouseOver(x,y):
                newOver=self.overElement;

            elif self.checkMouseOver(x, y):
                for i in self.nearElements:
                    if i>-1 and i<len(self.contentList):
                        if (self.contentList[i].checkMouseOver(x,y)):
                            self.nearElements=(i-1,i+1);
                            newOver=self.contentList[i];

        else:
            if self.checkMouseOver(x,y):
                for i,e in enumerate(self.contentList):
                    if (e.checkMouseOver(x,y)):
                        self.nearElements=(i-1, i+1);
                        newOver=e;
                        break;

        self.overElement=newOver
        #print newOver;

    def onMouseClick(self, button):
        if self.overElement:
            self.overElement.onMouseClick(button)

    def onMouseDoubleClick(self, button):
        if self.overElement:
            self.overElement.onMouseDoubleClick(button)

    def update(self):
        for i in self.contentList:
            i.update()

    def setPosition(self, x, y, z):
        Empty.setPosition(self, x, y, z)
        self.update();

    """def getTamMin(self,xoy):
        tam=0
        for i in self.content:
            tam+=i.getTamany()[xoy]
        return tam"""

    def setMargin(self, margin):
        self.margin=margin

    def draw(self):
        for e in self.contentList:
            e.draw();

class VerticalLayout(Layout):
    """
        For dispose the elements int vertical
    """
    """def getTamMin(self):
        self.getTamMin(1)"""

    """def click(self,coordenades):
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
        return False"""

    def update(self):
        Layout.update(self);
        print "Debug VLayout", self.size;

        nextCoordinate=self.margin
        maxSize=0
        z=self.zNear();
        for e in self.contentList:

            e.setPosition(self.px,self.py+nextCoordinate, z);

            size=e.getSize()
            nextCoordinate+=size[1]+self.margin
            if maxSize<size[0]:
                maxSize=size[0]
        self.size=(maxSize,nextCoordinate)
        print "Debug VLayout", self.size;

class HorizontalLayout(Layout):
    """
        For dispose the elements in horizontal
    """
    """def getTamMin(self):
        self.getTamMin(0)"""

    """def click(self,coordenades):
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
                return False"""

    def update(self):
        Layout.update(self);

        nextCoordinate=self.margin
        maxSize=0
        z=self.zNear();
        for e in self.contentList:

            e.setPosition(self.px+nextCoordinate,self.py, z);

            size=e.getSize()
            nextCoordinate+=size[0]+self.margin
            if maxSize<size[1]:
                maxSize=size[1]
        self.size=(maxSize,nextCoordinate)

    """def update(self):
        desp=-self.sep
        max=0
        for i in self.content:
            i.update()
            tam=i.getTamany()
            desp+=tam[0]+self.sep
            if max<tam[1]:
                max=tam[1]
        self.tamany=(desp,max)"""
