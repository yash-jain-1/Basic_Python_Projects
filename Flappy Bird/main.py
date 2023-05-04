import random 
# random length for pipes
import sys
import pygame
from pygame.locals import *

FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT  = 551
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT)) # initializing a window for display
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'Flappy Bird Assets/Player/bird1.png'
BACKGROUND = 'Flappy Bird Assets/Background/Background3.png'
PIPE = 'Flappy Bird Assets/pipe.png'

GAME_SPRITES['message'] = pygame.image.load('Flappy Bird Assets/demo-img-3.png').convert_alpha()
GAME_SPRITES['base'] = pygame.image.load('Flappy Bird Assets/Background/Background4.png').convert_alpha()
GAME_SPRITES['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
        pygame.image.load(PIPE).convert_alpha(),
    )
#game sounds
# GAME_SOUNDS['die'] = pygame.mixer.Sound('Flappy Bird Assets/Sounds/Straw Squeak.mp3')
# GAME_SOUNDS['hit'] = pygame.mixer.Sound('')
# GAME_SOUNDS['point'] = pygame.mixer.Sound('')
# GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('')
# GAME_SOUNDS['wing'] = pygame.mixer.Sound('')

GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert_alpha()
GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()


def WelcomeScreen():
    # We will put welcome image here
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0

    while True:
        for event in pygame.event.get():
            # if user clicks on cross the game would be turned off
            if event.type == QUIT or (event.type == KEYDOWN and event.type == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # if the user uses space or up key game would be started
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.type == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0,0))
                SCREEN.blit(GAME_SPRITES['player'], (playerx,playery))
                SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey))
                SCREEN.blit(GAME_SPRITES['base'], (basex,GROUNDY))
                pygame.display.update
                FPSCLOCK.tick(FPS)

if __name__ == "__main__":
    pygame.init() #initializing all pygame modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Batman')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('Num/1.jpg').convert_alpha(),
        pygame.image.load('Num/2.jpg').convert_alpha(),
        pygame.image.load('Num/3.jpg').convert_alpha(),
        pygame.image.load('Num/4.jpg').convert_alpha(),
        pygame.image.load('Num/5.jpg').convert_alpha(),
        pygame.image.load('Num/6.jpg').convert_alpha(),
        pygame.image.load('Num/7.jpg').convert_alpha(),
        pygame.image.load('Num/8.jpg').convert_alpha(),
        pygame.image.load('Num/9.jpg').convert_alpha(),
        pygame.image.load('Num/10.jpg').convert_alpha()
    )
   
while True:
    WelcomeScreen()
    # mainGame()

