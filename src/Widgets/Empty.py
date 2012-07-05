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
        """
        @param x
        @type float
        @param y
        @type float
        @param z
        @type float
        """
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
        """

        """
        #p=self.getPosition()
        s=self.getSize();
        sx=x-self.px
        sy=y-self.py
        #print "CheckMouseOver Empty", self.getPosition(), self.getSize(), x, y
        return sx>0 and sy>0 and sx<s[0] and sy<s[1];

    def zFar(self, value=1):
        return self.pz-value;

    def zNear(self, value=1):
        return self.pz+value;

    def draw(self):
        pass