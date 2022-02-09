import pygame
from pygame.locals import *
from sys import exit
from Scripts import Soil
from Scripts import Waterfont

pygame.init()

#* draw soil grid on screen
def drawGrid(cellsize, width, height):
    soils = list()
    gap = int(cellsize/16)
    for i in range(4):
        for j in range(3):
            solo = Soil.Soil(width + i * cellsize + gap*i, height + j * cellsize + gap*j, cellsize)
            print(solo.rect.topleft)
            soils.append(solo)
    return soils

#!get screen size
height = pygame.display.Info().current_h
width = pygame.display.Info().current_w

#* set background image scale
bgimg = pygame.image.load("data/sprites/scenary/background.png")
bgimg = pygame.transform.scale(bgimg, (width, height))

#* set display
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Farm Go")

all_sprites = pygame.sprite.Group()

#* draw soil grid proportionally to screen size
soils = drawGrid(int(width/256) * 16, int(width/7), int(height/2.5))
all_sprites.add(soils)

#* set Waterfont
waterfont = Waterfont.Waterfont(int((width/8)*4.4), int(height/4), int(width/256) * 64)
all_sprites.add(waterfont)

clock = pygame.time.Clock()

#! main loop
while True:
    clock.tick(60)
    print(clock.get_fps())
    screen.blit(bgimg, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.update()


