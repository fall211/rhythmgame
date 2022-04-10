import pygame

class Receptor(pygame.sprite.Sprite):
	def __init__(self,pos,group):
		super().__init__(group) # we need this, not quite sure why but it's here

		self.pos = pos
		self.image = pygame.image.load('images/receptor.png').convert()
		self.rect = self.image.get_rect(topleft=self.pos) #rectangle is for positioning the sprite and also later for collisions
