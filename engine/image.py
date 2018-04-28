from sdl2 import *
from sdl2.sdlimage import *


class Image:
    def __init__(self, renderer, path):
        surface = IMG_Load("res\\" + path)
        self.texture = SDL_CreateTextureFromSurface(renderer, surface)
        SDL_FreeSurface(surface)

    def dispose(self):
        SDL_DestroyTexture(surface)

    def getTexture(self):
        return self.texture