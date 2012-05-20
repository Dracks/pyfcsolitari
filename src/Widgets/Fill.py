import Widgets

class Fill(Widgets.Empty):
    def __init__(self, size, parent):
        Widgets.Empty.__init__(self)
        self.sizeToFill=size
        assert (hasattr(parent, 'getChilds'))
        self.parent=parent

class VerticalFill(Fill):
    def getSize(self):
        listBrothers=self.parent.getChilds()
        sizeResultant=self.sizeToFill
        numFillObjects=0
        for brother in listBrothers:
            if not isinstance(brother,VerticalFill) and not isinstance(brother,HorizontalFill):
                sizeResultant-=brother.getSize()[1]
            elif isinstance(brother,VerticalFill):
                numFillObjects+=1

        assert(numFillObjects>0)
        if sizeResultant>0:
            return (0, sizeResultant/numFillObjects)
        if sizeResultant>0:
            return (0, sizeResultant)
        else:
            return (0,0)

class HorizontalFill(Fill):
    def getSize(self):
        listBrothers=self.parent.getChilds()
        sizeResultant=self.sizeToFill
        numFillObjects=0
        for brother in listBrothers:
            if not isinstance(brother,VerticalFill) and not isinstance(brother,HorizontalFill):
                sizeResultant-=brother.getSize()[0]
            elif isinstance(brother,HorizontalFill):
                numFillObjects+=1;
        assert(numFillObjects>0)
        if sizeResultant>0:
            return (0, sizeResultant/numFillObjects)
        else:
            return (0,0)

