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



    def addObject(self, obj):
        self.listObjects.append(obj)

    def setDelegate(self, delegate):
        self.delegate=delegate;

    def keyboard(self, *event):
        glutPostRedisplay();

    def mouseMove(self, x, y):
        for i in self.listObjects:
            i.onMouseMove(x,y);
        glutPostRedisplay()

    def mouse(self, button, state, x, y):
        for i in self.listObjects:
            i.onMouseClick(button);
        glutPostRedisplay()

    def reshape(self, width, height):
        self.width=width;
        self.height=height;
        glutPostRedisplay()

    def idleFunction(self):
        tmpTime=time();
        self.count+=1
        if (tmpTime-self.lastStep>1.0):
            print self.count
            self.lastStep=tmpTime;
            self.count=0;

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
        for i in self.listObjects:
            i.draw();
        glutSwapBuffers();