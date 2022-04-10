import pygame
from receptor import Receptor

class Level:
    def __init__(self, lvl_num):
        self.stage_num = lvl_num
        self.surface = pygame.display.get_surface()
        self.receptorgroup = pygame.sprite.Group()

        receptorposlist = [(192,541),(279,541),(366,541),(453,541)]

        for pos in receptorposlist:
            Receptor(pos,self.receptorgroup)


    def load(self):
        x = 4

    def run(self):
        self.receptorgroup.draw(self.surface)

#TODO make a basic level class
