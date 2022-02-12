import pygame 
from pygame.locals import *

#TODO: instantiate store screen (in progress)

class Store(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups, screen):
        pygame.sprite.Sprite.__init__(self, groups)
        #* load images
        self.sprite = pygame.image.load("data/sprites/scenary/Store/store_2.png")
        self.image = self.sprite
        self.screen = screen
        #* set rect
        self.pos = pos

        self.open = False

        
        self.size = size
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]/10*8)
        self.hitbox_interact = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def Interact(self):
        self.open = True
    
    def DrawStore(self, screen):
        background = pygame.Rect((screen.get_width()*0.1,screen.get_height()*0.1),(screen.get_width()*0.8, screen.get_height()*0.8))
        region = pygame.Rect((0,0), (background.width*0.98, background.height*0.85))
        region.midbottom = background.midbottom + pygame.Vector2(0, -background.height*0.02)
        pygame.draw.rect(screen, (152,139,93), background, border_radius=20)
        pygame.draw.rect(screen, (68,62,36), region, border_radius=20)


        
        



