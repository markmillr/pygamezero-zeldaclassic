music.play("overworld.ogg")


WIDTH = 800
HEIGHT = 600

distance = 5
duration = 0.05


link = Actor('link')
link.pos = WIDTH/2, HEIGHT/2


def draw():
    screen.clear()
    link.draw()


def update():
	if keyboard.left:
		animate(link, duration = duration, pos=(link.x - distance, link.y))
	elif keyboard.right:
		animate(link, duration = duration, pos=(link.x + distance, link.y))
	elif keyboard.up:
		animate(link, duration = duration, pos=(link.x, link.y - distance))
	elif keyboard.down:
		animate(link, duration = duration, pos=(link.x, link.y + distance))
	elif keyboard.space:
		pass
