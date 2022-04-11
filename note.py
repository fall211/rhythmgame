import pygame

class Note(pygame.sprite.Sprite):
	def __init__(self,pos,group):
		super().__init__(group)

		self.pos = pos
		self.image = pygame.image.load('images/note.png').convert()
		self.rect = self.image.get_rect(topleft=self.pos)
		self.duration = 300

	def update(self):
		self.rect.y += 5
		self.duration -= 1
