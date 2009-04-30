import ConfigParser
import yaml
#from control import Texts

class Opcions:
    def __init__(self, nom_fitxer):
        config=ConfigParser.ConfigParser()
        config.read(nom_fitxer)
        self.resolucio=(config.getint('general','width'), config.getint('general','height'))
        self.texts=yaml.load(file('idioma'+"/"+config.get('general','language')+'.ylng','rb').read())
        self.tempsDobleClick=config.getfloat('general','vel_doubleclick')
        self.savepath=config.get('general', 'savepath')
        self.datetimeformat=config.get('general','dateformat')
        self.espaiat=((0,config.getint('game', 'espaiat1')),(0,config.getint('game', 'espaiat2')),(config.getint('game','espaiat3'),0));
        self.velositatDesplacamentCartes=config.getfloat('game','velositat')
        self.fps=config.getboolean('general','fps')
        self.maxDesplacamentPiles=(config.getint('game','MaxDespPilesx'),config.getint('game','MaxDespPilesy'))
        self.maxDesplacamentExtres=(config.getint('game','MaxDespExtresx'),config.getint('game','MaxDespExtresy'))
        self.theme=config.get('general','theme')

    def getText(self,menu, text):
        return self.texts[menu][text]
        
        