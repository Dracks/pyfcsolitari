__author__ = 'dracks'
from Widgets import Empty

class Image(Empty):
    def __init__(self, image):
        """
        @param imatge ViewGL.Image
        """
        Empty.__init__(self);
        self.image=image;

    def getSize(self):
        return self.image.getSize();

    def draw(self):
        self.image.draw(self.px, self.py, self.pz)