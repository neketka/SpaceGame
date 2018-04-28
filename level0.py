from engine.entity import *
from engine.vector import *
from engine.level import *
from engine.game import *
from engine.canvas import *
from engine.rectangle import *
from engine.animation import *
from engine.color import *

from enemies.enemy1 import enemy1
from enemies.enemy2 import enemy2
from enemies.enemy3 import enemy3
from enemies.enemy4 import enemy4


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


    if game.isMouseDown(SDL_BUTTON_LEFT) and attackTimer == 0:
        if gunNumber == 1:
            entitiesHit = level0.rayCast(gun.getPosition(), gun.getAngle())
            if entitiesHit != []:
                entitiesHit[0].setUserData([getUserData[0]-5, getUserData[1]]) #deals 5 damage, doesn't change attack speed
                attackTimer = 60
    #Turning around
    if game.getMousePos().getX() > player.getPosition().getX(): #if mouse on right of player
       player.setFlipX(True) #flip = true, so face right
    else:
        player.setFlipX(False) #face left


    #ENEMY AI
    enemy1()
    enemy2()
    enemy3()
    enemy4()
    #MEDKIT
    if player in regionTest(Rectangle(medkit1.getPosition().getX(),medkit1.getPosition().getY(),100, 100)):
        medkit1.kill()
        playerHealth = playerHealth + 25


def gui():
    canvas.DrawRect(Color(1, 0, 0), Rectangle(20,20, 2 * playerHealth, 20))



def level0(game):
    global attackTimer
    global playerHealth
    global player
    global view
    view = View()
    canvas = Canvas()
    player = Entity()
    player.setCollider(Rectangle(0, 0, 200, 300))
    view.attachTo(player) #camera follows him
    player.setPosition(Vector(50,50))
    enemy1 = Entity()
    enemy1Weapon = Entity()
    medkit1 = Entity()
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
    level0.setBackground(game.getAsset("map2.png"))


    enemy2 = Entity()
    enemy2Weapon = Entity()
    level0.addEntity(enemy2)
    enemy2.setUserData([10, 0])  # Health, attack timer
    enemy2.addChild(enemy2Weapon)
    enemy3 = Entity()
    enemy3Weapon = Entity()
    level0.addEntity(enemy3)
    enemy3.setUserData([10, 0])  # Health, attack timer
    enemy3.addChild(enemy3Weapon)
    enemy4 = Entity()
    enemy4Weapon = Entity()
    level0.addEntity(enemy4)
    enemy4.setUserData([10, 0])  # Health, attack timer
    enemy4.addChild(enemy4Weapon)

#Hitboxes
    enemy1.setCollider(Rectangle(0, 0, 200, 300))
    enemy2.setCollider(Rectangle(0, 0, 200, 300))
    enemy3.setCollider(Rectangle(0, 0, 200, 300))
    enemy4.setCollider(Rectangle(0, 0, 200, 300))


    #Platforms
    level0.addCollider(Rectangle(84, 266, 77, 25))
    level0.addCollider(Rectangle(207, 294, 52, 14))
    level0.addCollider(Rectangle(193, 217, 56, 18))
    level0.addCollider(Rectangle(280, 179, 60, 24))
    level0.addCollider(Rectangle(315, 312, 46, 14))
    level0.addCollider(Rectangle(389, 214, 49, 21))
    level0.addCollider(Rectangle(462, 322, 32, 18))
    level0.addCollider(Rectangle(592, 308, 42, 14))


    level0.addCollider(Rectangle(0, 340, 3499, 10)) #Ground

    #Animations
    enemyWalking = Animation([game.getAsset("AFrame.png"),game.getAsset("BFrame.png"),game.getAsset("CFrame.png"),game.getAsset("DFrame.png"),game.getAsset("EFrame.png")],game.getAsset("DFrame.png"),game.getAsset("CFrame.png"),game.getAsset("BFrame.png"), 1)
    MainCWalking = Animation([game.getAsset("Maincharacter2 - FRAME1.png"),game.getAsset("Maincharacter2 - FRAME2.png"),game.getAsset("Maincharacter2 - FRAME3.png"),game.getAsset("Maincharacter2 - FRAME4.png"),game.getAsset("Maincharacter2 - FRAME5.png"),game.getAsset("Maincharacter2 - FRAME6.png"),game.getAsset("Maincharacter2 - FRAME7.png"),game.getAsset("Maincharacter2 - FRAME8.png"),game.getAsset("Maincharacter2 - FRAME9.png"),game.getAsset("Maincharacter2 - FRAME10.png"),game.getAsset("Maincharacter2 - FRAME11.png"),game.getAsset("Maincharacter2 - FRAME12.png"),game.getAsset("Maincharacter2 - FRAME13.png")], 2)