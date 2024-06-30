import pygame

# --init--
pygame.init()
screen_size = (700, 500)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")

speed = 5
jump = 5

clock = pygame.time.Clock()
 
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    
    screen.fill((0,0,0))
     
    # Game Loop
  

    # Update
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()

