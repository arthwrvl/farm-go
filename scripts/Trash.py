import pygame 
from pygame.locals import *

#TODO: make player be able to throw Hortifrutti here

class Trash(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups):
        pygame.sprite.Sprite.__init__(self, groups)
        #* load images
        self.sprite = pygame.image.load("data/sprites/scenary/Trash/trashcan.png")
        self.image = self.sprite

        #* set rect
        self.pos = pos    
        self.size = size
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect(topright = self.pos)
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], self.size*0.9, self.size*0.7)
        self.hitbox_interact = pygame.Rect(self.pos[0], self.pos[1], self.size*0.9, self.size*0.8)
        self.hitbox_interact.topright = self.pos
        self.hitbox.topright = self.pos
    def Interact(self, player):
        if player.inventory.selected != 0 and player.inventory.selected != 1:
            player.inventory.removeItembyIndex(player.inventory.selected)
    
