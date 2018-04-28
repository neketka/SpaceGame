from engine.entity import *
from engine.vector import *
from engine.level import *
from engine.game import *
from engine.canvas import *
from engine.rectangle import *
from engine.animation import *
from level0 import level0

def tickLevel1:


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
