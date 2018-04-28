import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getLength(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def getAngle(self):
        return math.atan2(self.y, self.x)

    def mix(self, other, factor):
        return self.mult(1 - factor) + other.mult(factor)

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def sub(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def neg(self):
        return Vector(-self.x, -self.y)

    def mult(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def normalized(self):
        return self.mult(1 / self.getLength())
    