#import pixel

music.play("overworld.ogg")

WIDTH = 800
HEIGHT = 500

distance = 5
duration = 0.03

link = Actor('link_down1')
meanie = Actor('meanie2')
portal = Actor('portal', pos=(225,75))
link.pos = WIDTH/2, HEIGHT/2
meanie.pos = WIDTH/2 + 100, HEIGHT/2 + 100
link.orientation = 'down'

class GameState():
	def __init__(self):
		self.rooms = ['overworld', 'cave']
		self.current_room = self.rooms[0]
		self.portal_positions = [portal.pos]

class Overworld():
	def __init__(self):
		self.portal_positions = [(225,75)]

class Cave():
	def __init__(self):
		self.portal_positions = [(WIDTH/2, HEIGHT-20)]

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

def evaluatePosition(pos):
	if portal.collidepoint(link.pos) and gameState.current_room == 'overworld':
		gameState.current_room = 'cave'
		print(gameState.current_room)
		gameState.portal_position = cave.portal_positions[0]
		portal.pos = gameState.portal_position
		link.pos = cave.portal_positions[0]
		#print('entered portal... scene:', scene)
	elif portal.collidepoint(link.pos) and gameState.current_room == 'cave':
		gameState.current_room = 'overworld'
		print(gameState.current_room)
		gameState.portal_position = overworld.portal_positions[0]
		portal.pos = gameState.portal_position
	elif meanie.collidepoint(link.pos):
		#print('ouch')
		#print('not in portal.... scene:', scene)
		pass

gameState = GameState()
print(gameState.current_room)
overworld = Overworld()
cave = Cave()
	

def draw():
    screen.clear()
    
    screen.blit(gameState.current_room, (0, 0))
      
    portal.draw()
    link.draw()
    meanie.draw()
    
def update():

	evaluateKeyboard()
	evaluatePosition(link.pos)

		