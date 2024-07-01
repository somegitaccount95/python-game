import pygame

# --init--
pygame.init()
screen_size = (700, 500)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")

clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

right = False
left = False

riba = pygame.image.load("riba.png")
location = [100, 100]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                right = True
            if event.key == K_LEFT:
                left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                right = False
            if event.key == K_LEFT:
                left = False
    
    screen.fill((100,112,230))
     
    # Game Loop

    screen.blit(riba, location)
    if right:
        location[0] += 5
    if left:
        location[0] -= 5

    # Update
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()
