import ConfigParser
import yaml
#from control import Texts

class Opcions:
    def __init__(self, nom_fitxer):
        self.config=ConfigParser.ConfigParser()
        self.config.read(nom_fitxer)
        self.filename=nom_fitxer
        #self.resolucio=(config.getint('general','width'), config.getint('general','height'))
        if self.config.get('general','language')!='False':
            self.loadLanguage();
            self.language=True
        else:
            self.language=False
    
    def getLanguage(self):
        return self.language
        
    def setLanguage(self, language):
        self.language=language;
        self.config.set('general','language',language)
        self.loadLanguage()
        
    def loadLanguage(self):
        self.texts=yaml.load(file('idioma'+"/"+self.config.get('general','language')+'.ylng','rb').read())
        
    def getText(self,menu, text):
        return self.texts[menu][text]
        
    def getSavePath(self):
        return self.config.get('general','savepath')
    
    def getTempsDobleClick(self):
        return self.config.getfloat('general','vel_doubleclick')
        
    def getResolucio(self):
        return (self.config.getint('general','width'), self.config.getint('general','height'))
        
    def getDateFormat(self):
        return self.config.get('general','dateformat')
        
    def getEspaiat(self):
        return ((0,self.config.getint('game', 'espaiat1')),(0,self.config.getint('game', 'espaiat2')),(self.config.getint('game','espaiat3'),0));
        
    def getVelositatDesplacament(self):
        return self.config.getfloat('game','velositat')
        
    def getMaxDesplacamentPiles(self):
        return (self.config.getint('game','MaxDespPilesx'),self.config.getint('game','MaxDespPilesy'))
        
    def getMaxDesplacamentExtres(self):
        return (self.config.getint('game','MaxDespExtresx'),self.config.getint('game','MaxDespExtresy'))
    
    def getTheme(self):
        return self.config.get('general','theme')
        
    def save(self):
        configfile=open(self.filename, 'wb')
        #with open(self.filename, 'wb') as configfile:
        self.config.write(configfile)
#        self.config.write(self.filename)
        
    def getBoolFps(self):
        return self.config.getboolean('general','fps')
        
        