import pygame, sys
from pygame.locals import *

WIDTH  = 400 
HEIGHT = 400

PREY_SIZE = 20
PREDATOR_SIZE = 20
PREY_COLOR = (0, 0, 255, 100)
PREDATOR_COLOR = (255, 0, 0, 100)

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

class Creature:
    def __init__(self,maxHealth,fieldRadius,maxVelocity,position, color, size):
        self.x = position[0]
        self.y = position[1]
        self.color = color
        self.rect = pygame.Rect((self.x, self.y), (size, size))
        self.maxHealth = maxHealth
        self.fieldRadius = fieldRadius
        self.maxVelocity = maxVelocity
        self.alive = True
    def dead(self):
        self.alive = False
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
    def showFieldofView(self):
        pass
        #drawing the field of view circle
        #pygame.draw.circle(surface,(255,255,255),(self.x,self.y),self.fieldRadius)
    def details(self):
        if(self.alive):
            print(f"The Creatures max health is {self.maxHealth}")
            print(f"The Creatures field of view is from ({self.x},{self.y}) to a radius of {self.fieldRadius}")
            print(f"The Creatures max velocity is {self.maxVelocity}")
        else:
            print("The Creature is dead. Sorry :(")

class Predator(Creature):
    def __init__(self,creatureFields,detection,attraction):
        super(Predator,self).__init__(self,creatureFields)
        self.detectionOfPrey = detection
        self.attractionOfPrey = attraction
    def details(self):
        if(self.alive):
            print(f"The Creatures max health is {self.maxHealth}")
            print(f"The Creatures field of view is from ({self.x},{self.y}) to a radius of {self.fieldRadius}")
            print(f"The Creatures max velocity is {self.maxVelocity}")
            print(f"The Predator's detection capability is {self.detectionOfPrey}")
            print(f"The Predator's attraction capability is {self.attractionOfPrey}")
        else:
            print("The Creature is dead. Sorry :(")

class Prey(Creature):
    def __init__(self,creatureFields,detectionOfFood,attractionToFood,detectionOfPredator,repulsionToPredator):
        super(Prey,self).__init__(self,creatureFields)
        self.detectionOfFood = detectionOfFood
        self.attractionToFood = attractionToFood
        self.detectionOfPredator = detectionOfPredator
        self.repulsionToPredator = repulsionToPredator
    def details(self):
        if(self.alive):
            print(f"The Creatures max health is {self.maxHealth}")
            print(f"The Creatures field of view is from ({self.x},{self.y}) to a radius of {self.fieldRadius}")
            print(f"The Creatures max velocity is {self.maxVelocity}")
            print(f"The Prey's detection of Food capability is {self.detectionOfFood}")
            print(f"The Prey's attraction to Food capability is {self.attractionToFood}")
            print(f"The Prey's detection of Predator capability is {self.detectionOfPredator}")
            print(f"The Prey's repulsion to Predator capability is {self.repulsionToPredator}")
        else:
            print("The Creature is dead. Sorry :(")

sim = Simulator()

while True:
    sim.checkEvents()
    # sim.drawModels()
    sim.update()