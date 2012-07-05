__author__ = 'dracks'

from Widgets import Empty

class Center(Empty):
    def __init__(self, surface, contents=Empty()):
        Empty.__init__(self)
        self.surface=surface
        self.mouseOverBool=False
        self.contentsSize=(0,0)
        self.offset=(surface[0]/2,surface[1]/2)
        self.contents=contents

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
        self.mouseOverBool=self.contents.checkMouseOver(x, y)
        print "MouseMove- Center", self.mouseOverBool


    def onMouseClick(self, button):
        #print "MouseClick- Center", button
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
        self.size=self.surface;
        if (self.surface[0]<size[0]):
            self.size=(size[0],self.size[1])

        if (self.surface[1]<size[1]):
            self.size=(self.size[0], size[1])

        print "Debug Center ", size, self.surface;
        self.offset=((self.surface[0]-size[0])/2, (self.surface[1]-size[1])/2)
        self.contents.setPosition(self.px+self.offset[0], self.py+self.offset[1], self.zNear())

        self.contentsSize=size;

    def draw(self):
        self.contents.draw();