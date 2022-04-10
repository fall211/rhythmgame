import pygame
from receptor import Receptor

class Level:
    def __init__(self, lvl_num):
        self.stage_num = lvl_num
        self.surface = pygame.display.get_surface() #gets the surface so that we can draw on it
        self.receptorgroup = pygame.sprite.Group() #sprite group for the receptors

        receptorposlist = [(192,541),(279,541),(366,541),(453,541)] #just a list with positions

        for pos in receptorposlist:
            Receptor(pos,self.receptorgroup) #creates instances of the receptor class and adds them to its sprite group


    def load(self):
        x = 4

    def run(self): #this is the thing that gets ran every time the screen updates, so this will be used to draw all the shit
        self.receptorgroup.draw(self.surface)

#TODO make a basic level class
