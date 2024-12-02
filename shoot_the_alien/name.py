import pgzrun
from random import randint

TITLE="Shoot_the_alien"
WIDTH=600
HEIGHT=400

alien=Actor("alien")
explosion=Actor("explosion")
explosion.visible=False

def draw():
    screen.clear()
    screen.fill("white")
    alien.draw()
    if explosion.visible==True:
        explosion.draw()

def position():
    alien.x=randint(50, WIDTH -30)
    alien.y=randint(50, HEIGHT -30)

def update():
    pass
position()

pgzrun.go()