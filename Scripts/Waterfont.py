import pygame
from pygame.locals import *

class Waterfont(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        #* load images
        self.sprites = []
        for i in range(1, 10):
            self.sprites.append(pygame.image.load(f"data/sprites/Scenary/Waterfont/font_{i}.png"))
        self.spriteIndex = 0
        #* set image
        self.image = self.sprites[self.spriteIndex]

        #* set rect
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

        #* set size
        self.size = size
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
    
    def update(self):
        self.spriteIndex += 0.15
        if self.spriteIndex >= len(self.sprites):
            self.spriteIndex = 0
        self.image = self.sprites[int(self.spriteIndex)]

        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
