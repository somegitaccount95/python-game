import pygame

class platform:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.imgLoad = pygame.image.load("Images/platform.png")
        self.img = pygame.transform.scale(self.imgLoad, (self.screen.get_width(), self.imgLoad.get_height()))
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = x
        self.y = y

    def getRect(self):
        return self.img.get_rect()

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))

    def update(self):
        self.draw()