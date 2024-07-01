import pygame
class player:
	def __init__(self, screen, img, x, y):
		self.screen = screen
		self.img = pygame.image.load(img)
		self.x = x
		self.y = y


	def draw(self):
		self.screen.blit(self.img, (self.x, self.y))