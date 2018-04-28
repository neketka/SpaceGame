from sdl2 import *
import ctypes
import time
from engine.vector import *


class Game:
    def __init__(self, title):
        window = SDL_CreateWindow(title, 100, 100, 640, 480, SDL_WINDOW_SHOWN)
        self.renderer = SDL_CreateRenderer(window, -1, 0)
        self.keys = [True for x in range(0, 256)]
        self.mouseButtons = [True for x in range(0, 8)]
        self.level = None
        self.assets = {}
        self.timedEvents = []
        self.mousePos = Vector(0, 0)

    def run(self):
        running = True
        event = SDL_Event()
        while running:
            while SDL_PollEvent(ctypes.byref(event)) != 0:
                if event.type == SDL_QUIT:
                    running = False
        curTime = self.getTime()
        index = 0
        while index < len(self.timedEvents):
            event = self.timedEvents[index]
            if event[0] <= curTime:
                event[1]()
                self.timedEvents.pop(index)
                continue
            index += 1

        SDL_RenderClear(self.renderer)

        SDL_RenderPresent(self.renderer)

    def setLevel(self, level):
        self.level = level

    def getLevel(self):
        return self.level

    def getAsset(self, name):
        return self.assets[name]

    def getTime(self):
        return time.clock()

    def addTimedEvent(self, timeFromNow, callback):
        self.timedEvents.append([self.getTime() + timeFromNow, callback])

    def isKeyDown(self, key):
        return self.keys[key]

    def isMouseDown(self, mouseButton):
        return self.mouseButtons[mouseButton]

    def getMousePos(self):
        return self.mousePos