from pygame.locals import *
import pygame

class player:
	def __init__(self, screen, img, x, y):
		self.screen = screen
		self.img = pygame.image.load(img)
		self.x = x
		self.y = y
		self.xvel = 0
		self.yvel = 0
		self.drag = 0.98
		self.speed = 2
		self.jump = False


	def draw(self):
		self.screen.blit(self.img, (self.x, self.y))


	def update(self, keys):
		self.draw()

		# Movement
		if keys[K_a] == True or keys[K_LEFT] == True:
			self.xvel = -5
		if keys[K_d] == True or keys[K_RIGHT] == True:
			self.xvel = 5
		if keys[K_SPACE] == True:
			self.jump = True
		if self.jump:
			self.yvel += -7
			jump = False
			
		# Apply forces
		self.x += self.xvel
		self.y += self.yvel

		self.xvel *= self.drag
		self.yvel *= self.drag


		# print("xvel: " + str(self.xvel), "yvel: " + str(self.yvel))
