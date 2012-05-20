from Widgets import Empty

class Background(Empty):
    def __init__(self):
        Empty.__init__(self)
        self.background=Empty()
        self.foreground=Empty()

    def setForeground(self, fg):
        self.foreground=fg
        self.__update()

    def setBackground(self, bg):
        self.background=bg
        self.__update()

    def onMouseMove(self, x, y):
        self.foreground.onMouseMove(x,y)

    def onMouseClick(self, button):
        self.foreground.onMouseClick(button)

    def onMouseDoubleClick(self, button):
        self.foreground.onMouseDoubleClick(button)

    def update(self):
        self.background.update()
        self.foreground.update()
        self.__update();

    def __update(self):
        bgsize=self.background.getSize();
        fgsize=self.foreground.getSize();
        if bgsize[0]<fgsize[0]:
            bgsize=(fgsize[0], bgsize[1])
        if bgsize[1]<fgsize[1]:
            bgsize=(bgsize[0], fgsize[1])

        self.size=bgsize;

    def setPosition(self, x, y, z):
        self.background.setPosition(x,y,z)
        self.foreground.setPosition(x,y,self.zNear(10))

    def draw(self):
        self.background.draw()
        self.foreground.draw()