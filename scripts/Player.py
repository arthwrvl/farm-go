from email.mime import image
import imp
from msilib.schema import Directory
import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, size, speed, obstacles, soils):
        pygame.sprite.Sprite.__init__(self)
        #* load images
        self.sprites = []
        self.sprites.append(pygame.image.load("data/sprites/player/player_placeholder.png"))
        self.image = self.sprites[0]
        self.obstacles = obstacles
        self.x = x
        self.y = y

        self.soils = soils


        #* set movement
        self.direction = pygame.math.Vector2(0, 0)
        #self.vertical = 0
        #self.horizontal = 0
        self.speed = speed
        self.selectedSoil = {}
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

        self.size = size
        self.image = pygame.transform.scale(self.image, (self.size, int(self.size * 1.5)))
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, int(self.size/3*2), self.size/5*3)
        self.hitbox_soil = pygame.Rect(self.rect.x, self.rect.y, int(self.size/3*2)/2, self.size/5*3/2)
        self.SyncHitbox()

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[K_RIGHT]:
            self.direction.x = 1
        elif keys[K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[K_UP]:
            self.direction.y = -1
        elif keys[K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
    
    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            print(self.direction)
            self.hitbox.x += self.direction.x * self.speed
            self.collision('horizontal')
            self.hitbox.y += self.direction.y * self.speed
            self.collision('vertical')
            self.SyncHitbox()
            self.CheckSoilCollision()

    def SyncHitbox(self):
        self.rect.centerx = self.hitbox.centerx
        self.rect.topleft = self.hitbox.topleft + pygame.Vector2(-self.size/6, -self.size/6*5.2)
        self.hitbox_soil.center = self.hitbox.center + pygame.Vector2(0, self.size/10)
    def CheckSoilCollision(self):
        for sprite in self.soils:
            if sprite.hitbox.colliderect(self.hitbox_soil):
                print("Colision")
                print(self.selectedSoil)
                if self.selectedSoil != {}:
                    if self.selectedSoil != sprite:
                        self.selectedSoil.Deselect()
                        self.selectedSoil = sprite
                        self.selectedSoil.Select()
                        break
                else:
                    self.selectedSoil = sprite
                    self.selectedSoil.Select()    
                    break      
            else:
                if self.selectedSoil != {}:
                    self.selectedSoil.Deselect()
                    self.selectedSoil = {}


    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacles:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        print("colision right")
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
                        print("colision left")
        
        if direction == 'vertical':
            for sprite in self.obstacles:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                        print("colision down")
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                        print("colision up")

    def update(self):
        self.input()
        self.move()