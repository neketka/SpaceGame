from engine.entity import *
from engine.vector import *
from engine.level import *
from engine.game import *
from engine.canvas import *
from engine.rectangle import *
from engine.animation import *
from level0 import level0

def tickLevel1:
    if game.isKeyDown(SDL_SCANCODE_D):
        if player.getVelocity().getX() < 5:
            player.setVelocity(player.getVelocity().add(Vector(1, 0)))
    if game.isKeyDown(SDL_SCANCODE_A):
        if player.getVelocity().getX() > -5:
            player.setVelocity(player.getVelocity().add(Vector(-1, 0)))
    if game.isKeyDown(SDL_SCANCODE_W) and isGrounded():
        player.setVelocity(Vector(0, 5))
    if game.isKeyDown(SDL_SCANCODE_S):
        player.setCollider(Rectangle(0, 0, 200, 150))
        player.setPosition(player.getPosition().add(Vector(0,-150)))
        croaching = 1
    else:
        if croaching == 1:
            player.setCollider(Rectangle(0, 0, 200, 300))
            player.setPosition(player.getPosition().add(Vector(0, 150)))
            croaching = 0

    if game.getMousePos().getX() > player.getPosition().getX(): #if mouse on right of player
       player.setFlipX(True) #flip = true, so face right
    else:
        player.setFlipX(False) #face left



def level0(game):
    view = View()
    canvas = Canvas()
    player = Entity()
    player.setCollider(Rectangle(0, 0, 200, 300))
    level1 = Level()
    level1.setGravity(Vector(0, 2))
    level1.setDrag(0.9)
    level1.setSize(1000, 400)
    level1.setView(view)
    level1.addTickEvent(tickLevel1)
    level1.addEntity(player)
    level0.setBackground(game.getAsset("shuttle.png"))
    level0.addCollider(Rectangle(0, 340, 3499, 10)) #Ground
