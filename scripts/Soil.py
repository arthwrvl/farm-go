import pygame
from pygame.locals import *


class Soil(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)

        #*load images
        self.dry = []
        self.prepared = []
        for i in range(1,4):
            self.dry.append(pygame.image.load(f"data/sprites/scenary/Soil/dry/{i}.png"))
            self.prepared.append(pygame.image.load(f"data/sprites/scenary/Soil/prepared/{i}.png"))

        #*set state
        self.state = 0 # 0 = dry, 1 = prepared, 2 = planted, 3 = need water

        #*set image
        self.image = self.dry[0]

        #*set rect
        self.x = x
        self.y = y

        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

        #*set size
        self.size = size
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def ChangeState(self):
        if self.state == 0:
            self.image = self.dry[0]
        elif self.state == 1:
            self.image = self.prepared[0]
        elif self.state == 2:
            print("planted")
            #add seed sprite
        elif self.state == 3:
            print("need water")
            #add water sprite
        self.update()

    def interact(self):
        if self.state == 0:
            self.state = 1
        elif self.state == 1:
            self.state = 2
        elif self.state == 3:
            self.state = 2
        self.ChangeState()

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
    

        

            
        
