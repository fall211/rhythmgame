import pygame
from sys import exit
from level import Level
from settings import *

class Game:
    def __init__(self):
        pygame.init() #initialize pygame
        screen = pygame.display.set_mode((WIDTH, HEIGHT)) #set screen dimensions
        pygame.display.set_caption('RhythmGame') #set window title

        pygame.mixer.init()
        pygame.mixer.music.load('./audio/drip.wav')
        # pygame.mixer.music.play(1)

        self.clock = pygame.time.Clock()

        self.level = Level(1)

    def run(self):
        while True: #everything happens in this loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #closing the window exits the program
                    pygame.quit() #close pygame
                    exit() #exit the program
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: self.level.notedeath('q')
                    elif event.key == pygame.K_w: self.level.notedeath('w')
                    elif event.key == pygame.K_e: self.level.notedeath('e')
                    elif event.key == pygame.K_r: self.level.notedeath('r')
                    else: pass

            self.level.run()

            pygame.display.update() #update the screen when While True is
            self.clock.tick(FPS) #how many times per second the screen gets updated

