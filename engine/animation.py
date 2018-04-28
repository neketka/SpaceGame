import time


class Animation:
    def __init__(self, framesList, length):
        self.running = False
        self.time = 0
        self.framesList = framesList
        self.lastFrame = 0
        self.length = length

    def play(self):
        self.time = time.clock()
        self.running = True

    def stop(self):
        self.lastFrame = 0
        self.running = False

    def getCurrentFrame(self):
        if not self.running:
            return self.framesList[self.lastFrame]
        return self.framesList[int/(time.clock() - self.time) % self.length / self.length * self.framesList]
