from engine.vector import *


class Viewer:
    def __init__(self):
        self.center = Vector(0, 0)
        self.scale = 10
        self.windowW = 640
        self.windowH = 480
        self.minX = 0
        self.maxX = 1000000000
        self.minY = 0
        self.maxY = 1000000000
        self.entity = None
        self.viewSize = Vector(26, 20)

    def setCenter(self, vector):
        self.center = vector

    def setScale(self, factor):
        self.scale = factor

    def setWindowSize(self, size):
        self.windowW = int(size.getX())
        self.windowH = int(size.getY())

    def setMinXConstraint(self, x):
        self.minX = x

    def setMaxXConstraint(self, x):
        self.maxX = x

    def setMinYConstraint(self, y):
        self.minY = y

    def setMaxYConstraint(self, y):
        self.maxY = y

    def update(self):
        if self.entity is not None:
            self.center = self.entity.getCollider().getCenter()
        aspect = self.windowW / self.windowH
        if aspect > 1:
            self.viewSize = Vector(self.scale * aspect, self.scale)
        else:
            self.viewSize = Vector(self.scale, self.scale / aspect)
        leftSide = self.center.getX() - self.viewSize.getX() / 2
        rightSide = self.center.getX() + self.viewSize.getX() / 2
        topSide = self.center.getY() - self.viewSize.getY() / 2
        bottomSide = self.center.getY()() + self.viewSize.getY() / 2
        if leftSide < self.minX:
            self.center = Vector(self.center.getX() + (self.minX - leftSide), self.center.getY())
        if rightSide > self.maxX:
            self.center = Vector(self.center.getX() - (rightSide - self.maxX), self.center.getY())
        if topSide < self.minY:
            self.center = Vector(self.center.getX(), self.center.getY() + (self.minY - topSide))
        if bottomSide > self.maxY:
            self.center = Vector(self.center.getX(), self.center.getY() - (self.minY - topSide))

    def attachTo(self, entity):
        self.entity = entity

    def detachEntity(self):
        self.entity = None

    def getCenter(self):
        return self.center

    def getSize(self):
        return Vector(self.windowW, self.windowH)
