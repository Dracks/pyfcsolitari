__author__ = 'dracks'


from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

class Window:
    def __init__(self, width, height, name):
        self.listObjects=[];
        self.worldx=0.0;
        self.worldy=0.0;
        self.width=width;
        self.height=height;
        self.delegate=None;

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

        #glutCheckLoop()



    def addObject(self, obj):
        self.listObjects.append(obj)

    def setDelegate(self, delegate):
        self.delegate=delegate;

    def keyboard(self, *event):
        glutPostRedisplay();

    def mouse(self, button, state, x, y):
        #for i in self.listObjects:
        #    i.mouse(button, state, x, y);
        glutPostRedisplay()

    def reshape(self, width, height):
        self.width=width;
        self.height=height;
        glutPostRedisplay()

    def run(self):
        glutMainLoop()
        return

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT);


        #glMatrixMode(GL_PROJECTION);
        #glLoadIdentity();
        #glOrtho (0.0, self.width, self.height, 0.0, -10.0, 10.0);
        #glMatrixMode(GL_MODELVIEW);
        #glLoadIdentity()


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
        #glDepthFunc(GL_LESS);
        """glDepthMask(GL_TRUE);
        glEnable(GL_CULL_FACE);

        glEnable(GL_ALPHA_TEST);
        glDepthMask(GL_TRUE);
        glDepthFunc(GL_LESS);

        glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA);
        glAlphaFunc(GL_GREATER, 0.1);
        #"""



        """glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        glViewport(0, 0, self.width, self.height)
        glOrtho(0, self.width, self.height, 0.0, 0.1, 100);
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        #glEnable(GL_BLEND)
        #glEnable(GL_DEPTH_TEST)
        #glClearDepth(GL_LEQUAL)
        #glBlendFunc(GL_SRC_ALPHA, GL_ONE);
        #"""


        """#loadImage();
        glEnable(GL_TEXTURE_2D);
        glEnable(GL_DEPTH_TEST);
        glBlendFunc(GL_SRC_ALPHA, GL_ONE);
        glMatrixMode(GL_MODELVIEW);
        #"""

        glTranslatef(self.worldx, self.worldy, 0.0);
        for i in self.listObjects:
            i.draw();
        glutSwapBuffers();