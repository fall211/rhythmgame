import pygame

class Note(pygame.sprite.Sprite):
	def __init__(self,pos,group):
		super().__init__(group)

		self.pos = pos
		self.image = pygame.image.load('images/note.png').convert()
		self.rect = self.image.get_rect(topleft=self.pos)

	def update(self):
		self.rect.y += 1
