from engine.vector import *
from sdl2 import *
import ctypes
from sdl2.sdlttf import *


class Canvas:
    def __init__(self, renderer, width, height):
        self.renderer = renderer
        self.size = Vector(width, height)
        self.font = TTF_OpenFont("sans.ttf", 16)

    def drawImage(self, image, rectangle):
        SDL_RenderCopy(self.renderer, image.getTexture(), None,
                       SDL_Rect(int(rectangle.getPosition().getX()),
                                int(rectangle.getPosition().getY()),
                                int(rectangle.getSize().getX()),
                                int(rectangle.getSize().getY())))

    def drawRect(self, color, rectangle):
        SDL_SetRenderDrawColor(self.renderer, int(color.getR() * 255), int(color.getG() * 255), int(color.getB() * 255),
                               int(color.getA()))
        SDL_RenderDrawRect(self.renderer, ctypes.byref(rectangle))

    def drawText(self, x, y, color, text):
        SDL_SetRenderDrawColor(self.renderer, int(color.getR() * 255), int(color.getG() * 255), int(color.getB() * 255),
                               int(color.getA()))
        surface = TTF_RenderText_Solid(self.font, text, SDL_Color(int(color.getR() * 255),
                                                        int(color.getG() * 255), int(color.getB() * 255)))
        texture = SDL_CreateTextureFromSurface(self.renderer, surface)

        SDL_RenderCopy(self.renderer, texture, None, SDL_Rect(int(x),
                                int(y),
                                int(surface.contents.width),
                                int(surface.contents.height)))
        SDL_FreeSurface(surface)
        SDL_DestroyTexture(texture)


    def getSize(self):
        return self.size