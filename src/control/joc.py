# -*- coding: UTF-8 -*-
import os
import yaml
from datetime import datetime
import urllib

import ViewGL
import Widgets
import Pantalles


from model import Taulell
from model import Carta
from control import Recursos
from control import Acordeo
from control import Sismunts
from model import Moviment

VERSIO='1.0'

class joc:
    def __init__(self, opcions):
        self.recursos=Recursos(opcions.getTheme())
        self.opcions=opcions
        print self.opcions.getResolucio()[0], self.opcions.getResolucio()[1]
        self.interficie=ViewGL.Window(self.opcions.getResolucio()[0], self.opcions.getResolucio()[1], "PyFC: Solitari")
        #self.interficie.setTitle("PyFC: Solitari")
        #self.interficie.setIcon("Data/icona_transparent.png")
        imatge1=self.recursos.getimgBoto()
        font=self.recursos.getfont(1)
        font2=self.recursos.getfont(2)
        #self.interficie.showFPS(self.opcions.getBoolFps())
        self.marge=30;
        self.interficie.pushView(Widgets.Image(self.recursos.getfonsMenu()))
        self.mostrarMovimentsPossibles=False
        #self.interficie.setFunctSortir(self.sortir,1)
        self.sortint=False

    ############
    # Menu Principal!
    ###########
        #self.menuPrincipal=menu

    #############
    # Desactualitzat
    #############
         #self.desactualitzat=Centre(contingut,self.opcions.resolucio)


    #############
    # Sortir?
    #############

    ############
    # Sortir del joc, cancelar la partida
    ############

    ###########
    # Guardar i Carregar partida
    ###########

    ###########
    # Has guanyat!
    ###########


        #self.mouse=Mouse()
        #self.interficie.setMouse(self.mouse)
