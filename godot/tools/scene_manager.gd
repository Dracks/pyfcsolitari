extends Node


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
onready var root : Node= get_tree().get_root()

# Called when the node enters the scene tree for the first time.
#func _ready():
	
func replace_current(scene: Node):
	var current_scene = root.get_child( root.get_child_count() -1 )
	root.add_child(scene)
	current_scene.queue_free()
	


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
