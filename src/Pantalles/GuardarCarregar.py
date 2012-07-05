#
#  GuardarCarregar.py
#  Solitari
#
#  Created by dracks on 11/07/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#

import ViewGL
import Pantalles
import Widgets

class GuardarCarregar(Pantalles.Menu):
	def __init__(self, father, recursos, opcions, actions, textos, dades):
		imatge1=recursos.getimgBoto()
		font=recursos.getfont(1)
		font2=recursos.getfont(2)
		
		self.actions=actions
		self.dades=dades
		
		pla=Widgets.VerticalLayout(0)
		titol=Widgets.Image(font2.render(textos[0], (100,100,100)))
		pla.addElement(Widgets.Center(contents=titol,surface=(600,35)))
		content=Widgets.VerticalLayout(15)
		pla.addElement(Widgets.Center(contents=content,surface=(600,400)))
		boto_partida1=Widgets.Button(recursos.getPartidaGuardarCarregar(), textos[1], font)
		boto_partida1.setOnMouseClick(self.accioBoto,1)
		content.addElement(boto_partida1);
		boto_partida2=Widgets.Button(recursos.getPartidaGuardarCarregar(), textos[2], font)
		boto_partida2.setOnMouseClick(self.accioBoto,2)
		content.addElement(boto_partida2);
		boto_partida3=Widgets.Button(recursos.getPartidaGuardarCarregar(), textos[3], font)
		boto_partida3.setOnMouseClick(self.accioBoto,3)
		content.addElement(boto_partida3);
		boto_partida4=Widgets.Button(recursos.getPartidaGuardarCarregar(), textos[4], font)
		boto_partida4.setOnMouseClick(self.accioBoto,4)
		content.addElement(boto_partida4);
		cancel=Widgets.Button(imatge1, opcions.getText('Generic','cancel'), font)
		cancel.setOnMouseClick(self.cancel);
		#boto.setOnClick(self.deGuardaraJoc, None)
		content.addElement(Widgets.VerticalFill(parent=content,size=300))
		content.addElement(Widgets.Center(contents=cancel, surface=(500,20)))
		#self.menuGuardarCarregar=(Centre(Fons(Imatge(recursos.getmenuGuardariCarregar()),pla), opcions.resolucio), (boto_partida1,boto_partida2,boto_partida3, boto_partida4), titol, cancel)
	
		Pantalles.Menu.__init__(self, father, Widgets.Center(contents=Widgets.Background(Widgets.Image(recursos.getmenuGuardariCarregar()),pla), surface=opcions.getResolucio()))
	
	def accioBoto(self, params):
		if self.actions[params]!=None:
			self.actions[params](self.dades[params])
		
	def cancel(self, params):
		self.actions[0]()
	
	
