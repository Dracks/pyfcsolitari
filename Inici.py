__author__ = 'dracks'

import ViewGL
import Widgets
import Image

if __name__=='__main__':
    w=ViewGL.Window(1024, 600, 'Test WidgetsOld Over GL');
    ButtonViewImage=ViewGL.Image(Image.open('Data/fournier/boto.png'));

    Menu=Widgets.Center((1200, 600))
    Menu.setElement(Widgets.Image(ButtonViewImage));
    w.addObject(Menu);

    Menu=Widgets.Center((1000,600));
    Layout=Widgets.VerticalLayout(10);
    Layout.addElem(Widgets.Image(ButtonViewImage));
    Layout.addElem(Widgets.Image(ButtonViewImage));
    Layout.addElem(Widgets.Image(ButtonViewImage));
    Menu.setElement(Layout);
    w.addObject(Menu)

    Menu=Widgets.Center((800, 600))
    Menu.setElement(Widgets.Image(ButtonViewImage));
    w.addObject(Menu);

    w.run();
