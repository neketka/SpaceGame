from engine.entity import *
from engine.vector import *
from engine.level import *
from engine.game import *

def tick(deltaTime): #Stuff that happens every frame
    #Movement (Right, left, jump, crouch)
    if game.isKeyDown(SDL_SCANCODE_D):
        if player.getVelocity().getX() < 5:
            player.setVelocity(player.getVelocity().add(Vector(1, 0)))
    if game.isKeyDown(SDL_SCANCODE_A):
        if player.getVelocity().getX() > -5:
            player.setVelocity(player.getVelocity().add(Vector(-1, 0)))
    if game.isKeyDown(SDL_SCANCODE_W) and isGrounded() == true:
            player.setVelocity((Vector(0,5))
    if game.isKeyDown(SDL_SCANCODE_S):
        player.setCollider(Rectangle(0, 150, 200, 150))
    #Shooting
    gun.setRotation(gun.getPosition().sub(game.getMousePos()).getAngle()) #Constantly points gun at mouse
    if game.isMouseDown(1):
        if gunNumber == 1:
            entitiesHit = level0.rayCast(gun.getPosition(), gun.getAngle()))
            closestEnemy = 100000000 #just a really big number
            for hitEnemy in entitiesHit:
                if gun.getPosition().sub(hitenemy.getPosition()).getLength() <  closestEnemy:
                    closestEnemy = gun.getPosition().sub(hitenemy.getPosition()).getLength()
            closestEnemy.kill





def main():
    game = Game("Space Game")
    view = View()
    player = Entity()
    player.setCollider(Rectangle(0, 0, 200, 300))
    view.attachTo(player) #camera follows him
    player.setPosition(Vector(50,50))

    gunNumber = 1 #1 = pistol,
    #Gun
    gun = Entity()

    level0 = Level()
    level0.setGravity(Vector(0, 2))
    level0.setDrag(0.9)
    level0.setSize(1000, 400)
    level0.setView(view)
    level0.addTickEvent(tick)
    level0.addEntity(player)
    level0.addEntity(enemy)


    player.addChild(gun)
    gun.getPosition().sub(Game.getMousePos()).getAngle() #gets angle
