from engine.vector import *
from sdl2 import *


class Level:
    def __init__(self):
        self.tickEvents = []
        self.guiDrawEvents = []
        self.background = None
        self.foreground = None
        self.bgSpeed = 1
        self.drag = 1
        self.gravity = Vector(0, 1)
        self.colliders = []
        self.entities = []
        self.view = None

    def addTickEvent(self, callback):
        self.tickEvents.append(callback)

    def addGuiDrawEvent(self, callback):
        self.tickEvents.append(callback)

    def setBackground(self, image):
        self.background = image

    def setForeground(self, image):
        self.foreground = image

    def setBackgroundSpeed(self, speed):
        self.bgSpeed = speed

    def setDrag(self, factor):
        self.drag = factor

    def setGravity(self, vector):
        self.gravity = vector

    def setView(self, view):
        self.view = view

    def regionTest(self, bounds):
        successes = []
        for region in self.entities:
            if bounds.getIntersection(region.getCollider(), True, None):
                successes.append(region)
        return successes

    def aabbRay(self, min, max, origin, normal):
        tx1 = (min.getX() - origin.getX()) / normal.getX()
        tx2 = (max.getX() - origin.getX()) / normal.getX()

        tmin = min(tx1, tx2)
        tmax = max(tx1, tx2)

        ty1 = (min.getY() - normal.getY()) / normal.getY()
        ty2 = (max.getY() - normal.getY()) / normal.getY()

        tmin = max(tmin, min(ty1, ty2))
        tmax = min(tmax, max(ty1, ty2))

        if tmax >= tmin:
            if tmin < 0:
                return abs(tmax)
            else:
                return abs(tmin)
        return None

    def rayCast(self, origin, angle):
        normal = Vector(math.cos(angle * 3.14159265 / 180), math.sin(angle * 3.14159265 / 180))
        closestBound = 2147483647
        entities = []
        distances = []
        for bound in self.colliders:
            min = bound.getPosition()
            max = bound.getPosition + bound.getSize()
            inter = self.aabbRay(min, max, origin, normal)
            if inter is not None:
                if inter < closestBound:
                    closestBound = inter
        for entity in self.entities:
            collider = entity.getCollider()
            min = collider.getPosition()
            max = collider.getPosition + collider.getSize()
            inter = self.aabbRay(min, max, origin, normal)
            if inter is not None:
                if inter < closestBound:
                    entities.append(entity)
                    distances.append(distances)
        return [x for _,x in sorted(zip(distances, entities))]

    def tick(self, dTime):
        for event in self.tickEvents:
            event(dTime)
        index = 0
        while index < len(self.entities):
            entity = self.entities[index]
            if not entity.isAlive():
                self.entities.pop(index)
                continue
            entity.setPosition(entity.setPosition() + entity.getVelocity() * dTime)
            entity.setVelocity(entity.getVelocity() * self.drag ** dTime)
            for bounds in self.entities:
                newPos = bounds.getIntersection(entity.getCollider(), True, entity.getVelocity())
                if newPos is not None:
                    entity.setPosition(newPos)
                    center, normal = entity.getCollider().getCenter()
                    if normal == 0 or normal == 2:
                        entity.setVelocity(0, entity.getVelocity().getY())
                    elif normal == 1 or normal == 3:
                        entity.setVelocity(entity.getVelocity().getX(), 0)
                        if normal == 1:
                            entity.isGround = True
            index += 1
        self.view.update()

    def render(self, canvas, renderer):
        center = self.view.getCenter()
        size = self.view.getSize()
        SDL_RenderCopy(renderer, self.background.getTexture(), SDL_Rect(
            int(center.getX() - size.getX() / 2), int(center.getY() - size.getY() / 2),
                       int(size.getX()), int(size.getY())), None)
        SDL_RenderCopy(renderer, self.foreground.getTexture(), SDL_Rect(
            int(center.getX() - size.getX() / 2), int(center.getY() - size.getY() / 2),
                       int(size.getX()), int(size.getY())), None)
        for entity in self.entities:
            flip = SDL_FLIP_NONE
            if entity.getFlipX() and entity.getFlipY():
                flip = SDL_FLIP_HORIZONTAL | SDL_FLIP_VERTICAL
            elif entity.getFlipX():
                flip = SDL_FLIP_VERTICAL
            elif entity.getFlipY():
                flip = SDL_FLIP_HORIZONTAL
            img = entity.getImage()
            SDL_RenderCopyEx(renderer, img.getTexture(), None,
                             SDL_Rect(entity.getPosition().getX() * self.view.getScale(),
                                      entity.getPosition().getY() * self.view.getScale(),
                                      img.getSize().getX() * self.view.getScale()),
                                      img.getSize().getY() * self.view.getScale())
            for child in entity.getChildren():
                flip = SDL_FLIP_NONE
                pos = child.getPosition()
                if entity.getFlipX() and entity.getFlipY() and not child.getFlipX() and not child.getFlipY():
                    flip = SDL_FLIP_HORIZONTAL | SDL_FLIP_VERTICAL
                    pos = Vector(-child.getPosition().getX(), -child.getPosition().getY())
                elif entity.getFlipX() and not child.getFlipX():
                    flip = SDL_FLIP_VERTICAL
                    pos = Vector(child.getPosition().getX(), -child.getPosition().getY())
                elif entity.getFlipY() and not child.getFlipY():
                    flip = SDL_FLIP_HORIZONTAL
                    pos = Vector(-child.getPosition().getX(), child.getPosition().getY())
                childImg = child.getImage()
                SDL_RenderCopyEx(renderer, childImg.getTexture(), None,
                             SDL_Rect((child.getPosition().getX() + entity.getPosition().getX()) * self.view.getScale(),
                                      (child.getPosition().getY() + entity.getPosition().getY()) * self.view.getScale(),
                                      childImg.getSize().getX() * self.view.getScale()),
                                 childImg.getSize().getY() * self.view.getScale())

        for event in self.guiDrawEvents:
            event(canvas)

    def addCollider(self, rectangle):
        self.colliders.append(rectangle)

    def removeCollider(self, rectangle):
        self.colliders.remove(rectangle)

    def addEntity(self, entity):
        self.entities.append(entity)
