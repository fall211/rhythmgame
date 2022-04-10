import pygame
from sys import exit


#https://www.pygame.org/docs/   <---- quick access to documentation

WIDTH = 720
HEIGHT = 720
FPS = 30

class Game:
    def __init__(self):
        pygame.init() #initialize pygame
        screen = pygame.display.set_mode((WIDTH, HEIGHT)) #set screen dimensions
        pygame.display.set_caption('RhythmGame') #set window title
        self.clock = pygame.time.Clock()


    def run(self):
        while True: #everything happens in this loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #closing the window exits the program
                    pygame.quit() #close pygame
                    exit() #exit the program
                if pygame.key.get_pressed()[pygame.K_BACKSPACE]: #pressing backspace exits the program
                    pygame.quit()
                    exit()


            pygame.display.update() #update the screen when While True is
            self.clock.tick(FPS) #how many times per second the screen gets updated



if __name__ == '__main__': #shows that this is the only .py file that should be ran in console
	Game().run()
