from engine.vector import *


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getPosition(self):
        return Vector(self.x, self.y)

    def getSize(self):
        return Vector(self.width, self.height)

    def getCenter(self):
        return Vector(self.x + self.width / 2, self.y + self.height / 2)

    def getIntersection(self, otherObject, retBool, vectorHint):
        overlaps = not (
            self.x < otherObject.x + otherObject.width or
            self.x + self.width > otherObject.x or
            self.y > otherObject.y + otherObject.height or
            self.y + self.height < otherObject.y
        )
        if retBool:
            return overlaps
        if not overlaps:
            return None
        if vectorHint is None or vectorHint == Vector(0, 0):
            vectorHint = Vector(0, -1)
        angle = vectorHint.neg().getAngle()
        """
        clip = Rectangle(max(self.x, otherObject.x), max(self.y, otherObject.y),
                         min(self.x + self.width, otherObject.x + otherObject.width) - self.x,
                         min(self.y + self.height, otherObject.y + otherObject.height) - self.y)
        """
        if 135 < angle <= 225:  # Check left
            return Vector(self.x - (otherObject.width - max(0, self.x - otherObject.x)), otherObject.y), 2
        elif 45 < angle <= 135:  # Check top
            return Vector(otherObject.y, self.y - (otherObject.height - max(0, self.y - otherObject.y))), 1
        elif 225 < angle <= 315:  # Check bottom
            return Vector(otherObject.x, self.y + self.height), 3
        else:  # Check right
            return Vector(self.x + self.width, otherObject.y), 0
