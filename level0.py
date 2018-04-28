from engine.entity import *
from engine.vector import *
from engine.level import *
from engine.game import *
from engine.canvas import *
from engine.rectangle import *
from random import randint



def tick(deltaTime): #Stuff that happens every frame
    #Movement (Right, left, jump, crouch)
    if game.isKeyDown(SDL_SCANCODE_D):
        if player.getVelocity().getX() < 5:
            player.setVelocity(player.getVelocity().add(Vector(1, 0)))
    if game.isKeyDown(SDL_SCANCODE_A):
        if player.getVelocity().getX() > -5:
            player.setVelocity(player.getVelocity().add(Vector(-1, 0)))
    if game.isKeyDown(SDL_SCANCODE_W) and isGrounded():
        player.setVelocity(Vector(0,5))
    if game.isKeyDown(SDL_SCANCODE_S):
        player.setCollider(Rectangle(0, 0, 200, 150))
        player.setPosition(player.getPosition().add(Vector(0,-150)))
        croaching = 1
    else:
        if croaching == 1:
            player.setCollider(Rectangle(0, 0, 200, 300))
            player.setPosition(player.getPosition().add(Vector(0, 150)))
            croaching = 0

            #Shooting
    gun.setRotation(gun.getPosition().sub(game.getMousePos()).getAngle()) #Constantly points gun at mouse
    enemy1Weapon.setRotation(enemy1Weapon.getPosition().sub(player.getPosition()).getAngle())

    #attack speed
    if attackTimer > 0:
        attackTimer = attackTimer - 1


    if game.isMouseDown(1) and attackTimer == 0:
        if gunNumber == 1:
            entitiesHit = level0.rayCast(gun.getPosition(), gun.getAngle())
            entitiesHit[0].kill()
            attackTimer = 60
    #Turning around
    if game.getMousePos().getX() > player.getPosition().getX(): #if mouse on right of player
       player.setFlipX(True) #flip = true, so face right
    else:
        player.setFlipX(False) #face left

#GUI
    canvas.DrawRect(Red, Rectangle(20,20, 20 * playerHealth, 20))

    #ENEMY AI
    if player in level0.rayCast(enemy1Weapon.getPosition(), enemy1Weapon.getAngle()): #If the enemy is in range of the player
        if
            randint(1,4)




def level0(game):
    view = View()
    canvas = Canvas()
    player = Entity()
    player.setCollider(Rectangle(0, 0, 200, 300))
    view.attachTo(player) #camera follows him
    player.setPosition(Vector(50,50))
    enemy1 = Entity()
    enemy1Weapon = Entity()
    global attackTimer
    global playerHealth
    playerHealth= 10
    gun= Entity()

    level0 = Level()
    level0.setGravity(Vector(0, 2))
    level0.setDrag(0.9)
    level0.setSize(1000, 400)
    level0.setView(view)
    level0.addTickEvent(tick)
    level0.addEntity(player)
    level0.addEntity(enemy1)
    player.addChild(gun)
    enemy1.addChild(enemy1Weapon)
