import pygame

# maxHealth    =>  integer for health (Out of 100)
# fieldRadius  => integer for field of view
# maxVelocity  => integer value of max Velocity
# position     => a tuple of integers for initial 2D coordinate system
# velocity     => current velocity
# color        => color code
# size         => size of creature

class Creature:
    def __init__(self,maxHealth,fieldRadius, maxVelocity, position, velocity, color, size):    
        self.color = color
        self.size = size
        self.rect = pygame.Rect((position[0], position[1]), (size, size))
        self.maxHealth = maxHealth
        self.fieldRadius = fieldRadius
        self.maxVelocity = maxVelocity
        self.velocity = pygame.math.Vector2(velocity)
        self.alive = True
    def dead(self):
        self.alive = False
    def move(self, width, height):
        self.rect.move_ip(self.velocity[0], self.velocity[1])
        if (self.rect.x <= 0 or self.rect.x >= width):
            self.velocity.update(-self.velocity[0], self.velocity[1])
        if (self.rect.y <= 0 or self.rect.y >= height):
            self.velocity.update(self.velocity[0], -self.velocity[1])
    def changeDirection(self, newDirectionVec):
        OldMagnitude = self.velocity[0]**2 + self.velocity[1]**2
        NewMagnitude = newDirectionVec[0]**2 + newDirectionVec[1]**2
        if NewMagnitude == 0:
            pass
        else:
            factor = OldMagnitude/NewMagnitude
            self.velocity.update(factor*newDirectionVec[0], factor*newDirectionVec[1])
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