extends Control

class_name Splash

# Declare member variables here. Examples:
# var a = 2
# var b = "text"

var main = preload("res://menus/main.tscn")

# Called when the node enters the scene tree for the first time.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_Timer_timeout():
	SceneManager.replace_current(main.instance());
	
