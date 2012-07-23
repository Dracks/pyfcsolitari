#
#  MostrarCartes1.py
#  Solitari
#
#  Created by Dracks on 24/07/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#
import ViewGL
import Pantalles
import Widgets

class MostrarCartes(Pantalles.Menu):
    def __init__(self, father, recursos, opcions, dump_taulell):
        self.mostrarMovimentsPossibles=False
        imatgeMarca=Widgets.Image(recursos.getImatgeMarca())
        piles=list()
        espaiat=opcions.getEspaiat()
        for i in range(len(dump_taulell[0])):
            pila=Widgets.Stack(Widgets.Background(Widgets.Image(recursos.getCartaNull()), imatgeMarca))
            #pila.setOnClick(self.clickPila,i)
            #pila.setOnDobleClick((self.dobleclickColumna,i))
            for e in dump_taulell[0][i]:
                if e["visible"]:
                    pila.addElement(Widgets.Background(Widgets.Image(recursos.getCarta(e["pal"],e["numero"])),imatgeMarca),espaiat[0],True)
                else:
                    pila.addElement(Widgets.Background(Widgets.Image(recursos.getCartaOculta()),imatgeMarca),espaiat[1],False)
            piles.append(pila)  
        muntets=list()
        for i in range(len(dump_taulell[1])):
            pila=Widgets.Stack(Widgets.Background(Widgets.Image(recursos.getCartaNull()),imatgeMarca))
            #pila.setOnClick(self.clickMunt,i)
            for e in dump_taulell[1][i]:
                pila.addElement(Widgets.Background(Widgets.Image(recursos.getCarta(e["pal"],e["numero"])),imatgeMarca),(1,1),False)
            pila.update()
            muntets.append(pila)
        
        sobrants=False
        if dump_taulell[2]!=False:
            #cartes_sobrants=self.taulell.llistaCartesSobrantsOcultes()
            p_sobrants_ocultes=Widgets.Stack(Widgets.Image(recursos.getCartaNull()))
            #p_sobrants_ocultes.setOnClick(self.clickSobrantsOcultes,None)
            for e in dump_taulell[2]["ocultes"]:
                p_sobrants_ocultes.addElement(Widgets.Background(Widgets.Image(recursos.getCartaOculta()),imatgeMarca),(1,1),False)
            #cartes_sobrants=taulell.llistaCartesSobrantsVisibles()
            p_sobrants_visibles=Widgets.Stack(Widgets.Empty())
            #p_sobrants_visibles.setOnClick(self.clickSobrantsVisibles, None)
            #p_sobrants_visibles.setOnDobleClick((self.dobleclickSobrants, None))
            for e in dump_taulell[2]["visibles"]:
                p_sobrants_visibles.addElement(Widgets.Background(Widgets.Image(recursos.getCarta(e["pal"],e["numero"])),imatgeMarca),espaiat[2],True)
            sobrants=(p_sobrants_ocultes,p_sobrants_visibles)
        #else:
            #sobrants=False
            
        self.accesdirecte=(piles, muntets, sobrants)
        
        All=Widgets.VerticalLayout(20)
        Interficie=Widgets.HorizontalLayout(20)
        Interficie.addElement(Widgets.Empty())
        for p in self.accesdirecte[0]:
            Interficie.addElement(p)
        Interficie.addElement(Widgets.HorizontalFill(opcions.getResolucio()[0],Interficie))
        muntets=Widgets.VerticalLayout(15)
        Interficie.addElement(muntets)
        #for p in self.accesdirecte[1]:
        muntets.addElement(self.accesdirecte[1][0])
        muntets.addElement(self.accesdirecte[1][1])
        muntets=Widgets.VerticalLayout(15)
        Interficie.addElement(muntets)
        muntets.addElement(self.accesdirecte[1][2])
        muntets.addElement(self.accesdirecte[1][3])
        Interficie.addElement(Widgets.Empty())
        All.addElement(Interficie)
        if self.accesdirecte[2]!=False:
            Interficie2=Widgets.HorizontalLayout(20)
            Interficie2.addElement(Widgets.Empty())
            Interficie2.addElement(self.accesdirecte[2][0])
            Interficie2.addElement(Widgets.Empty())
            Interficie2.addElement(self.accesdirecte[2][1])
            All.addElement(Interficie2)
            
        menu=Widgets.Background(Widgets.Image(recursos.getfonsMenu()),All)
        Pantalles.Menu.__init__(self, father, menu)
        
    def dobleclickColumna(self):
        None
    def clickPila(self):
        None
    def clickSobrantsVisibles(self):
        None
    def clickMunt(self):
        None
    def dobleclickSobrants(self):
        None
    def clickSobrantsOcultes(self):
        None
    #
    #  Function Cut : Talla una pila d'una seccio, per una carta en concret
    #  (seccio_orig, pila_orig, carta_orig): dades desde on estaven les cartes
    def cut(self,(seccio, pila, carta)):
        self.accesdirecte[seccio][pila].subPila(carta-1)
        return 
        
    #  Function add : affegeix les cartes concretes
    #  (seccio_orig, pila_orig): Dades d'on es fiquen les cartes
    def add(self,(seccio, pila), cartes):
        self.accesdirecte[seccio][pila].append(cartes)
    
        
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
    
    def getEstatMarcaMoviments(self):
        return self.estatMarcaMoviments
    
    def modificaMarcaMoviments(self, estat, cartes):
        self.estatMarcaMoviments=estat
        for elem in cartes:
            if elem[2]==-1:
                self.accesdirecte[elem[0]][elem[1]].getEmpty().setMostrarFons(estat)
            else:
                self.accesdirecte[elem[0]][elem[1]].getAll()[elem[2]].setMostrarFons(estat)
    