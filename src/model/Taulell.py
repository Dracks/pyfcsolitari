#
#  Taulell.py
#  Solitari
#
#  Created by Dracks on 30/05/08.
#  Copyright (c) 2008 __MyCompanyName__. All rights reserved.
#

class Taulell:
    def __init__(self,columnes, munts, extra=0):
        self.n_munts=munts
        self.n_columnes=columnes
        self.munts=[]
        self.columnes=[]
        for i in range(0,columnes):
            self.columnes.append(list())
#        self.munts= [list(),list(),list(),list()]   # Inicialitzem els 4 munts a cap carta
        for i in range(0,munts):
            self.munts.append(list())

      #  self.columnes= [list(),list(),list(),list(),list(),list(),list(),list()]  # Inicialitzem les 8 columnes a cap carta
        if extra : self.sobrants = (list(),list())
        else: self.sobrants = False;
        
    def usaOcultes(self):
        if self.sobrants==False:
            return False
        else:
            return True;
    
    def ficaCartaMunt(self,carta,munt):
        self.munts[munt].append(carta)
        
    def ficaCartaColumna(self, carta, columna):
        self.columnes[columna].append(carta)
    
    def ficaCartaSobrantOculta(self, carta):
        self.sobrants[0].append(carta)
        
    def ficaCartaSobrantVisible(self,carta):
        self.sobrants[1].append(carta)
    
    def cartaMunt(self, munt):
        if len(self.munts[munt])>0:
            return self.munts[munt][len(self.munts[munt])-1]
        else: 
            return False
    
    def cartaColumna(self, columna, carta=-1):
        #print ">%i - %i - %i" % (columna, carta, len(self.columnes[columna]))
        if (carta == -1 and len(self.columnes[columna])>0):
            return self.columnes[columna][len(self.columnes[columna])-1]
        elif (carta !=-1 and carta < len(self.columnes[columna])):
            return self.columnes[columna][carta]
        else: return False
        
    def cartaSobrantOculta(self):
        if len(self.sobrants[0])!=0:
            return self.sobrants[0][len(self.sobrants[0])-1]
        else: return 0
    
    def cartaSobrantVisible(self):
        if len(self.sobrants[1])!=0:
            return self.sobrants[1][len(self.sobrants[1])-1]
        else: return 0
        
    def mouCartaColumnaMunt2(self, columna, carta, munt):
        self.mouCartaColumnaMunt(columna,munt)
        
    def mouCartaColumnaMunt(self,columna,munt):
        # treure la ultima carta de la columna i ficar-la en el munt que li toqui
        carta=self.columnes[columna].pop();
        self.munts[munt].append(carta);
    
    def mouCartesEntreColumnes(self, columna1, carta, columna2 ):
        # mou les cartes a partir de carta desde columna1 a columna2
        llista=self.columnes[columna1][carta-1:]
        self.columnes[columna1]=self.columnes[columna1][:carta-1]
        self.columnes[columna2].extend(llista)
        
    def mouCartaMuntColumna2(self, munt, carta, columna):
        self.mouCartaMuntColumna(munt, columna)      # Apanyo temporal
        
    def mouCartaMuntColumna(self, munt, columna):
        # mou la ultima carta del munt 'munt' a la columa
        carta=self.munts[munt].pop();
        self.columnes[columna].append(carta)
        
    def mouCartaMuntMunt2(self, munt1, carta, munt2):
        self.mouCartaMuntMunt(munt1,munt2)
    
    def mouCartaMuntMunt(self, munt1, munt2):
        self.munts[munt2].append(self.munts[munt1].pop())
    
    def mouCartaSobrantOcultaaVisible(self):
        carta=self.sobrants[0].pop()
        carta.setVisible(1)
        self.sobrants[1].append(carta)
    
    def mouCartaSobrantaMunt2(self, orig, munt):
        self.mouCartaSobrantaMunt(munt)
        
    def mouCartaSobrantaMunt(self, munt):
        self.munts[munt].append(self.sobrants[1].pop())
        
    def mouCartaSobrantaColumna2(self, original, carta, columna):
        self.mouCartaSobrantaColumna(columna)
        
    def mouCartaSobrantaColumna(self, columna):
        self.columnes[columna].append(self.sobrants[1].pop())
    
    def mouCartaColumnaSobrant2(self, columna, carta, desti):
        self.mouCartaColumnaSobrant(columna)
        
    def mouCartaColumnaSobrant(self, columna):
        self.sobrants[1].append(self.columnes[columna].pop())

    def mouCartaMuntSobrant2(self, munt, carta, desti):
        self.mouCartaMuntSobrant(munt)
        
    def mouCartaMuntSobrant(self, munt):
        self.sobrants[1].append(self.munts[munt].pop())
    
        #Extreu tot el contingut del Taulell en format d'arrays i diccionaris    
    def dump(self):
        columnes=list()
        for columna in self.columnes:
            contents=list()
            for carta in columna:
                contents.append({"pal":carta.getPal(), "numero": carta.getNum(), "visible": carta.getVisible()})
            columnes.append(contents)
        munts=list()
        for columna in self.munts:
            contents=list()
            for carta in columna:
                contents.append({"pal":carta.getPal(), "numero": carta.getNum(), "visible": carta.getVisible()})
            munts.append(contents)
        extres=False
        if self.sobrants != False:
            #extres=list()
            contents=list()
            for carta in self.sobrants[0]:
                contents.append({"pal":carta.getPal(), "numero": carta.getNum(), "visible": False})
            #extres.append(contents)
            contents2=list()
            for carta in self.sobrants[1]:
                contents2.append({"pal":carta.getPal(), "numero": carta.getNum(), "visible": True})
            extres={"visibles":contents2, "ocultes":contents}
        return (columnes, munts, extres)
        
    def llistaCartesColumna(self, columna):
        return self.columnes[columna];
        
    def llistaCartesMunt(self, munt):
        return self.munts[munt];
    
    def llistaCartesSobrantsOcultes(self):
        return self.sobrants[0]
        
    def llistaCartesSobrantsVisibles(self):
        return self.sobrants[1]
    
    def ncolumnes(self):
        return self.n_columnes
        
    def nmunts(self):
        return self.n_munts
        
    