
from Widgets import Empty

class Stack(Empty):
    def __init__(self, emptyShow=Empty(), separate=0, maxSeparate=0, increase=True, velocity=1):
        Empty.__init__(self)
        self.imgEmpty=emptyShow
        self.separate=separate
        self.maxSeparate=maxSeparate
        self.increase=increase
        self.velocity=velocity

        #self.listElements=