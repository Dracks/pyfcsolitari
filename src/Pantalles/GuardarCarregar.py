#
#  GuardarCarregar.py
#  Solitari
#
#  Created by dracks on 11/07/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#

import ViewGL
import Pantalles

class GuardarCarregar(Pantalles.Menu):
	def __init__(self, father, recursos, opcions, actions, textos, dades):
		imatge1=recursos.getimgBoto()
		font=recursos.getfont(1)
		font2=recursos.getfont(2)
		
		self.actions=actions
		self.dades=dades
		
		pla=VArea(0)
		titol=Imatge(font2.render(textos[0], True, (100,100,100)))
		pla.addElem(Centre(titol, (600,35)))
		content=VArea(15)
		pla.addElem(Centre(content, (600,400)))
		boto_partida1=Boto(recursos.getPartidaGuardarCarregar(), textos[1], font)
		boto_partida1.setOnClick(self.accioBoto,1)
		content.addElem(boto_partida1);
		boto_partida2=Boto(recursos.getPartidaGuardarCarregar(), textos[2], font)
		boto_partida2.setOnClick(self.accioBoto,2)
		content.addElem(boto_partida2);
		boto_partida3=Boto(recursos.getPartidaGuardarCarregar(), textos[3], font)
		boto_partida3.setOnClick(self.accioBoto,3)
		content.addElem(boto_partida3);
		boto_partida4=Boto(recursos.getPartidaGuardarCarregar(), textos[4], font)
		boto_partida4.setOnClick(self.accioBoto,4)
		content.addElem(boto_partida4);
		cancel=Boto(imatge1, opcions.getText('Generic','cancel'), font)
		cancel.setOnClick(self.cancel,None);
		#boto.setOnClick(self.deGuardaraJoc, None)
		content.addElem(Reomple(content,(500,300)))
		content.addElem(Centre(cancel, (500,20)))
		#self.menuGuardarCarregar=(Centre(Fons(Imatge(recursos.getmenuGuardariCarregar()),pla), opcions.resolucio), (boto_partida1,boto_partida2,boto_partida3, boto_partida4), titol, cancel)
	
		Pantalles.Menu.__init__(self, father, Centre(Fons(Imatge(recursos.getmenuGuardariCarregar()),pla), opcions.getResolucio()))
	
	def accioBoto(self, params):
		if self.actions[params]!=None:
			self.actions[params](self.dades[params])
		
	def cancel(self, params):
		self.actions[0]()
	
	
