import pygame, sys
import predator
import prey
import food
import random
from pygame.locals import *

WIDTH  = 900 
HEIGHT = 900
MAX_FOOD_SUPPLY = 200

class Simulator:
    def __init__(self, initialPredatorPopulation, initialPreyPopulation):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        self.predators = []
        self.prey = []
        self.food = []
        for i in range(initialPredatorPopulation):
            p = predator.Predator(
                (
                    predator.MAX_HEALTH, 
                    predator.VIEW_RADIUS,
                    predator.MAX_VELOCITY,
                    (random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                    predator.COLOR,
                    predator.SIZE,
                ),
                predator.MAX_DETECTION_OF_PREY  * random.uniform(-1, 1),
                predator.MAX_ATTRACTION_TO_PREY * random.uniform(-1, 1),    
            )
            self.predators.append(p)

        for i in range(initialPreyPopulation):
            p = prey.Prey(
                (
                    prey.MAX_HEALTH, 
                    prey.VIEW_RADIUS,
                    prey.MAX_VELOCITY,
                    (random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                    prey.COLOR,
                    prey.SIZE,
                ),
                prey.MAX_DETECTION_OF_FOOD       * random.uniform(-1, 1),
                prey.MAX_ATTRACTION_TO_FOOD      * random.uniform(-1, 1),
                prey.MAX_DETECTION_OF_PREDATOR   * random.uniform(-1, 1),
                prey.MAX_REPULSION_FROM_PREDATOR * random.uniform(-1, 1),
            )
            self.prey.append(p)

        for i in range(MAX_FOOD_SUPPLY):
            f = food.Food(
                (random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                food.COLOR,
                food.SIZE
            )
            self.food.append(f)
        
        pygame.display.set_caption('SIMULATOR')

    def drawModels(self):
        for p in self.predators:
            p.draw(self.surface)
        for p in self.prey:
            p.draw(self.surface)
        for p in self.food:
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

sim = Simulator(50, 50)

while True:
    sim.checkEvents()
    sim.drawModels()
    sim.update()