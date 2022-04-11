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
        self.background = pygame.image.load("images/background.png")

        self.receptorgroup = pygame.sprite.Group() #sprite group for the receptors
        self.notegroup = pygame.sprite.Group() #sprite group for the notes


        receptorposlist = [(192,541),(279,541),(366,541),(453,541)] #just a list with positions
        self.noteArr = [(1000, (0, 341)), (2000, (0, 341))]
        self.inNoteArr = [[],[],[],[]];
        self.notePosition = 0;

        for pos in receptorposlist:
            Receptor(pos,self.receptorgroup) #creates instances of the receptor class and adds them to its sprite group

    def run(self): #this is the thing that gets ran every time the screen updates, so this will be used to draw all the shit

        # adds the delta time, and then checks if the upcoming notes are within the interval
        self.te += self.stage_clock.tick() 

        # while loop is there to ensure doubles are accounted for (instead of just popping the first)
        # "15" here is hardcoded due to the framerate. TODO change this for variable framerate/60 FPS

        while(self.notePosition < len(self.noteArr) and self.noteArr[self.notePosition][0] - self.te < 15):
            (self.inNoteArr[self.noteArr[self.notePosition][1][0]]).append(Note(self.noteArr[self.notePosition][1], self.notegroup,0.1))
            print(len(self.inNoteArr[self.noteArr[self.notePosition][1][0]]))
            self.notePosition += 1
        
        for arr in self.inNoteArr:
            if len(arr) == 0:
                continue
            while len(arr) != 0 and not arr[0].alive():
                arr.pop(0)
            if len(arr) != 0:
                arr[0].isLast = True

                
        
        self.surface.blit(self.background, (0, 0))
        self.receptorgroup.draw(self.surface)
        self.notegroup.draw(self.surface)
        self.notegroup.update()


