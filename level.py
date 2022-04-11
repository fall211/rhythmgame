import pygame
from receptor import Receptor
from note import Note

class Level:
    def __init__(self, lvl_num):
        self.stage_clock = pygame.time.Clock()
        self.stage_clock.tick()
        self.te = 0

        self.stage_num = lvl_num
        self.surface = pygame.display.get_surface() #gets the surface so that we can draw on it
        self.receptorgroup = pygame.sprite.Group() #sprite group for the receptors
        self.notegroup = pygame.sprite.Group() #sprite group for the notes

        self.background = pygame.image.load("images/background.png")

        receptorposlist = [(192,541),(279,541),(366,541),(453,541)] #just a list with positions
        self.notearr = [(100, (0, 341)), (200, (0, 341))]
        self.notePosition = 0;

        for pos in receptorposlist:
            Receptor(pos,self.receptorgroup) #creates instances of the receptor class and adds them to its sprite group

    def run(self): #this is the thing that gets ran every time the screen updates, so this will be used to draw all the shit
        while(self.notePosition < len(self.notearr) and self.notearr[self.notePosition][0] - self.te < 0.03):
            Note(self.notearr[self.notePosition][1], self.notegroup)
            self.notePosition += 1
        
        print(self.te)

        self.stage_clock.tick()
        self.surface.blit(self.background, (0, 0))
        self.receptorgroup.draw(self.surface)
        self.notegroup.draw(self.surface)
        self.notegroup.update()

        self.te += self.stage_clock.tick()

#TODO make a basic level class
