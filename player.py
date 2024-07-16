from pygame.locals import *
import pygame

class player:
	def __init__(self, screen, img, x, y):
		self.screen = screen
		self.img = pygame.image.load(img).convert_alpha()
		self.width = self.img.get_width()
		self.height = self.img.get_height()
		self.x = x
		self.y = y
		self.xvel = 0
		self.yvel = 0
		self.drag = 0.98
		self.speed = 2
		self.gravity = 0.90
		self.jump = False

	def getSurface(self):
		return self.img

	def getRect(self):
		return pygame.Rect(self.x, self.y, self.width, self.height)

	def draw(self):
		self.screen.blit(self.img, (self.x, self.y))

	def collisionCheck(self, collisionObjects):
		for collisionObject in collisionObjects:
			print(collisionObject.y, self.y)
			if self.getRect().colliderect(collisionObject.getRect()):
				self.mask = pygame.mask.from_surface(self.getSurface())
				if self.mask.overlap(collisionObject.getMask(), (self.x - collisionObject.x, self.y - collisionObject.y)):
					self.mask.to_surface(self.screen, None, None, "white", None, (self.x, self.y))
					return True
		return False

		
		# Draw Mask: mask.to_surface(self.screen, None, None, "white", None, (self.x, self.y))


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
		if not self.collisionCheck(collisionObjects):
			self.yvel += self.gravity
		else:
			print("colliding")

		self.xvel *= self.drag
		self.yvel *= self.drag
		
		self.yvel = round(self.yvel)

		self.x += self.xvel
		self.y += self.yvel


		# print("xvel: " + str(self.xvel), "yvel: " + str(self.yvel))
