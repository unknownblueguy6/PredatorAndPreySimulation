import pygame

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
    def details(self, name):
        if(self.alive):
            print(f"The {name}'s max health is {self.maxHealth}")
            print(f"The {name}'s field of view is from ({self.x},{self.y}) to a radius of {self.fieldRadius}")
            print(f"The {name}'s max velocity is {self.maxVelocity}")