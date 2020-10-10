import pygame

COLOR = (0, 255, 0, 100)
SIZE = 5

class Food:
    def __init__(self, position, color, size):
        self.x = position[0]
        self.y = position[1]
        self.color = color
        self.size = size
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.size)