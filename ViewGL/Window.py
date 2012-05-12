__author__ = 'dracks'


from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from time import time;

class Window:
    def __init__(self, width, height, name):
        self.listObjects=[];
        self.worldx=0.0;
        self.worldy=0.0;
        self.width=width;
        self.height=height;
        self.delegate=None;
        self.count=0;
        self.lastStep=time();
        self.lastPosition=False;

        self.firstLayer=False
        self.FPSFunction=None
        self.FPSImage=None

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        glutInitWindowSize(width,height)
        glutInitWindowPosition(0,0)

        glutCreateWindow(name)

        glutKeyboardFunc(self.keyboard)
        glutSpecialFunc(self.keyboard)

        glutMouseFunc(self.mouse)

        glutReshapeFunc(self.reshape)

        glutDisplayFunc(self.draw)

        glutIdleFunc (self.idleFunction);

        glutPassiveMotionFunc(self.mouseMove);

        #glutCheckLoop()

    def pushView(self, view):
        self.listObjects.append(view)
        self.firstLayer=view

    def popView(self):
        self.listObjects.pop();
        if len(self.listObjects):
            self.firstLayer=self.listObjects[-1]
        else:
            self.firstLayer=False;

    #def addObject(self, obj):
    #    self.listObjects.append(obj)

    def setDelegate(self, delegate):
        self.delegate=delegate;

    def setFPSFunction(self, fun):
        self.FPSFunction=fun;

    def keyboard(self, *event):
        glutPostRedisplay();

    def mouseMove(self, x, y):
        #for i in self.listObjects:
        #    i.onMouseMove(x,y);
        self.firstLayer.onMouseMove(x,y);
        self.lastPosition=(x,y);
        glutPostRedisplay()

    def mouse(self, button, state, x, y):
        #for i in self.listObjects:
        #    i.onMouseClick(button);
        if self.firstLayer!=False:
            self.firstLayer.onMouseClick(button);
        glutPostRedisplay()

    def reshape(self, width, height):
        self.width=width;
        self.height=height;
        glutPostRedisplay()

    def idleFunction(self):
        tmpTime=time();
        self.count+=1
        if (tmpTime-self.lastStep>1.0):
            #print self.count
            if self.FPSFunction!=None:
                self.FPSImage=self.FPSFunction(self.count)
            else:
                self.FPSImage=None;
            self.lastStep=tmpTime;
            self.count=0;
        glutPostRedisplay();

    def run(self):
        glutMainLoop()
        return

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT);

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        glViewport(0, 0, self.width, self.height)
        #gluOrtho2D(0.0, self.width, self.height, 0.0)
        glOrtho (0.0, self.width, self.height, 0.0, -100.0, 100.0);
        #gluPerspective(45, float(self.width)/self.height, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();

        # Enable z-buffer
        glEnable(GL_BLEND)
        glEnable(GL_DEPTH_TEST);
        glEnable(GL_ALPHA_TEST);

        glDepthMask(GL_TRUE);
        glDepthFunc(GL_LESS);

        glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA);
        glAlphaFunc(GL_GREATER, 0.1);


        glTranslatef(self.worldx, self.worldy, 0.0);
        if self.FPSImage!=None:
            self.FPSImage.draw(0,0,80);
        glScale(1.0, 1.0, len(self.listObjects)*0.001)
        for i in self.listObjects:
            glTranslatef(0.0, 0.0, 100);
            i.draw();
        glutSwapBuffers();