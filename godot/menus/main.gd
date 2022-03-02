extends Control


# Declare member variables here. Examples:
var tableGame := preload("res://game/board.tscn")


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_6_munts_pressed():
	SceneManager.replace_current(tableGame.instance())
