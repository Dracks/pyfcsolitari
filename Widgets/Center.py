__author__ = 'dracks'

from Widgets import Empty

class Center(Empty):
    def __init__(self, surface):
        Empty.__init__(self)
        self.surface=surface
        self.mouseOverBool=False;
        self.contentsSize=(0,0)
        self.contents=Empty();

    def setElement(self, elem):
        elem.setParentElement(elem)
        self.contents=elem
        self.update()

    def setSurface(self, surface):
        self.surface=surface
        self.update()

    def getSize(self):
        return self.size

    def onMouseMove(self, x, y):
        self.contents.onMouseMove(x, y)
        self.mouseOverBool=self.contents.checkMouseOver(x,y)


    def onMouseClick(self, button):
        if self.mouseOverBool:
            self.contents.onMouseClick(button)

    def onMouseDoubleClick(self, button):
        if self.mouseOverBool:
            self.contents.onMouseDoubleClick(button)

    def setPosition(self, x, y, z):
        Empty.setPosition(self, x, y, z)
        self.update();

    def update(self):
        #self.contents.update();
        size=self.contents.getSize()
        print "Debug Center ", size;
        self.contents.setPosition(self.px+(self.surface[0]-size[0])/2, self.py+(self.surface[1]-size[1])/2, self.zNear())
        self.size=self.surface;
        if (self.surface[0]<size[0]):
            self.size=(size[0],self.size[1])

        if (self.surface[1]<size[1]):
            self.size=(self.size[0], size[1])

        self.contentsSize=size;

    def draw(self):
        self.contents.draw();