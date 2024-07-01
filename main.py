from pygame.locals import *
import pygame
from player import player

# --init--
pygame.init()
screen_size = (700, 500)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")

clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()


keyDict = [K_w, K_a, K_s, K_d, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE]
keys = {K_w : False, K_a : False, K_s : False, K_d : False, K_UP : False, K_DOWN : False, K_LEFT : False, K_RIGHT : False, K_SPACE : False}


riba = player(screen, "Images/Riba.png", 100, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard inputs
        if event.type == KEYDOWN:
            if event.key in keyDict:
              keys[event.key] = True


        if event.type == KEYUP:
            if event.key in keyDict:
                keys[event.key] = False

    screen.fill((100,112,230))
     
    # Game Loop
    riba.update(keys)


    # Update
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()
