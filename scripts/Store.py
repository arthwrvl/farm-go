import pygame 
from pygame.locals import *

class Store(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        #* load images
        self.sprite = pygame.image.load("data/sprites/scenary/Store/store_2.png")
        self.image = self.sprite

        #* set rect
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topright = self.x, self.y
        
        self.size = size
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
    
    def update(self):
        self.rect = self.image.get_rect()
        self.rect.topright = self.x, self.y
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
