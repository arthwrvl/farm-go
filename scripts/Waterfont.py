import pygame
from pygame.locals import *

from scripts.Can import Can

#TODO: fill water can on interact

class Waterfont(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups):
        pygame.sprite.Sprite.__init__(self, groups)
        #* load images
        self.sprites = []
        for i in range(1, 10):
            self.sprites.append(pygame.image.load(f"data/sprites/scenary/Waterfont/font_{i}.png"))
        self.spriteIndex = 0
        #* set image
        self.image = self.sprites[self.spriteIndex]

        #* set rect
        self.pos = pos
        self.rect = self.image.get_rect(topleft = pos)
        
        
        #* set size
        self.size = size
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], self.size/10*9, self.size/5*3)
        self.hitbox.topleft += pygame.Vector2(self.size*0.1, self.size/5)
        self.hitbox_interact = pygame.Rect(self.pos[0] - self.size*0.1, self.pos[1] - self.size*0.1, self.size*1.1, self.size*1.1)
    
    def update(self):
        self.spriteIndex += 0.1
        if self.spriteIndex >= len(self.sprites):
            self.spriteIndex = 0
        self.image = self.sprites[int(self.spriteIndex)]

        self.rect = self.image.get_rect(topleft = self.pos)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        
    def Interact(self, player):
        if isinstance(player.inventory.itens[player.inventory.selected].item, Can):
            if player.inventory.itens[player.inventory.selected].item.value < 10:
                player.inventory.itens[player.inventory.selected].item.value += 1
