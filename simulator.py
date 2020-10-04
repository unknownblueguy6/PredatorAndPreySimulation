import pygame, sys
from pygame.locals import *

WIDTH  = 400 
HEIGHT = 400

class Simulator:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        self.predators = []
        self.prey = []
        self.food = []
        pygame.display.set_caption('SIMULATOR')

    def drawModels(self):
        for p in predators:
            p.draw(self.surface)
        for p in prey:
            p.draw(self.surface)
        for p in food:
            p.draw(self.surface)

    def update(self):
        pygame.display.update()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.kill()
            
            # add keys for config settings here
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.kill()

    def kill(self):
        pygame.quit()
        sys.exit()


sim = Simulator()

while True:
    sim.checkEvents()
    # sim.drawModels()
    sim.update()