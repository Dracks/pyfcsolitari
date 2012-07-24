# -*- coding: UTF-8 -*-
#
#  InterficiePartida.py
#  Solitari
#
#  Created by Dracks on 13/07/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#
import ViewGL
import Pantalles
import Widgets

class InterficiePartida(Pantalles.Menu):
	def __init__(self, father, recursos, opcions, interficie, mouse, moviments):
		self.moviments=list()
		Visible=Widgets.VerticalLayout(2)
		self.mouse=mouse
		
		boto=Widgets.Button(recursos.getimgBoto(), opcions.getText('game','menu'), recursos.getfont(1))
		boto.setOnMouseClick(self.aMenuJoc)
		barra=Widgets.HorizontalLayout(10)
		barra.addElement(Widgets.Empty())
		barra.addElement(boto);
		boto=Widgets.Button(recursos.getimgBoto(), opcions.getText('game','undo'), recursos.getfont(1))
		boto.setOnMouseClick(self.undo)
		barra.addElement(boto)
		boto=Widgets.Button(recursos.getimgBoto(), opcions.getText('game','save'), recursos.getfont(1))
		boto.setOnMouseClick(self.aMenuGuardar,None)
		barra.addElement(boto)
		boto=Widgets.Button(recursos.getimgBoto(), opcions.getText('game','viewmovements'), recursos.getfont(1))
		boto.setOnMouseClick(self.activaMoviments,None)
		self.botoVisualitzarMoviments=boto
		barra.addElement(boto)
		barra.addElement(Widgets.HorizontalFill(opcions.getResolucio()[0],barra))
		self.vistaMoviments=Widgets.Image(recursos.getfont(1).render(opcions.getText('game','movements')+": %d" % moviments,(255,255,255)))
		barra.addElement(self.vistaMoviments)
		barra.addElement(Widgets.Empty())
		Visible.addElement(barra)
		self.scroll=Widgets.Scroll((opcions.getResolucio()[0], opcions.getResolucio()[1]-30))
		self.scroll.setElement(interficie.get())
		Visible.addElement(self.scroll)
		#self.interficie.setPrimerPla(Visible)
		#Visible.update()
		self.zonaJoc=interficie;
		#self.interficie.setOnMouseMove(self.tractaScroll)
		
		Pantalles.Menu.__init__(self, father, Visible)
		
	def getScroll(self):
		return self.scroll
	
	def setMoviments(self, moviments):
		self.vistaMoviments.set(Imatge(recursos.getfont(1).render(opcions.getText('game','movements')+": %d" % moviments,(255,255,255))))
		
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
		pos=self.scroll.getPos();
		tam_joc=self.scroll.getTamany()
		tam_fons=self.scroll.getTamContents();
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
		self.scroll.desplaca((x,y))
		
	
	def undo(self, button):
		self.father.undo()
		
	def aMenuJoc(self, params):
		self.father.aMenuJoc()
		
	def aMenuGuardar(self, params):
		self.father.aMenuGuardar()
		
	def desactivaMoviments(self, params):
		self.father.desactivaMoviments()
		
	def activaMoviments(self, params):
		self.father.activaMoviments()
	
	def setMovimentsText(self, text, funcio):
		self.botoVisualitzarMoviments.setText(text)
		self.botoVisualitzarMoviments.setOnClick(funcio, None)

	