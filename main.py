import pygame

# --init--
pygame.init()
screen_size = (700, 500)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")

clock = pygame.time.Clock()

right = false
left = false
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type = KEYDOWN
            if event.key = K_RIGHT
                right = true
            if event.key = K_LEFT
                left = true
        if event.type = KEYUP
            if event.key = K_RIGHT
                right = false
            if event.key = K_LEFT
                left = false
    
    screen.fill((0,0,0))
     
    # Game Loop
  

    # Update
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()
