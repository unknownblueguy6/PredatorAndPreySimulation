import pygame

WIDTH = HEIGHT = 400

pygame.init()
mainClock = pygame.time.clock()
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('SIMULATOR')


while 1:
    pygame.draw.rect(windowSurface, (255, 0, 0), pygame.Rect(10, 20, 30, 40))
    pygame.display.update()