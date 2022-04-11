import pygame
from settings import *

class Note(pygame.sprite.Sprite):
	def __init__(self,pos,group):
		super().__init__(group)

		self.isLast = False
		self.column = pos[0]
		self.posx = 192 + 87 * pos[0]
		self.posy = pos[1]
		self.image = pygame.image.load('images/note.png').convert()
		self.rect = self.image.get_rect(topleft=(self.posx,self.posy))
		self.timer = 0

	def killonkeypress(self):
		keys = pygame.key.get_pressed()
		if not self.isLast:
			return
		if keys[pygame.K_q] and self.column == 0 and self.rect.centery < +75/2 + 616 and self.rect.centery > 541-75/2: self.kill()
		elif keys[pygame.K_w] and self.column == 1 and self.rect.centery < +75/2 + 616 and self.rect.centery > 541-75/2: self.kill()
		elif keys[pygame.K_e] and self.column == 2 and self.rect.centery < +75/2 + 616 and self.rect.centery > 541-75/2: self.kill()
		elif keys[pygame.K_r] and self.column == 3 and self.rect.centery < +75/2 + 616 and self.rect.centery > 541-75/2: self.kill()
		else: pass #fix later to delete only bottom note

	def update(self):
		self.rect.y += 5
		self.timer += 1/FPS
		if self.rect.bottom > 720:
			self.kill()
		self.killonkeypress()
