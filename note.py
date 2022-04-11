import pygame

class Note(pygame.sprite.Sprite):
	def __init__(self,pos,group):
		super().__init__(group)

		self.pos = (192 + 87 * pos[0], pos[1])
		self.image = pygame.image.load('images/note.png').convert()
		self.rect = self.image.get_rect(topleft=self.pos)
		self.duration = 60

	def update(self):
		self.rect.y += 5
		self.duration -= 1
		if self.duration == 0 or self.rect.bottom > 616:
			self.kill()
