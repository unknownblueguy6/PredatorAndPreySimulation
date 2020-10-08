import pygame

FOOD_COLOR = (0, 0, 255, 100)
FOOD_SIZE = 10

class Food:
    def __init__(self, position, color, size):
        self.x = position[0]
        self.y = position[1]
        self.color = color
        self.size = size
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.size)