music.play("overworld.ogg")

link = Actor('link')
link.topright = 0, 10

WIDTH = 500
HEIGHT = link.height + 20

def draw():
    screen.clear()
    link.draw()

def update():
    link.left += 2
    if link.left > WIDTH:
        link.right = 0

