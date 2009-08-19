#
#  MostrarCartes1.py
#  Solitari
#
#  Created by Dracks on 24/07/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#
from view import *
from Pantalles import Menu

class MostrarCartes(Menu):
	def __init__(self, father, recursos, opcions, dump_taulell):
		self.mostrarMovimentsPossibles=False
		imatgeMarca=Imatge(recursos.getImatgeMarca(),True,(3,3))
		piles=list()
		espaiat=opcions.getEspaiat()
		for i in range(len(dump_taulell[0])):
			pila=Pila(Fons(imatgeMarca,Imatge(recursos.getCartaNull()), False), (-2,1), opcions.getMaxDesplacamentPiles(), velositatDesplacament=opcions.getVelositatDesplacament())
			pila.setOnClick(self.clickPila,i)
			pila.setOnDobleClick((self.dobleclickColumna,i))
			for e in dump_taulell[0][i]:
				if e["visible"]:
					pila.addElem(Fons(imatgeMarca,Imatge(recursos.getCarta(e["pal"],e["numero"])),False),espaiat[0],True)
				else:
					pila.addElem(Fons(imatgeMarca,Imatge(recursos.getCartaOculta()),False),espaiat[1],False)
			piles.append(pila)  
		muntets=list()
		for i in range(len(dump_taulell[1])):
			pila=Pila(Fons(imatgeMarca,Imatge(recursos.getCartaNull()),False),creixer=False)
			pila.setOnClick(self.clickMunt,i)
			for e in dump_taulell[1][i]:
				pila.addElem(Fons(imatgeMarca,Imatge(recursos.getCarta(e["pal"],e["numero"])),False),(1,1),False)
			pila.update()
			muntets.append(pila)
		
		sobrants=False
		if dump_taulell[2]!=False:
			#cartes_sobrants=self.taulell.llistaCartesSobrantsOcultes()
			p_sobrants_ocultes=Pila(Imatge(recursos.getCartaNull()),creixer=False)
			p_sobrants_ocultes.setOnClick(self.clickSobrantsOcultes,None)
			for e in dump_taulell[2]["ocultes"]:
				p_sobrants_ocultes.addElem(Fons(imatgeMarca,Imatge(recursos.getCartaOculta()),False),(1,1),False)
			#cartes_sobrants=taulell.llistaCartesSobrantsVisibles()
			p_sobrants_visibles=Pila(Ghost(),(10,0),opcions.getMaxDesplacamentExtres(), velositatDesplacament=opcions.getVelositatDesplacament())
			p_sobrants_visibles.setOnClick(self.clickSobrantsVisibles, None)
			p_sobrants_visibles.setOnDobleClick((self.dobleclickSobrants, None))
			for e in dump_taulell[2]["visibles"]:
				p_sobrants_visibles.addElem(Fons(imatgeMarca,Imatge(recursos.getCarta(e["pal"],e["numero"])),False),espaiat[2],True)
			sobrants=(p_sobrants_ocultes,p_sobrants_visibles)
		#else:
			#sobrants=False
			
		self.accesdirecte=(piles, muntets, sobrants)
		
		All=VArea(20)
		Interficie=HArea(20)
		Interficie.addElem(Ghost())		
		for p in self.accesdirecte[0]:
			Interficie.addElem(p)
		Interficie.addElem(Reomple(Interficie, (opcions.getResolucio()[0],1)))
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
			
		menu=Fons(Imatge(recursos.getfonsMenu(), True),All)
		Menu.__init__(self, father, menu)
		
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
	