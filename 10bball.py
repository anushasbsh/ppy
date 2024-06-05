import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,400))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.draw.circle(screen, (255,255,255), [95,150], 10,0)
pygame.display.update()
pygame.draw.circle(screen, (0,0,0), [95,150], 10,0)
pygame.display.update()
pygame.draw.circle(screen, (255,255,255), [105,160], 10,0)
pygame.display.update()
pygame.draw.circle(screen, (0,0,0), [105,160], 10,0)
pygame.display.update()
pygame.draw.circle(screen, (255,255,255), [125,180], 10,0)
pygame.display.update()
pygame.draw.circle(screen, (0,0,0), [125,180], 10,0)
pygame.display.update()
pygame.draw.circle(screen, (255,255,255), [155,210], 10,0)
pygame.display.update()
pygame.display.update()
for event in pygame.event.get():
    if event.type == quit:
        pygame.quit()
        sys.exit()