from engine.entity import *
from engine.vector import *
from engine.level import *
from engine.game import *
from engine.canvas import *
from engine.rectangle import *
from random import randint

def enemy1:
    if player in level0.rayCast(enemy1Weapon.getPosition(),
                                enemy1Weapon.getAngle()):  # If the enemy is in range of the player
        if enemy1.getUserData()[1] == 0:  # If the attack timer = 0, as in he is ready to shoot
            if randint(1, 4) == 1:  # 1 in 4 change to hit
                playerHealth = playerHealth - 5
        enemy1.setUserData([getUserData()[0], 100])
    else:  # can't see player
        if player.getPosition().getX() < enemy1.getPostition().getX():  # If player is on left of enemy
            if enemy1.getVelocity().getX() > -5:
                enemy1.setVelocity(enemy1.getVelocity().add(Vector(-1, 0)))
        else:  # player is on the right of the enemy
            if enemy1.getVelocity().getX() < 5:
                enemy1.setVelocity(player.getVelocity().add(Vector(1, 0)))