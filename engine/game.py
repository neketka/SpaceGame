from sdl2 import *
import ctypes
import time
from engine.vector import *
from engine.image import *
from engine.canvas import *


class Game:
    def __init__(self, title):
        self.window = SDL_CreateWindow(title, 100, 100, 640, 480, SDL_WINDOW_SHOWN)
        self.renderer = SDL_CreateRenderer(self.window, -1, 0)
        self.keys = [True for x in range(0, 500)]
        self.mouseButtons = [True for x in range(0, 12)]
        self.level = None
        self.assets = {}
        self.timedEvents = []
        self.mousePos = Vector(0, 0)
        self.size = Vector(640, 480)
        self.canvas = Canvas(self.renderer, int(self.size.getX()), int(self.size.getY()))

    def run(self):
        running = True
        curTime = self.getTime()
        index = 0
        event = SDL_Event()
        while running:
            while SDL_PollEvent(ctypes.byref(event)) != 0:
                if event.type == SDL_QUIT:
                    running = False
                elif event.type == SDL_KEYDOWN:
                    self.keys[event.key.keysym.scancode] = True
                elif event.type == SDL_KEYUP:
                    self.keys[event.key.keysym.scancode] = False
                elif event.type == SDL_MOUSEMOTION:
                    self.mousePos = Vector(event.motion.x - self.size.getX() / 2,
                                           event.motion.y - self.size.getY() / 2)
                elif event.type == SDL_WINDOWEVENT:
                    if event.window.event == SDL_WINDOWEVENT_RESIZED:
                        self.size = Vector(event.window.data1, event.window.data2)
                elif event.type == SDL_MOUSEBUTTONDOWN:
                    self.mouseButtons[event.button.button] = True
                elif event.type == SDL_MOUSEBUTTONUP:
                    self.mouseButtons[event.button.button] = False
            while index < len(self.timedEvents):
                event = self.timedEvents[index]
                if event[0] <= self.getTime():
                    event[1]()
                    self.timedEvents.pop(index)
                    continue
                index += 1
            if self.level is not None:
                self.level.tick(self.getTime() - curTime)
            SDL_RenderClear(self.renderer)
            if self.level is not None:
                self.level.render(self.renderer, self.canvas)
            SDL_RenderPresent(self.renderer)
            curTime = self.getTime()
        for asset in self.assets:
            asset.dispose()
        SDL_DestroyRenderer(self.renderer)
        SDL_DestroyWindow(self.window)

    def setLevel(self, level):
        self.level = level

    def getLevel(self):
        return self.level

    def getAsset(self, name):
        if name not in self.assets:
            self.assets[name] = Image(self.renderer, name)
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
