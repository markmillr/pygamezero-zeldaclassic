music.play("overworld.ogg")

WIDTH = 800
HEIGHT = 500

distance = 5
duration = 0.05

link = Actor('link_down1')
link.pos = WIDTH/2, HEIGHT/2

def set_link_normal():
	link.image = 'link_down1'

def attack():
	link.image = 'attack_down'
	

def draw():
    screen.clear()
    screen.blit('overworld', (0, 0))
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
	elif keyboard.a:
		attack()
		clock.schedule(set_link_normal, 0.2)
		