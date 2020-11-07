import pygame, sys
import predator
import prey
import food
import random
import constants
from pygame.locals import *

WIDTH  = constants.WIDTH
HEIGHT = constants.HEIGHT
MAX_FOOD_SUPPLY = constants.MAX_FOOD_SUPPLY
INIT_VELOCITY = constants.INIT_VELOCITY
FPS = constants.FPS
CHANCE_OF_ESCAPE = constants.CHANCE_OF_ESCAPE
initialPredatorPopulation = constants.initialPredatorPopulation
initialPreyPopulation = constants.initialPreyPopulation

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
                    (random.uniform(-1, 1) * INIT_VELOCITY, random.uniform(-1, 1) * INIT_VELOCITY),
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
                    (random.uniform(-1, 1) * INIT_VELOCITY, random.uniform(-1, 1) * INIT_VELOCITY),
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

    def moveModels(self):
        self.surface.fill((0, 0, 0))
        for i in range(len(self.predators)):
            self.predators[i].move(WIDTH, HEIGHT, self.prey)
        for i in range(len(self.prey)):
            self.prey[i].move(WIDTH, HEIGHT, self.predators, self.food)

    def update(self):
        pygame.display.update()
        self.clock.tick(FPS)

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.kill()
            
            # add keys for config settings here
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.kill()

    def preyHunt(self):
        for j in range(len(self.prey)):
            p = self.prey[j]
            for i in range(len(self.food)-1, -1, -1):
                foodRect = pygame.Rect(0, 0, 2*self.food[i].size, 2*self.food[i].size)
                foodRect.centerx = self.food[i].x
                foodRect.centery = self.food[i].y
                if p.rect.colliderect(foodRect):
                    del self.food[i]
                    self.prey[j].health += prey.HEALTH_GAIN
                    self.prey[j].health = min(self.prey[j].health, self.prey[j].maxHealth)
    
    def predatorHunt(self):
        for j in range(len(self.predators)):
            p = self.predators[j]
            for i in range(len(self.prey)-1, -1, -1):
                if p.rect.colliderect(self.prey[i].rect):
                    chance = random.random()
                    if chance > CHANCE_OF_ESCAPE:
                        self.prey[i].dead()
                        del self.prey[i]
                        self.predators[j].health += predator.HEALTH_GAIN
                        self.predators[j].health = min(self.predators[j].health, self.predators[j].maxHealth)
                    else:
                        self.prey[i].health -= prey.HEALTH_LOSS / 2
                        self.predators[j].health += predator.HEALTH_GAIN / 2
                        self.predators[j].health = min(self.predators[j].health, self.predators[j].maxHealth)

    
    def decreaseHealth(self):
        for i in range(len(self.predators)):
            self.predators[i].health -= predator.HEALTH_LOSS
            if self.predators[i].health <= 0:
                self.predators[i].dead()
        for i in range(len(self.prey)):
            self.prey[i].health -= prey.HEALTH_LOSS
            if self.prey[i].health <= 0:
                self.prey[i].dead()
    
    def removeDead(self):
        for i in range(len(self.predators)-1, -1, -1):
            if (self.predators[i].alive == False):
                del self.predators[i]
        for i in range(len(self.prey)-1, -1, -1):
            if (self.prey[i].alive == False):
                del self.prey[i]

    def addFood(self):
        while len(self.food) < MAX_FOOD_SUPPLY:
            f = food.Food(
                (random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                food.COLOR,
                food.SIZE
            )
            self.food.append(f)

    def kill(self):
        pygame.quit()
        sys.exit()

sim = Simulator(initialPredatorPopulation, initialPreyPopulation)

while True:
    sim.checkEvents()
    sim.removeDead()
    sim.addFood()
    sim.moveModels()
    sim.drawModels()
    sim.preyHunt()
    sim.predatorHunt()
    sim.decreaseHealth()
    sim.update()