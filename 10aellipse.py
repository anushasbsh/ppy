import pygame
pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.draw.circle(screen, (255,255,255), [95,150], 5, 3)
pygame.draw.circle(screen, (255,255,255), [95,150], 5, 3)
pygame.draw.circle(screen, (255,255,255), [95,150], 5, 3)
pygame.draw.circle(screen, (255,255,255), [95,150], 5, 3)
pygame.draw.circle(screen, (255,255,255), [95,150], 5, 3)
pygame.draw.circle(screen, (255,255,255), [95,150], 5, 3)
pygame.draw.circle(screen, (255,255,255), [95,150], 5, 3)
pygame.draw.circle(screen, (255,255,255), [95,150], 5, 3)
pygame.draw.circle(screen, (255,255,255), [95,150], 5, 3)
pygame.draw.circle(screen, (255,255,255), [95,150], 5, 3)
pygame.draw.circle(screen, (255,255,255), [95,150], 5, 3)
pygame.draw.circle(screen, (255,255,255), [95,150], 5, 3)
pygame.draw.circle(screen, (255,255,255), [95,150], 5, 3)
pygame.draw.circle(screen, (255,255,255), [95,150], 5, 3)
pygame.draw.ellipse(screen, (255,0,0), [100,100,100,70], 70)
pygame.display.flip()
