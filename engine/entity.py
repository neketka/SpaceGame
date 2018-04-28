from engine.vector import *
from engine.rectangle import *


class Entity:
    def __init__(self):
        self.pos = Vector(0, 0)
        self.velocity = Vector(0, 0)
        self.rot = 0
        self.scale = 1
        self.flipX = False
        self.flipY = False
        self.image = None
        self.isImage = True
        self.collider = None
        self.children = []
        self.userData = None
        self.alive = True
        self.isGround = False

    def setPosition(self, vector):
        self.pos = vector

    def setScale(self, factor):
        self.scale = factor

    def setRotation(self, angle):
        self.rot = angle

    def setFlipX(self, flipX):
        self.flipX = flipX

    def setFlipY(self, flipY):
        self.flipY = flipY

    def setVelocity(self, vector):
        self.velocity = vector

    def setCollider(self, rectangle):
        self.collider = rectangle

    def setDieOnImpact(self, dieOnImpact):
        pass

    def setImage(self, image):
        self.image = image
        self.isImage = True

    def setAnimation(self, animation):
        self.image = animation
        self.isImage = False

    def addChild(self, child):
        self.children.append(child)

    def setUserData(self, data):
        self.userData = data

    def setLifetime(self, lifetime):
        pass

    def setGrounded(self, grounded):
        self.isGround = grounded

    def kill(self):
        self.alive = False

    def getPosition(self):
        return self.pos

    def getScale(self):
        return self.scale

    def getRotation(self):
        return self.rot

    def getFlipX(self):
        return self.flipX

    def getFlipY(self):
        return self.flipY

    def getVelocity(self):
        return self.velocity

    def getCollider(self):
        if self.collider is None:
            return None
        """
        point0 = Vector(self.collider.x - self.collider.width / 2, self.collider.y - self.collider.height / 2)
        point1 = point0.add(Vector(self.collider.width, self.collider.height))
        corner = point0.mult(self.scale) + Vector(self.collider.x, self.collider.y)
        size = point1 - point0
        """
        return Rectangle(self.getPosition().getX(), self.getPosition().getY(),
                         self.collider.width * self.scale, self.collider.height * self.scale)

    def doesDieOnImpact(self):
        pass

    def getImage(self):
        if self.isImage:
            return self.image
        return self.image.getCurrentFrame()

    def getChildren(self):
        return self.children

    def getUserData(self):
        return self.userData

    def isAlive(self):
        return self.alive

    def isGrounded(self):
        return self.isGround

