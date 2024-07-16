import pygame

class platform:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.imgLoad = pygame.image.load("Images/platform.png").convert()
        self.img = pygame.transform.scale(self.imgLoad, (self.screen.get_width(), self.imgLoad.get_height()))
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = x
        self.y = y

    def getSurface(self):
        return self.img

    def getMask(self):
        return pygame.mask.from_surface(self.getSurface())

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))

    def update(self):
        self.draw()