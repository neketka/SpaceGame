from engine.entity import *
from engine.vector import *
from engine.level import *
from engine.game import *
from engine.canvas import *
from engine.rectangle import *
from random import randint

def enemy2:
    if player in level0.rayCast(enemy2Weapon.getPosition(),
                                enemy2Weapon.getAngle()):  # If the enemy is in range of the player
        if enemy2.getUserData()[1] == 0:  # If the attack timer = 0, as in he is ready to shoot
            if randint(1, 4) == 1:  # 1 in 4 change to hit
                playerHealth = playerHealth - 5
        enemy2.setUserData([getUserData()[0], 100])
    else:  # can't see player
        if player.getPosition().getX() < enemy2.getPostition().getX():  # If player is on left of enemy
            if enemy2.getVelocity().getX() > -5:
                enemy2.setVelocity(enemy2.getVelocity().add(Vector(-1, 0)))
        else:  # player is on the right of the enemy
            if enemy2.getVelocity().getX() < 5:
                enemy2.setVelocity(player.getVelocity().add(Vector(1, 0)))