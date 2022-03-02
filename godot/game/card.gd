extends Spatial

class_name Card


var type: String
var card: int
var is_hidden: bool

onready var uncover_animation := $UncoverAnimation
onready var front :Sprite3D= $Card/front


func init(type: String, card: int, cover: bool):
	self.type = type
	self.card = card
	self.is_hidden = cover
	
	self.load_resource()
	self.load_card()
	
	if not cover:
		uncover_animation.seek(1, true)

func load_resource():
	front.set_texture(load("res://resources/creativecommons/"+self.type+"vector.png"))
	
func load_card():
	front.frame = self.card-1

func reveal_card():
	uncover_animation.play("rotate")
	

