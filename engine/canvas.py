from engine.vector import *
from sdl2 import *
from sdl2.sdlttf import *


class Canvas:
    def __init__(self, renderer, width, height):
        self.renderer = renderer
        self.size = Vector(width, height)

    def drawImage(self, image, rectangle):
        SDL_RenderCopy()

    def drawRect(self, color, rectangle):
        pass

    def drawText(self, x, y, fontSize, color):
        pass

    def getSize(self):
        return self.size