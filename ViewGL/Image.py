__author__ = 'dracks'

from ViewGL import DrawableImage
import numpy

from OpenGL.GL import *

class Image(DrawableImage):
    def __init__(self, img):
        DrawableImage.__init__(self);
        img_data = numpy.array(list(img.getdata()), 'B')
        texture = glGenTextures(1)
        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glBindTexture(GL_TEXTURE_2D, texture)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.size[0], img.size[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
        #gluBuild2DMipmaps(GL_TEXTURE_2D, 1, img.size[0], img.size[1], GL_RGBA, GL_UNSIGNED_BYTE, img_data )
        self.image=texture
        #self.position=(px, py);
        self.size=img.size;
        #print self.size, self.image;