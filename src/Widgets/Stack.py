
import Widgets
import ViewGL.Window

class FactoryAnimation:
    def __init__(self, c):
        assert(False)

    def getInstance(self, e):
        """
        @param e: element to animate
        @type e:Widgets.Empty
        @rtype: Widgets.Animation
        @return InstanceAnimation
        """
        assert(False)
        return None

class Animation:
    def __init__(self, widget, window):
        """
        @type widget:Widgets.Empty
        @param widget:
        @type window:ViewGL.Window
        @param window:
        @return:
        """
        self.widget=widget
        self.window=window

    def timeElapsed(self, t):
        assert(False)

    def clear(self):
        assert(False)

class OffsetAnimation(Animation):
    def __init__(self, widget, window, offset, velocity, type='lineal'):
        """
        @param widget:
        @type widget: Widgets.Empty
        @param window:
        @type window: ViewGL.Window
        @param offset:
        @type offset:Record
        @param type:
        @type type:string
        @return:
        """
        Animation.__init__(widget, window)
        self.offset=offset
        self.type=type
        self.velocity=velocity
        self.time=0
        self.origin=self.widget.getPosition()

    def timeElapsed(self, t):
        """

        @param t:
        @type t: int
        @return:
        """
        self.time+=t
        if self.time<0:
            self.time=0;
        offsetX=self.velocity[0]*self.time
        offsetY=self.velocity[1]*self.time
        endx=False
        endy=False
        if offsetX>self.offset[0]:
            offsetX=self.offset[0]
            endx=True
        if offsetY>self.offset[1]:
            offsetY=self.offset[1]
            endy=True

        return endx and endy


    def clear(self):
        self.widget.setPosition(self.origin[0], self.origin[1], self.origin[2])




class Stack(Widgets.Empty):
    """
    @type self.showEmpty: Widgets.Empty
    """
    def __init__(self, emptyShow=Widgets.Empty()):
        """

        @param emptyShow:
        @type emptyShow:Widgets.Empty
        @return:
        """
        Widgets.Empty.__init__(self)
        self.showEmpty=emptyShow
        self.listElements=[]
        self.__update()
        #self.listElements=

    def addElement(self, element, showSpace, show):
        """

        @param element:
        @type element: Widgets.Empty
        @param showSpace:
        @type showSpace: (number, number)
        @param show:
        @type show: boolean
        """
        self.listElements.append({'element':element, 'showSpace':showSpace, 'show': show})
        #self.listShow.append(show)
        #self.listShowSpace.append(showSpace)

        self.__update()

    def update(self):
        for i in self.listElements:
            i.update()
        self.__update()

    def __update(self):
        p=self.getPosition()

        self.showEmpty.setPosition(p[0], p[1], p[2])
        if len(self.listElements)==0:
            self.size=self.showEmpty.getSize()
        else:
            pos={'x':0, 'y':0}
            max={'w':0, 'h':0}
            count=0;
            for dict in self.listElements:
                size=dict['element'].getSize()
                if pos['x']+size[0]>max['w']:
                    max['w']=pos['x']+size[0]
                if pos['y']+size[1]>max['h']:
                    max['h']=pos['y']+size[1]
                dict['element'].setPosition(p[0]+pos['x'],p[1]+pos['y'], self.zNear(count))
                count+=1
                pos['x']+=dict['showSpace'][0]
                pos['y']+=dict['showSpace'][1]
            self.size=(max['w'], max['h'])

    def getLast(self):
        """

        @return: dictionary of last element
        @rtype: {element, showSpace, show}
        """
        return self.listElements[-1]

    def setLast(self, element):
        """

        @param element:
        @type element:{element, showSpace, show}
        """
        assert element.hasKey('element')
        assert element.hasKey('showSpace')
        assert element.hasKey('show')
        self.listElements[-1]=element

    def subStack(self, position):
        ret=self.listElements[position:]
        self.listElements=self.listElements[:position]
        self.__update()
        return ret

    def draw(self):
    #print "Debuggin Layout ", self.size, self.px, self.py, self.pz;
        for e in self.listElements:
            #print e
            e['element'].draw();