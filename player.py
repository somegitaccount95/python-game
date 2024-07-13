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
		self.gravity = 0.90
		self.jump = False

	def getSurface(self):
		return pygame.surface(self.img, (self.x, self.y))

	def getRect(self):
		return self.img.get_rect()

	def draw(self):
		self.screen.blit(self.img, (self.x, self.y))

	def collisionCheck(self, collisionObjects):
		for object in collisionObjects:
			if object.getRect().colliderect(self.getRect()):
				return True
		return False


	def update(self, keys, collisionObjects):
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
		self.xvel *= self.drag
		self.yvel *= self.drag

		if self.collisionCheck(collisionObjects) == False:
			self.yvel *= self.gravity
		
		self.x += self.xvel
		self.y += self.yvel


		# print("xvel: " + str(self.xvel), "yvel: " + str(self.yvel))
