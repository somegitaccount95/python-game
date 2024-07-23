import pygame
class image:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
    
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))
