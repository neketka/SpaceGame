from engine.entity import *
from engine.vector import *
from engine.level import *
from engine.game import *
from engine.canvas import *
from engine.rectangle import *
from random import randint

def enemy3:
    if player in level0.rayCast(enemy3Weapon.getPosition(),
                                enemy3Weapon.getAngle()):  # If the enemy is in range of the player
        if enemy3.getUserData()[1] == 0:  # If the attack timer = 0, as in he is ready to shoot
            if randint(1, 4) == 1:  # 1 in 4 change to hit
                playerHealth = playerHealth - 5
        enemy3.setUserData([getUserData()[0], 100])
    else:  # can't see player
        if player.getPosition().getX() < enemy3.getPostition().getX():  # If player is on left of enemy
            if enemy3.getVelocity().getX() > -5:
                enemy3.setVelocity(enemy3.getVelocity().add(Vector(-1, 0)))
        else:  # player is on the right of the enemy
            if enemy3.getVelocity().getX() < 5:
                enemy3.setVelocity(player.getVelocity().add(Vector(1, 0)))