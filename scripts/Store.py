import pygame 
from pygame.locals import *

class Store(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups):
        pygame.sprite.Sprite.__init__(self, groups)
        #* load images
        self.sprite = pygame.image.load("data/sprites/scenary/Store/store_2.png")
        self.image = self.sprite

        #* set rect
        self.pos = pos

        
        self.size = size
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]/10*8)