#		self.mouse.setOnUnClick(F,None)
        self.jugada=False

    ###########
    # Fiquem el menu que toca per començar
    ###########
        if self.opcions.getLanguage()==False:
            idioma=Language(self, self.recursos ,self.opcions)
            self.interficie.setPrimerPla(idioma.get());
        else:
            self.reset();
            self.loadInici()

    def loadInici(self):
        #### Carraguem l'ultima versió
        try:
            #lastVersion=urllib.urlopen('http://dracks.freehostia.com/PyFC-Version').read()
            lastVersion=urllib.urlopen('http://localhost/~dracks/PyFC-Version').read()
            if len(lastVersion)>10:
                lastVersion=VERSIO
        except:
            print "error en llegir la versio"
            lastVersion=VERSIO

        if lastVersion==VERSIO:
            self.interficie.pushView(self.menuPrincipal.get())
        else:
            self.interficie.pushView(self.menuPrincipal.get())
            self.interficie.enableDarkness()
            #self.interficie.setPrimerPla(Desactualitzat(self, self.recursos, self.opcions, lastVersion, VERSIO).get())
            self.interficie.pushView(Desactualitzat(self, self.recursos, self.opcions, lastVersion, VERSIO).get())

    def reset(self):
        self.menuPrincipal=Pantalles.Principal(self, self.recursos, self.opcions)
        self.preguntarSortida=Pantalles.Sortir(self, self.recursos, self.opcions)
        #self.desactualitzat=


    def executa(self):
        self.interficie.run()

    def aMenuPrincipal(self):
        self.interficie.popView()

    def aPrincipaldesdeActualitzacio(self):
        self.interficie.ocultaFosc()
        self.interficie.setPrimerPla(self.interficie.popBackground())

    def aMenuJoc(self):
        self.interficie.enableDarkness()
        #self.interficie.pushBackground(self.interficie.getPrimerPla())
        #self.interficie.setPrimerPla(CancelarPartida(self, self.recursos, self.opcions).get())
        self.interficie.pushView(Pantalles.CancelarPartida(self, self.recursos, self.opcions).get())
        self.interficiePartida.desactivaDesplacar()

    def aJocdesdeMenu(self):
        self.interficie.disableDarkness()
        self.interficie.popView()
        self.interficiePartida.activaDesplacar()

    def deJocaMenu(self):
        self.interficie.disableDarkness()
        self.interficie.popView()
        self.interficie.popView()

        #self.interficie.popBackground()
        #self.interficie.ocultaFosc()
        #self.interficie.setPrimerPla(self.menuPrincipal.get())
        #self.interficie.setOnMouseMove(False)
        #self.interficie.setForFrame(False)
        #self.activaDesplacar()

    def menuPartidaFinalitzada(self):
        self.interficie.pushBackground(self.interficie.getPrimerPla())
        self.interficie.mostraFosc()
        moviments="%d" %  self.joc.getNumMoviments()
        self.guanyar[1].set(self.recursos.getfont(1).render(self.opcions.getText('win','text').replace('<~moviments~>', moviments),True, (100,100,100)))
        self.guanyar[0].update()
        self.interficie.setPrimerPla(self.guanyar[0])
        self.desactivaDesplacar()

    def deFinalitzadaaPrincipal(self):
        self.interficie.popBackground()
        self.interficie.ocultaFosc()
        self.interficie.setPrimerPla(self.menuPrincipal.get())
        self.interficie.setOnMouseMove(False)
        self.interficie.setForFrame(False)
        self.activaDesplacar()

    def activaMoviments(self):
        self.interficiePartida.modificaMarcaMoviments(True, self.joc.getMoviments())
        self.zonaJoc.setMovimentsText(self.opcions.getText('game', 'hiddenmovements'), self.zonaJoc.desactivaMoviments)

        """self.botoVisualitzarMoviments.setText(self.opcions.getText('game','hiddenmovements'))
        self.botoVisualitzarMoviments.setOnClick(self.desactivaMoviments, None)
        self.cartesMarcades=self.joc.getMoviments()
        self.modificaMarcaMoviments(True)
        self.mostrarMovimentsPossibles=True;"""

    def desactivaMoviments(self):
        self.interficiePartida.modificaMarcaMoviments(False, self.joc.getMoviments())
        self.zonaJoc.setMovimentsText(self.opcions.getText('game', 'viewmovements'), self.zonaJoc.activaMoviments)
        """self.botoVisualitzarMoviments.setText(self.opcions.getText('game','viewmovements'))
        self.botoVisualitzarMoviments.setOnClick(self.activaMoviments, None)
        self.modificaMarcaMoviments( False)
        self.mostrarMovimentsPossibles=False;"""


    def aCarregarJoc(self):
        textos=list()
        textos.append(self.opcions.getText('load&save', 'load'));
        actions=[None,None,None,None,None]
        dades=[None]
        actions[0]=self.aMenuPrincipal
        j=0
        fitxers=self.getFitxersGuardats()
        for i in range(len(fitxers)):
            j+=1
            if fitxers[i]==False:
                #self.carregaBotoPartidaGuardada( self.menuGuardarCarregar[1][i], self.opcions.getText('load&save','empty'), False, None)
                textos.append(self.opcions.getText('load&save','empty'))
            else:
                partida=self.getInfoFitxerPartida(fitxers[i])
                #self.carregaBotoPartidaGuardada(self.menuGuardarCarregar[1][i], partida['name'], self.carregarPartida, partida)
                textos.append(partida['name'])
                actions[j]=self.carregarPartida
                dades.append(partida)
        #self.menuGuardarCarregar[3].setOnClick(self.aMenuPrincipal, None)

        self.interficie.pushView(Pantalles.GuardarCarregar(self, self.recursos, self.opcions, actions, textos, dades).get())

    def aMenuGuardar(self):
        textos=list()
        textos.append(self.opcions.getText('load&save','save'))
        actions=[None, None, None, None, None]
        actions[0]=self.deGuardaraJoc
        dades=[None]
        j=0
        fitxers=self.getFitxersGuardats()
        for i in range(len(fitxers)):
            j+=1
            nom= self.opcions.getSavePath()+"/savegame%d.sav" % i
            dades.append(nom)
            actions[j]=self.guardarPartida
            if fitxers[i]==False:
                #self.carregaBotoPartidaGuardada( self.menuGuardarCarregar[1][i], self.opcions.getText('load&save','empty'), self.guardarPartida, nom)
                textos.append(self.opcions.getText('load&save','empty'))

            else:

                partida=self.getInfoFitxerPartida(fitxers[i])
                #self.carregaBotoPartidaGuardada( self.menuGuardarCarregar[1][i], partida['name'], self.guardarPartida, fitxers[i])
                textos.append(partida['name'])
        self.interficie.mostraFosc()
        self.interficie.pushBackground(self.interficie.getPrimerPla())
        self.interficie.setPrimerPla(GuardarCarregar(self, self.recursos, self.opcions, actions, textos, dades).get())
        """self.interficie.mostraFosc()
        self.menuGuardarCarregar[2].set(self.recursos.getfont(2).render(self.opcions.getText('load&save','save'),True, (100,100,100)) )
        fitxers=self.getFitxersGuardats()
        for i in range(len(fitxers)):
            nom= self.opcions.savepath+"/savegame%d.sav" % i
            if fitxers[i]==False:
                self.carregaBotoPartidaGuardada( self.menuGuardarCarregar[1][i], self.opcions.getText('load&save','empty'), self.guardarPartida, nom)
            else:
                partida=self.getInfoFitxerPartida(fitxers[i])
                self.carregaBotoPartidaGuardada( self.menuGuardarCarregar[1][i], partida['name'], self.guardarPartida, fitxers[i])
        self.menuGuardarCarregar[0].update()
        self.menuGuardarCarregar[3].setOnClick(self.deGuardaraJoc, None)
        self.interficie.pushBackground(self.interficie.getPrimerPla())
        self.interficie.setPrimerPla(self.menuGuardarCarregar[0])"""

    def deGuardaraJoc(self):
        self.interficie.ocultaFosc()
        self.interficie.setPrimerPla(self.interficie.popBackground())
        self.interficiePartida.activaDesplacar()

    def guardarPartida(self, fitxer):
        header="# Save: Solitari - PFC\n# Creador: Jaume\n# Save format: yaml\n"
        estat=self.taulell.dump()
        moviments=self.joc.getNumMoviments()
        partida=self.joc.__class__.__name__
        file(fitxer, 'wb').write(header+yaml.dump({"game": partida, "movements": moviments, "name": datetime.now().strftime(self.opcions.getDateFormat()), "piles": estat[0], "munts": estat[1], "extres": estat[2]}))
        self.interficie.setPrimerPla(self.interficie.popBackground())
        self.interficie.ocultaFosc()
        self.aMenuGuardar()

    def carregarPartida(self, info):
        clase=globals()[info['game']]
        partida=clase()
        taulell=partida.getTaulell()
        partida.setMoviments(info['movements'])
        for i in range(len(info['piles'])):
            for elem in info['piles'][i]:
                if elem!=None:
                    carta=Carta(elem['numero'],elem['pal'],elem['visible'])
                    taulell.ficaCartaColumna(carta,i)
        for i in range(len(info['munts'])):
            for elem in info['munts'][i]:
                if elem!=None:
                    carta=Carta(elem['numero'],elem['pal'],elem['visible'])
                    taulell.ficaCartaMunt(carta,i)
        if taulell.usaOcultes():
            for elem in info['extres']['ocultes']:
                if elem!=None:
                    carta=Carta(elem['numero'],elem['pal'],False)
                    taulell.ficaCartaSobrantOculta(carta)
            for elem in info['extres']['visibles']:
                if elem!=None:
                    carta=Carta(elem['numero'],elem['pal'],True)
                    taulell.ficaCartaSobrantVisible(carta)
        self.taulell=taulell
        self.joc=partida
        Interficie=globals()[partida.getInterficie()];
        self.interficiePartida=Interficie(self, self.recursos, self.opcions, self.taulell.dump())
        self.zonaJoc=InterficiePartida(self, self.recursos, self.opcions, self.interficiePartida, self.mouse, self.joc.getNumMoviments())
        self.interficie.setPrimerPla(self.zonaJoc.get())

    def sortir(self,params):
        if self.sortint==True and params==0:
            return
        if params==0:
            self.interficie.enableDarkness()
            #self.interficie.pushBackground(self.interficie.getPrimerPla())
            self.interficie.pushView(self.preguntarSortida.get())
            self.sortint=True
        elif params==1:
            self.interficie.close()
        elif params==-1:
            self.interficie.disableDarkness()
            self.interficie.popView()
            self.sortint=False

    def getInfoFitxerPartida(self, fitxer):
        return yaml.load(file(fitxer,'rb').read())

    def getFitxersGuardats(self):
        fitxers=[False,False,False, False]
        if not os.path.exists(self.opcions.getSavePath()):
            try:
                os.makedirs(self.opcions.getSavePath())
                return fitxers
            except os.error:
                return fitxers
        llistat=os.listdir(self.opcions.getSavePath())
        for file in llistat:
            for i in range(len(fitxers)):
                nom="savegame%d.sav" % i
                if file==nom:
                    fitxers[i]=self.opcions.getSavePath()+"/"+nom
        return fitxers;

    """def carregaBotoPartidaGuardada(self, boto, text,funcio, parametres):
        boto.setText(text)
        boto.setOnClick(funcio, parametres)"""

    """def opcionsMenu(self):
        self.moviments=list()
        Visible=VArea(2)
        boto=Boto(self.recursos.getimgBoto(), self.opcions.getText('game','menu'), self.recursos.getfont(1))
        boto.setOnClick(self.aMenuJoc,1)
        barra=HArea(10)
        barra.addElem(Ghost())
        barra.addElem(boto);
        boto=Boto(self.recursos.getimgBoto(), self.opcions.getText('game','undo'), self.recursos.getfont(1))
        boto.setOnClick(self.undo,1)
        barra.addElem(boto)
        boto=Boto(self.recursos.getimgBoto(), self.opcions.getText('game','save'), self.recursos.getfont(1))
        boto.setOnClick(self.aMenuGuardar,None)
        barra.addElem(boto)
        boto=Boto(self.recursos.getimgBoto(), self.opcions.getText('game','viewmovements'), self.recursos.getfont(1))
        boto.setOnClick(self.activaMoviments,None)
        self.botoVisualitzarMoviments=boto
        barra.addElem(boto)
        barra.addElem(Reomple(barra,(self.opcions.resolucio[0],1)))
        self.vistaMoviments=Imatge(self.recursos.getfont(1).render(self.opcions.getText('game','movements')+": %d" % self.joc.getNumMoviments(),True,(255,255,255)))
        barra.addElem(self.vistaMoviments)
        barra.addElem(Ghost())
        Visible.addElem(barra)
        scroll=Scroll((self.opcions.resolucio[0], self.opcions.resolucio[1]-30))
        Visible.addElem(scroll)
        self.interficie.setPrimerPla(Visible)
        Visible.update()
        self.zonaJoc=scroll;
        self.interficie.setOnMouseMove(self.tractaScroll)
        return scroll"""

    def createGame(self, game):
        clase=globals()[game]
        self.joc=clase()
        self.joc.reparteixCartes()
        self.taulell=self.joc.getTaulell()
        Interficie=globals()['Pantalles'].get(self.joc.getInterficie());
        self.interficiePartida=Interficie(self, self.recursos, self.opcions, self.taulell.dump())
        self.zonaJoc=Pantalles.InterficiePartida(self, self.recursos, self.opcions, self.interficiePartida, None, self.joc.getNumMoviments())
        self.interficie.pushView(self.zonaJoc.get())

    """def mostraPartida(self):
        contents=self.opcionsMenu()
        self.mostrarMovimentsPossibles=False

        All=VArea(20)
        Interficie=HArea(20)
        Interficie.addElem(Ghost())
        for p in self.accesdirecte[0]:
            Interficie.addElem(p)
        Interficie.addElem(Reomple(Interficie, (self.opcions.resolucio[0],1)))
        muntets=VArea(15)
        Interficie.addElem(muntets)
        #for p in self.accesdirecte[1]:
        muntets.addElem(self.accesdirecte[1][0])
        muntets.addElem(self.accesdirecte[1][1])
        muntets=VArea(15)
        Interficie.addElem(muntets)
        muntets.addElem(self.accesdirecte[1][2])
        muntets.addElem(self.accesdirecte[1][3])
        Interficie.addElem(Ghost())
        All.addElem(Interficie)
        if self.accesdirecte[2]!=False:
            Interficie2=HArea(20)
            Interficie2.addElem(Ghost())
            Interficie2.addElem(self.accesdirecte[2][0])
            Interficie2.addElem(Ghost())
            Interficie2.addElem(self.accesdirecte[2][1])
            All.addElem(Interficie2)
        contents.assign(Fons(Imatge(self.recursos.getfonsMenu(), True),All))
        #contents.assign(All)
        contents.update()
       # self.zonaJoc="""

    """def carregaPiles(self):
        #self.accesdirecte=(list(),list(), Pila())
        imatgeMarca=Imatge(self.recursos.getImatgeMarca(),True,(3,3))
        piles=list()
        for i in range(self.taulell.ncolumnes()):
            pila=Pila(Fons(imatgeMarca,Imatge(self.recursos.getCartaNull()), False), (-2,1), self.opcions.maxDesplacamentPiles, velositatDesplacament=self.opcions.velositatDesplacamentCartes)
            pila.setOnClick(self.clickPila,i)
            pila.setOnDobleClick((self.dobleclickColumna,i))
            for e in self.taulell.llistaCartesColumna(i):
                if e.getVisible():
                    pila.addElem(Fons(imatgeMarca,Imatge(self.recursos.getCarta(e.pal,e.num)),False),self.opcions.espaiat[0],True)
                else:
                    pila.addElem(Fons(imatgeMarca,Imatge(self.recursos.getCartaOculta()),False),self.opcions.espaiat[1],False)
            piles.append(pila)
        muntets=list()
        for i in range(self.taulell.nmunts()):
            pila=Pila(Fons(imatgeMarca,Imatge(self.recursos.getCartaNull()),False),creixer=False)
            pila.setOnClick(self.clickMunt,i)
            for e in self.taulell.llistaCartesMunt(i):
                pila.addElem(Fons(imatgeMarca,Imatge(self.recursos.getCarta(e.pal,e.num)),False),(1,1),False)
            pila.update()
            muntets.append(pila)

        sobrants=False
        if self.taulell.usaOcultes():
            cartes_sobrants=self.taulell.llistaCartesSobrantsOcultes()
            p_sobrants_ocultes=Pila(Imatge(self.recursos.getCartaNull()),creixer=False)
            p_sobrants_ocultes.setOnClick(self.clickSobrantsOcultes,None)
            for e in cartes_sobrants:
                p_sobrants_ocultes.addElem(Fons(imatgeMarca,Imatge(self.recursos.getCartaOculta()),False),(1,1),False)
            cartes_sobrants=self.taulell.llistaCartesSobrantsVisibles()
            p_sobrants_visibles=Pila(Ghost(),(10,0),self.opcions.maxDesplacamentExtres, velositatDesplacament=self.opcions.velositatDesplacamentCartes)
            p_sobrants_visibles.setOnClick(self.clickSobrantsVisibles, None)
            p_sobrants_visibles.setOnDobleClick((self.dobleclickSobrants, None))
            for e in cartes_sobrants:
                p_sobrants_visibles.addElem(Fons(imatgeMarca,Imatge(self.recursos.getCarta(e.pal,e.num)),False),self.opcions.espaiat[2],True)
            sobrants=(p_sobrants_ocultes,p_sobrants_visibles)
        else:
            sobrants=False
      #  muntets=(Pila(Imatge(self.recursos.getCartaNull(),0)),Pila(Imatge(self.recursos.getCartaNull(),0)),Pila(Imatge(self.recursos.getCartaNull(),0)),Pila(Imatge(self.recursos.getCartaNull(),0)))
        self.accesdirecte=(piles,muntets, sobrants)"""

    def desactivaDesplacar(self):
        for p in self.accesdirecte[0]:
            p.desactivaDesplacar()
        for p in self.accesdirecte[1]:
            p.desactivaDesplacar()
        if self.accesdirecte[2]!=False:
            self.accesdirecte[2][1].desactivaDesplacar()

    def activaDesplacar(self):
        for p in self.accesdirecte[0]:
            p.activaDesplacar()
        for p in self.accesdirecte[1]:
            p.activaDesplacar()
        if self.accesdirecte[2]!=False:
            self.accesdirecte[2][1].activaDesplacar()

    def tractaScroll(self, (x,y)):
        despx=despy=0;
        if x>self.opcions.resolucio[0]-self.marge:
            despx=2;
        elif x<self.marge:
            despx=-2;
        if y>self.opcions.resolucio[1]-self.marge:
            despy=2;
        elif y<self.marge:
            despy=-2
        if despx!=0 or despy!=0:
            self.interficie.setForFrame((self.moureScroll,(despx,despy)))
        else: self.interficie.setForFrame(False)

    def moureScroll(self,(x,y)):
        pos=self.zonaJoc.getPos();
        tam_joc=self.zonaJoc.getTamany()
        tam_fons=self.zonaJoc.getTamContents();
        #print tam_fons;
        if x<0:
            if pos[0]<-x:
                x=-pos[0]
        elif x>0:
            if pos[0]+x+tam_joc[0]>tam_fons[0]:
                x=tam_fons[0]-pos[0]-tam_joc[0]
                if (x<0):
                    x=0
        if y<0:
            if pos[1]<-y:
                y=-pos[1]
        elif y>0:
            if pos[1]+y+tam_joc[1]>tam_fons[1]:
                y=tam_fons[1]-pos[1]-tam_joc[1]
                if (y<0):
                    y=0
        self.zonaJoc.desplaca((x,y))

    def clickPila(self,pila, (carta, coordenades)):
       # print "%d - %d" % (pila, carta)
        if len(self.accesdirecte[0][pila])>0:
            if self.mostrarMovimentsPossibles:
                    self.modificaMarcaMoviments(False)
            carta_model=self.taulell.cartaColumna(pila, carta-1)
            if len(self.accesdirecte[0][pila])==carta and not carta_model.getVisible():
                self.accesdirecte[0][pila].setLast((Fons(Imatge(self.recursos.getImatgeMarca(),True,(3,3)),Imatge(self.recursos.getCarta(carta_model.pal, carta_model.num)),False),self.opcions.espaiat[0],True))
                carta_model.setVisible(True)
                self.moviments=list()
                if self.mostrarMovimentsPossibles:
                    self.cartesMarcades=self.joc.getMoviments()
                    self.modificaMarcaMoviments(True)
            elif self.joc.comprovaClickCartaPila(pila, carta-1):
                mouse=self.interficie.getMouse()
                llistat=self.accesdirecte[0][pila].subPila(carta-1)
                p=Pila()
                for i in range(len(llistat[0])):
                    p.addElem(llistat[0][i],llistat[1][i], llistat[2][i])
                mouse.arrastrar(p, (coordenades[0]-5,coordenades[1]-5))
                mouse.setOnUnClick(self.deixaCarta,((self.joc.comprovaMovimentColumnaAColumna, self.joc.comprovaMovimentColumnaAMunt), (self.taulell.mouCartesEntreColumnes, self.taulell.mouCartaColumnaMunt), self.accesdirecte[0][pila], pila, carta, self.opcions.espaiat[0], True))
                if self.mostrarMovimentsPossibles:
                    self.cartesMarcades=self.joc.getMovimentsFromPila(pila, carta)
                    self.modificaMarcaMoviments(True)
                self.jugada=True
                self.desactivaDesplacar()
                self.last_pseudomoviment=Moviment()
                self.last_pseudomoviment.funcions= (self.taulell.mouCartesEntreColumnes, self.taulell.mouCartaMuntColumna2)
                self.last_pseudomoviment.zona_orig= 0
                self.last_pseudomoviment.original= pila
            else:
                if self.mostrarMovimentsPossibles:
                    #self.cartesMarcades=self.joc.getMoviments()
                    self.modificaMarcaMoviments(True)


    def clickMunt(self,munt, (carta, coordenades)):
        #print "munt: %d carta: %d" % (munt, carta)
        if len(self.accesdirecte[1][munt])>0:
            if self.mostrarMovimentsPossibles:
                    self.modificaMarcaMoviments(False)
            mouse=self.interficie.getMouse()
            p=Pila()
            p.addElem(self.accesdirecte[1][munt].pop()[0],self.opcions.espaiat[0],True)
            mouse.arrastrar(p, (coordenades[0]-5,coordenades[1]-5))
            self.desactivaDesplacar()
            mouse.setOnUnClick(self.deixaCarta,((self.joc.comprovaMovimentMuntAColumna, self.joc.comprovaMovimentMuntAMunt), (self.taulell.mouCartaMuntColumna2,self.taulell.mouCartaMuntMunt), self.accesdirecte[1][munt], munt, carta, (1,1), False))
            if self.mostrarMovimentsPossibles:
                    self.cartesMarcades=self.joc.getMovimentsFromMunt(munt)
                    self.modificaMarcaMoviments(True)
            self.jugada=True
            self.last_pseudomoviment=Moviment()
            self.last_pseudomoviment.funcions= (self.taulell.mouCartaColumnaMunt2, self.taulell.mouCartaMuntMunt2)
            self.last_pseudomoviment.zona_orig= 1
            self.last_pseudomoviment.original= munt


    def clickSobrantsOcultes(self,params, (carta, coordenades)):
        if len(self.accesdirecte[2][0]):
            self.accesdirecte[2][0].pop()
            c=self.taulell.cartaSobrantOculta()
            self.accesdirecte[2][1].addElem(Fons(Imatge(self.recursos.getImatgeMarca(),True,(3,3)),Imatge(self.recursos.getCarta(c.pal,c.num)), False),self.opcions.espaiat[2],True)
            self.taulell.mouCartaSobrantOcultaaVisible()
            self.zonaJoc.update()
            self.moviments=list()
            if self.mostrarMovimentsPossibles:
                self.modificaMarcaMoviments(False)
                self.cartesMarcades=self.joc.getMoviments()
                self.modificaMarcaMoviments(True)

    def clickSobrantsVisibles(self, params, (carta, coordenades)):
       # print "hi2"
        if len(self.accesdirecte[2][1])>0:
            if self.mostrarMovimentsPossibles:
                    self.modificaMarcaMoviments(False)
            mouse=self.interficie.getMouse()
            p=Pila()
            p.addElem(self.accesdirecte[2][1].pop()[0],self.opcions.espaiat[0],True)
            mouse.arrastrar(p, (coordenades[0]-5,coordenades[1]-5))
            self.desactivaDesplacar()
          #  mouse.setOnUnClick(self.deixaDesdeSobrants, None)
          #(funcions_moure, original_vista, pilaOriginal, cartaOriginal, espaiat_original)
            mouse.setOnUnClick(self.deixaCarta, ((self.joc.comprovaMovimentExtresAColumna, self.joc.comprovaMovimentExtresAMunt), (self.taulell.mouCartaSobrantaColumna2, self.taulell.mouCartaSobrantaMunt2), self.accesdirecte[2][1], None, None, self.opcions.espaiat[2], False))
            self.jugada=True
            #self.last_pseudomoviment={ "funcio": self.undoSobrants; }	# Preparo el moviment per retrocedir
            self.last_pseudomoviment=Moviment()
            self.last_pseudomoviment.funcions= (self.taulell.mouCartaColumnaSobrant2, self.taulell.mouCartaMuntSobrant2)
            self.last_pseudomoviment.zona_orig= 2
            self.last_pseudomoviment.original= 1
            if self.mostrarMovimentsPossibles:
                    self.cartesMarcades=self.joc.getMovimentsFromExtres()
                    self.modificaMarcaMoviments(True)

    def deixaCarta(self, (funcions_comprovar, funcions_moure, original_vista, pilaOriginal, cartaOriginal, espaiat_original, Avancat)):
        if self.jugada == True:
            if self.mostrarMovimentsPossibles:
                self.modificaMarcaMoviments( False)
            colocada=False
            piles=self.accesdirecte[0]
            coordenades_test=self.mouse.getCoordenades()
            overflow=self.mouse.getOverflow()
            tam_pila=self.mouse.getTamany();
            coordenades_test=(coordenades_test[0]-overflow[0]+(tam_pila[0]/2),coordenades_test[1]-overflow[1]+5)
            for i in range(len(piles)):
                if piles[i].test(coordenades_test):
                #if not piles[i].getMouseOver() ==False:
                    #comprova moviment
                    #if True:
                    if Avancat == True:
                        comprovacioAvancat=self.joc.comprovaMovimentAvancat(pilaOriginal, i, cartaOriginal)
                    else:
                        comprovacioAvancat=False
                    if funcions_comprovar[0](pilaOriginal,i,cartaOriginal) or comprovacioAvancat:
                        self.last_pseudomoviment.carta=len(piles[i])  # Carrego un valor que necessitare mes tard
                        self.last_pseudomoviment.zona_desti=0;
                        self.last_pseudomoviment.desti=i;
                        self.last_pseudomoviment.funcio=self.last_pseudomoviment.funcions[0]
                        piles[i].addList(self.mouse.getLlista().subPila(0), self.opcions.espaiat[0])
                        funcions_moure[0](pilaOriginal, cartaOriginal, i)
                        colocada=True
                    break

            if len(self.mouse.getLlista())==1 and not colocada:
                muntets=self.accesdirecte[1]
                for i in range(len(muntets)):
                    if muntets[i].test(coordenades_test):
                    #if not muntets[i].getMouseOver() == False:
                            #comprova moviment
                        if funcions_comprovar[1](pilaOriginal,i):
                            self.last_pseudomoviment.carta=len(muntets[i])
                            self.last_pseudomoviment.zona_desti=1;
                            self.last_pseudomoviment.desti=i;
                            self.last_pseudomoviment.funcio=self.last_pseudomoviment.funcions[1]
                            muntets[i].addElem(self.mouse.getLlista().getLast()[0],(1,1),True)
                            self.mouse.arrastrar(False, None)
                            funcions_moure[1](pilaOriginal,i)
                            colocada=True
                        break
            if colocada==False:
                original_vista.addList(self.mouse.getLlista().subPila(0), espaiat_original)
            else :
                moviments=self.joc.incrementaMoviments() # Per seguretat
                imatge=self.recursos.getfont(1).render(self.opcions.getText('game','movements')+": %d" % moviments,True, (255,255,255))
                self.vistaMoviments.set(imatge)
                self.zonaJoc.update()
                if self.joc.partidaFinalitzada():
                    self.menuPartidaFinalitzada()
                    self.last_pseudomoviment=False  # Per seguretat
                else:
                    self.moviments.append(self.last_pseudomoviment)
                   # self.last_pseudomoviment=Moviment()
            if self.mostrarMovimentsPossibles:
                self.cartesMarcades=self.joc.getMoviments()
                self.modificaMarcaMoviments(True)

        self.jugada=False
        self.activaDesplacar()

    def dobleclickColumna(self,columna, carta):
        if len(self.accesdirecte[0][columna])==carta[0]:
            if not self.taulell.cartaColumna(columna).getVisible():
                self.clickPila(columna, carta)
            #self.debug()
            if self.mostrarMovimentsPossibles:
                self.modificaMarcaMoviments( False)
            for i in range(len(self.accesdirecte[1])):
                if self.joc.comprovaMovimentColumnaAMunt(columna,i):
                    self.taulell.mouCartaColumnaMunt(columna,i)
                    self.last_pseudomoviment=Moviment()
                    self.last_pseudomoviment.original=columna
                    self.last_pseudomoviment.desti=i
                    self.last_pseudomoviment.zona_orig=0
                    self.last_pseudomoviment.zona_desti=1
                    self.last_pseudomoviment.carta=len(self.accesdirecte[1][i])
                    self.last_pseudomoviment.funcio=self.taulell.mouCartaMuntColumna2
                    self.accesdirecte[1][i].addElem(self.accesdirecte[0][columna].pop()[0],(1,1),True)
                    moviments=self.joc.incrementaMoviments()
                    imatge=self.recursos.getfont(1).render(self.opcions.getText('game','movements')+": %d" % moviments, True, (255,255,255))
                    if self.mostrarMovimentsPossibles:
                        self.cartesMarcades=self.joc.getMoviments()
                        self.modificaMarcaMoviments(True)
                    self.vistaMoviments.set(imatge)
                    self.zonaJoc.update()
                    if self.joc.partidaFinalitzada():
                        self.menuPartidaFinalitzada()
                        self.last_pseudomoviment=False  # Per seguretat
                    else:
                        self.moviments.append(self.last_pseudomoviment)
                        # self.last_pseudomoviment=Moviment()
                    break
            if self.mostrarMovimentsPossibles:
                self.modificaMarcaMoviments(True)


    def dobleclickSobrants(self,params, carta):
        if len(self.accesdirecte[2][1])==carta[0]:
            #self.debug()
            if self.mostrarMovimentsPossibles:
                self.modificaMarcaMoviments( False)
            for i in range(len(self.accesdirecte[1])):
                if self.joc.comprovaMovimentExtresAMunt(0, i): # CONY s'ha d'arreglar això!
                    self.taulell.mouCartaSobrantaMunt(i)
                    self.last_pseudomoviment=Moviment()
                    self.last_pseudomoviment.original=1
                    self.last_pseudomoviment.desti=i
                    self.last_pseudomoviment.zona_orig=2
                    self.last_pseudomoviment.zona_desti=1
                    self.last_pseudomoviment.carta=len(self.accesdirecte[1][i])
                    self.last_pseudomoviment.funcio=self.taulell.mouCartaMuntColumna2
                    self.accesdirecte[1][i].addElem(self.accesdirecte[2][1].pop()[0],(1,1),True)
                    moviments=self.joc.incrementaMoviments()
                    imatge=self.recursos.getfont(1).render(self.opcions.getText('game','movements')+": %d" % moviments, True, (255,255,255))
                    if self.mostrarMovimentsPossibles:
                        self.cartesMarcades=self.joc.getMoviments()
                        self.modificaMarcaMoviments(True)
                    self.vistaMoviments.set(imatge)
                    self.zonaJoc.update()
                    if self.joc.partidaFinalitzada():
                        self.menuPartidaFinalitzada()
                        self.last_pseudomoviment=False  # Per seguretat
                    else:
                        self.moviments.append(self.last_pseudomoviment)
                        # self.last_pseudomoviment=Moviment()
                    break
            if self.mostrarMovimentsPossibles:
                self.modificaMarcaMoviments(True)

    def undo(self):
        if self.interficiePartida.getMovimentsPossibles():
            cartes=self.joc.getMoviments()
            self.interficiePartida.modificaMarcaMoviments(True, cartes)
            #self.modificaMarcaMoviments( False)
        if len(self.moviments)>0:
            moviment=self.moviments.pop()
            if moviment.zona_orig==0:
                espaiat=self.opcions.espaiat[0]
            elif moviment.zona_orig==1:
                espaiat=(1,1)
            elif moviment.zona_orig==2:
                espaiat=self.opcions.espaiat[2]
            moviment.funcio(moviment.desti,moviment.carta+1, moviment.original )
            self.accesdirecte[moviment.zona_orig][moviment.original].addList(self.accesdirecte[moviment.zona_desti][moviment.desti].subPila(moviment.carta), espaiat)
            self.joc.buidaCache()
            self.debug()
        if self.mostrarMovimentsPossibles:
            cartes=self.joc.getMoviments()
            self.interficiePartida.modificaMarcaMoviments(True, cartes)



    def debug(self):
        columnes=[]
        taulell=self.taulell
        max=0;
        for i in range(0,taulell.ncolumnes()):
            columnes.append(taulell.llistaCartesColumna(i))
            if (max<len(columnes[i])):
                max=len(columnes[i])
        print max
        i=0
        while i<max:
            linea=[]
            separador=""
           # print "------------------------------------------------"
            for j in range(0,taulell.ncolumnes()):
                if (len(columnes[j])>i):
                    separador=separador+"--------"
                    if (columnes[j][i].visible):
                        carta="| %d %d " % (columnes[j][i].pal,columnes[j][i].num)
                        if (len(carta)==6):
                            linea.append(carta+" |")
                        else:
                            linea.append(carta+"|")
                    else :
                        linea.append("| X XX |")
                else:
                    linea.append("		")
                    separador=separador+"		"
            print separador
            print "".join(linea)
            i=i+1


