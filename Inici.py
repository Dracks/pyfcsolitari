__author__ = 'dracks'

import ViewGL
import Widgets
import Image, ImageDraw, ImageFont

class Font:
    def __init__(self, font, size):
        self.font=ImageFont.truetype(font, size);

    def render(self, text, color=(0,0,0)):
        size = self.font.getsize(text) # Returns the width and height of the given text, as a 2-tuple.
        im = Image.new('RGBA', size, (0, 0, 0, 0)) # Create a blank image with the given size
        draw = ImageDraw.Draw(im)
        draw.text((0, 0), text, font=self.font, fill=color) #Draw text
        return im

    def renderText(self, text, width, align,color=(0,0,0)):
        pass

if __name__=='__main__':
    w=ViewGL.Window(1024, 600, 'Test WidgetsOld Over GL');

    #w.setWindowIcon('Data/icona_osX.png')

    ButtonViewImage=ViewGL.Image(Image.open('Data/fournier/boto.png'));
    BackgroundImage=ViewGL.Drawable(1024,600);
    BackgroundImage.setColor(0.0,0.4,0.0,.2)

    Menu=Widgets.Center((1200, 600))
    Menu.setElement(Widgets.Image(ButtonViewImage));
    w.pushView(Menu);

    Menu=Widgets.Center((800, 600))
    Menu.setElement(Widgets.Image(ButtonViewImage));
    w.pushView(Menu);

    Menu=Widgets.Center((1000,600));
    Layout=Widgets.VerticalLayout(10);
    Layout.addElem(Widgets.Image(ButtonViewImage));
    Layout.addElem(Widgets.Image(ButtonViewImage));
    Layout.addElem(Widgets.Image(ButtonViewImage));
    Menu.setElement(Layout);

    #F=Font('Data/font1.ttf', 40);
    F=Font('Data/Anonymous_Pro.ttf', 20);
    w.setFPSFunction(lambda text: (ViewGL.Image(F.render(str(text), (255,255,255)))));
    #w.pushView(Widgets.Image(ViewGL.Image(F.render("Hola mon!", (255,255,255)))))

    #w.pushView(Widgets.Image(BackgroundImage))

    bg=Widgets.Background()
    bg.setBackground(Widgets.Image(BackgroundImage))
    bg.setForeground(Menu);

    w.pushView(bg)

    #w.pushView(Menu)

    w.run();
