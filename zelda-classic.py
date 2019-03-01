music.play("overworld.ogg")

WIDTH = 800
HEIGHT = 500

distance = 5
duration = 0.05

portal_x = range(0,1)
portal_y = range(0,1)

link = Actor('link_down1')
link.pos = WIDTH/2, HEIGHT/2
link.orientation = 'down'

def set_link_normal():
	link.image = 'link_down1'

def set_link_image():
	link.image = 'link_' + link.orientation + '1'

def attack():
	link.image = 'attack_' + link.orientation
	sounds.sword.play()

def evaluateKeyboard():
	if keyboard.left:
		animate(link, duration = duration, pos=(link.x - distance, link.y))
		link.orientation = 'left'
		set_link_image()
	elif keyboard.right:
		animate(link, duration = duration, pos=(link.x + distance, link.y))
		link.orientation = 'right'
		set_link_image()
	elif keyboard.up:
		animate(link, duration = duration, pos=(link.x, link.y - distance))
		link.orientation = 'up'
		set_link_image()
	elif keyboard.down:
		animate(link, duration = duration, pos=(link.x, link.y + distance))
		link.orientation = 'down'
		set_link_image()
	elif keyboard.a:
		attack()
		clock.schedule(set_link_image, 0.2)	

def evaluatePosition():
	if link.x in portal_x and link.y in portal_y:
		pass

def draw():
    screen.clear()
    screen.blit('overworld', (0, 0))
    link.draw()

def update():

	evaluateKeyboard()
	evaluatePosition()

		