music.play("overworld.ogg")


WIDTH = 800
HEIGHT = 600


link = Actor('link')
link.pos = WIDTH/2, HEIGHT/2


def draw():
    screen.clear()
    link.draw()


def update():
	if keyboard.left:
		animate(link, pos=(link.x - 100, link.y))
	elif keyboard.right:
		animate(link, pos=(link.x + 100, link.y))
