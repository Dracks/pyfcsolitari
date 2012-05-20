from Widgets import Empty

class Scroll(Empty):
    def __init__(self, size):
        Empty.__init__(self)
        self.size=size
        self.offset=(0,0)
        self.contents=Empty()

    def setPosition(self, x, y, z):
        Empty.setPosition(self, x,y,z)
        self._update()
        #self.contents.setPosition(x-self.offset[0], y-self.offset[1], self.zFar(40))

    def update(self):
        self.contents.update()
        self._update()

    def _update(self):
        self.contents.setPosition(self.px-self.offset[0], self.py-self.offset[1], self.zFar(40))

    def onMouseClick(self, button):
        self.contents.onMouseClick(button)

    def onMouseDoubleClick(self, button):
        self.contents.onMouseDoubleClick(button)

    def addOffset(self, offset):
        self.offset=(self.offset[0]+offset[0], self.offset[1]+offset[1])

    def onMouseMove(self, x, y):
        sx=x-self.px
        sy=y-self.py
        if sx>0 and sy>0 and sx<self.size[0] and sy<self.size[1]:
            self.contents.onMouseMove(x-self.offset[0],y-self.offset[1])

    def draw(self):
        self.contents.draw()
