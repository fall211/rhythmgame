import pygame
from settings import *

class Note(pygame.sprite.Sprite):
	def __init__(self,pos,group,speed):
		super().__init__(group)

		self.isLast = False
		self.column = pos[0]
		self.posx = 192 + 87 * pos[0]
		self.posy = pos[1]
		self.image = pygame.image.load('images/note.png').convert()
		self.rect = self.image.get_rect(topleft=(self.posx,self.posy))
		self.speed = speed


	def update(self):
		self.rect.y += 1 * self.speed
		if self.rect.bottom > 720:
			self.kill()
