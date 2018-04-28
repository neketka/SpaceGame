from engine.vector import *
from sdl2 import *
from sdl2.sdlttf import *


class Canvas:
    def __init__(self, renderer, width, height):
        self.renderer = renderer
        self.size = Vector(width, height)

    def drawImage(self, image, rectangle):
        SDL_RenderCopy(self.renderer, image.getTexture(), None,
                       SDL_Rect(int(rectangle.getPosition().getX()),
                                int(rectangle.getPosition().getY()),
                                int(rectangle.getSize().getX()),
                                int(rectangle.getSize().getY())))

    def drawRect(self, color, rectangle):
        pass

    def drawText(self, x, y, fontSize, color):
        pass

    def getSize(self):
        return self.size