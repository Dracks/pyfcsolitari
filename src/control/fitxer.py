import xml.dom.minidom
from xml.dom.minidom import Node


class fitxer:
    def __init__(self, fitxer):
        self.file=fitxer;
    
    # Guarda el taulell en el fitxer
    def guardar(self, taulell):
        None
        
    # Carrega un taulell d'un fitxer
    def carrega(self, taulell):
        doc=xml.dom.minidom.parse(self.file)
        None