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
            entitiesHit[0].setUserData([getUserData[0]-5, getUserData[1]]) #deals 5 damage, doesn't change attack speed
            attackTimer = 60
    #Turning around
    if game.getMousePos().getX() > player.getPosition().getX(): #if mouse on right of player
       player.setFlipX(True) #flip = true, so face right
    else:
        player.setFlipX(False) #face left



    #ENEMY AI
    if player in level0.rayCast(enemy1Weapon.getPosition(), enemy1Weapon.getAngle()): #If the enemy is in range of the player
        if enemy1.getUserData()[1] == 0: #If the attack timer = 0, as in he is ready to shoot
           if randint(1,4) == 1: #1 in 4 change to hit
               playerHealth = playerHealth - 5
        enemy1.setUserData([getUserData()[0],100])
    else: #can't see player
       if player.getPosition().getX() < enemy1.getPostition().getX(): #If player is on left of enemy
           if enemy1.getVelocity().getX() > -5:
               enemy1.setVelocity(enemy1.getVelocity().add(Vector(-1, 0)))
       else: #player is on the right of the enemy
           if enemy1.getVelocity().getX() < 5:
               enemy1.setVelocity(player.getVelocity().add(Vector(1, 0)))
    #MEDKIT
    if player in regionTest(Rectangle(medkit1.getPosition().getX(),medkit1.getPosition().getY(),100, 100)):
        medkit1.kill
        playerHealth = playerHealth + 25


def gui
    canvas.DrawRect(Red, Rectangle(20,20, 2 * playerHealth, 20))



def level0(game):
    view = View()
    canvas = Canvas()
    player = Entity()
    player.setCollider(Rectangle(0, 0, 200, 300))
    view.attachTo(player) #camera follows him
    player.setPosition(Vector(50,50))
    enemy1 = Entity()
    enemy1Weapon = Entity()
    medkit1 = Entity()
    global attackTimer
    global playerHealth
    playerHealth= 100
    gun = Entity()

    level0 = Level()
    level0.setGravity(Vector(0, 2))
    level0.setDrag(0.9)
    level0.setSize(1000, 400)
    level0.setView(view)
    level0.addTickEvent(tick)
    level0.addGuiDrawEvent(gui)
    level0.addEntity(player)
    level0.addEntity(enemy1)
    enemy1.setUserData([10, 0]) #Health, attack timer
    player.addChild(gun)
    enemy1.addChild(enemy1Weapon)

    #Platforms
    level0.addCollider(Rectangle(84, 266, 77, 25))
    level0.addCollider(Rectangle(207, 294, 52, 14))
    level0.addCollider(Rectangle(193, 217, 56, 18))
    level0.addCollider(Rectangle(280, 179, 60, 24))