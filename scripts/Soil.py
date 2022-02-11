import pygame
from pygame.locals import *


class Soil(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        pygame.sprite.Sprite.__init__(self)

        self.selected = False
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
        self.lastImage = self.image

        self.pos = pos
        

        #*set size
        self.size = size
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect(topleft = self.pos)
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], self.size, self.size)

    def ChangeState(self):
        if self.state == 0:
            self.image = self.dry[0]
        elif self.state == 1:
            self.image = self.prepared[0]
            self.lastImage = self.prepared[0]
            self.select()
        elif self.state == 2:
            print("planted")
            #add seed sprite
        elif self.state == 3:
            print("need water")
            #add water sprite
        self.Redraw()

    def Interact(self):
        if self.state == 0:
            self.state = 1
        elif self.state == 1:
            self.state = 2
        elif self.state == 3:
            self.state = 2
        self.ChangeState()

    def Select(self):
        if self.selected == False:
            self.lastImage = self.image.copy()
            color = pygame.Surface(self.image.get_size()).convert_alpha()
            color.fill(pygame.Color("#FFFFFFAA"))
            self.image.blit(color, (0, 0), special_flags=BLEND_RGBA_MULT)
            self.selected = True

    def Deselect(self):
        if self.selected == True:
            self.image = self.lastImage
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
            self.selected = False

    def Redraw(self):
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect(topleft = self.pos)
    

        

            
        
