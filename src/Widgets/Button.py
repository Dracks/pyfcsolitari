import Widgets

class Button(Widgets.Empty):
    def __init__(self, image, text, font):
        Widgets.Empty.__init__(self)
        self.mouseOver=False
        self.font=font
        self.text=text
        self.bgImage=image
        self.texImage=font.render(text)
        self.onClickFunction=None
        self.offset=(0,0)
        self._update()

    def setOnMouseClick(self, f):
        self.onClickFunction=f;

    def update(self):
        self._update();

    def _update(self):
        imgSize=self.bgImage.getSize()
        texSize=self.texImage.getSize()
        self.offset=((imgSize[0]-texSize[0])/2,(imgSize[1]-texSize[1])/2)
        self.size=imgSize;
        #print "Offset", self.offset

    def onMouseMove(self, x, y):
        sx=x-self.px;
        sy=y-self.py;
        if sx>0 and sy>0 and sx<self.size[0] and sy<self.size[1]:
            self.mouseOver=True
        else:
            self.mouseOver=False

    def onMouseClick(self, button):
        #print "Hola"
        if self.mouseOver and self.onClickFunction!=None:
            self.onClickFunction(button);

    def draw(self):
        self.bgImage.draw(self.px, self.py, self.pz)
        self.texImage.draw(self.px+self.offset[0], self.py+self.offset[1], self.zNear());
