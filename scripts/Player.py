import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, size, speed):
        pygame.sprite.Sprite.__init__(self)
        #* load images
        self.sprites = []
        self.sprites.append(pygame.image.load("data/sprites/player/player_placeholder.png"))
        self.image = self.sprites[0]
        
        self.x = x
        self.y = y

        #* set movement
        self.vertical = 0
        self.horizontal = 0
        self.speed = speed
        self.selectedSoil = {}

        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

        self.size = size
        self.image = pygame.transform.scale(self.image, (self.size, int(self.size * 1.5)))

    def update(self):
        #* filter diagonal movement
        if self.horizontal != 0 and self.vertical != 0:
            if self.vertical > 0:
                self.vertical = 0.7
            else:
                self.vertical = -0.7
            if self.horizontal > 0:
                self.horizontal = 0.7
            else:
                self.horizontal = -0.7
        else:
            if self.vertical > 0 and self.vertical < 1:
                self.vertical = 1
            elif self.vertical < 0 and self.vertical > -1:
                self.vertical = -1
            if self.horizontal > 0 and self.horizontal < 1:
                self.horizontal = 1
            elif self.horizontal < 0 and self.horizontal > -1:
                self.horizontal = -1



        self.rect = self.image.get_rect()
        #* move
        self.x += self.horizontal * self.speed
        self.y += self.vertical * self.speed

        self.rect.topleft = self.x, self.y
        self.image = pygame.transform.scale(self.image, (self.size, int(self.size * 1.5)))
