from Menu import Menu
from Desactualitzat import Desactualitzat
from Language import Language
from Principal import Principal
from Sortir import Sortir
from CancelarPartida import CancelarPartida
from GuardarCarregar import GuardarCarregar
from Guanyar import Guanyar
from InterficiePartida import InterficiePartida
from MostrarCartes import MostrarCartes

def get(d):
    return globals()[d]