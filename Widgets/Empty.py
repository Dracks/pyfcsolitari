__author__ = 'dracks'


class Empty:
    def __init__(self):
        self.px=0
        self.py=0
        self.pz=-10
        self.size=(0,0);
        self.parent=False

    def update(self):
        pass;

    def getPosition(self):
        return (self.px, self.py, self.pz)

    def setPosition(self, x, y, z):
        self.px=x
        self.py=y
        self.pz=z

    def setParentElement(self, parent):
        self.parent=parent

    def addElement(self, elem):
        assert(False);

    def setElement(self, elem):
        assert(False);

    def getSize(self):
        return self.size;

    def onMouseMove(self, x, y):
        pass

    def onMouseClick(self, button):
        pass

    def onMouseDoubleClick(self, button):
        pass

    def checkMouseOver(self, x, y):
        p=self.getPosition()
        s=self.getSize();
        return x>p[0] and y>p[1] and x<p[0]+s[0] and y<p[1]+s[1];


    def zFar(self):
        return self.pz-1;

    def zNear(self):
        return self.pz+1;

    def draw(self):
        pass