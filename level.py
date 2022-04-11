import pygame
from receptor import Receptor
from note import Note

class Level:
    def __init__(self, lvl_num):
        self.stage_num = lvl_num
        self.surface = pygame.display.get_surface() #gets the surface so that we can draw on it
        self.receptorgroup = pygame.sprite.Group() #sprite group for the receptors
        self.notegroup = pygame.sprite.Group() #sprite group for the notes

        self.background = pygame.image.load("images/background.png")

        receptorposlist = [(192,541),(279,541),(366,541),(453,541)] #just a list with positions
        notearr = [(192, 341)]

        for pos in receptorposlist:
            Receptor(pos,self.receptorgroup) #creates instances of the receptor class and adds them to its sprite group
        for pos in notearr:
            Note(pos, self.notegroup)

    def run(self): #this is the thing that gets ran every time the screen updates, so this will be used to draw all the shit
        self.surface.blit(self.background, (0, 0))
        self.receptorgroup.draw(self.surface)
        self.notegroup.draw(self.surface)
        self.notegroup.update()

#TODO make a basic level class
