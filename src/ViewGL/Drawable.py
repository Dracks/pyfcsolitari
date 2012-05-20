__author__ = 'dracks'

from OpenGL.GL import *
import numpy

class AbstractDrawable:
    def __init__(self):
        pass
    def getSize(self):
        """
        @return return the size of the contents
        """
        return self.size;

    def draw(self):
        """
        Draw the data to a openGL, raises assert;
        """
        assert(False);

class Drawable(AbstractDrawable):
    def __init__(self, sx, sy):
        self.color=numpy.array((0,0,0,1), 'f')
        self.size=(sx, sy);

    def setColor(self, Red, Green, Blue, Alpha=1):
        self.color=numpy.array((Red,Green,Blue,Alpha), 'f');

    def draw(self, px, py, pz):
        glPushMatrix();

        #print "Pintant a la z", pz;
        #glScalef(0.01,0.01,0.01);
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glDisable(GL_TEXTURE_2D)
        glTranslatef(px, py, pz);

        glBegin(GL_QUADS)
        glColor4fv(self.color);
        #glTexCoord2f(0, 0);
        glVertex2f(0, 0)    # Bottom Left Of The Texture and Quad
        #glTexCoord2f(0, 1);
        glVertex2f(0, self.size[1])    # Top Left Of The Texture and Quad
        #glTexCoord2f(1, 1);
        glVertex2f( self.size[0],  self.size[1])    # Top Right Of The Texture and Quad
        #glTexCoord2f(1, 0);
        glVertex2f(self.size[0], 0)    # Bottom Right Of The Texture and Quad
        glEnd()
        glPopMatrix();

class DrawableImage(AbstractDrawable):
    def draw(self, px, py, pz):
        #print "Debug DrawableImage", px, py, pz
        glPushMatrix();
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.image)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        #print "Pintant a la z", pz;

        glTranslatef(px, py, pz);

        glBegin(GL_QUADS)
        glColor4f(1,1,1,1);
        glTexCoord2f(0, 0);
        glVertex2f(0, 0)    # Bottom Left Of The Texture and Quad
        #glVertex3f(0, 0, pz)    # Bottom Left Of The Texture and Quad
        glTexCoord2f(0, 1);
        glVertex2f(0, self.size[1])    # Top Left Of The Texture and Quad
        #glVertex3f(0, self.size[1],pz)    # Top Left Of The Texture and Quad
        glTexCoord2f(1, 1);
        glVertex2f( self.size[0],  self.size[1])    # Top Right Of The Texture and Quad
        #glVertex3f( self.size[0],  self.size[1], 0)    # Top Right Of The Texture and Quad
        glTexCoord2f(1, 0);
        glVertex2f(self.size[0], 0)    # Bottom Right Of The Texture and Quad
        #glVertex3f(self.size[0], 0, pz)    # Bottom Right Of The Texture and Quad
        glEnd()
        #glPopMatrix();

        glPopMatrix();

