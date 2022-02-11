from email.mime import image
import imp
import pygame
from pygame.locals import *

pygame.init()
WIDTH = int(pygame.display.Info().current_w/2)
HEIGHT = int(pygame.display.Info().current_h/2)
SCALE = WIDTH/256

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
        self.screen = pygame.display.get_surface()

    def collision(self):
        self.rect_player = pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.image.get_width(), self.image.get_height()))
        self.rect_waterfont = pygame.draw.rect(self.screen, (0, 0, 0), (WIDTH * 0.59, HEIGHT * 0.30, SCALE * 40, SCALE * 38))
        self.rect_trash = pygame.draw.rect(self.screen, (0, 0, 0), (WIDTH * 0.35, HEIGHT * 0.15, SCALE * 35, SCALE * 6))

        # waterfont
        if (self.rect_player.colliderect(self.rect_waterfont) or self.rect_player.colliderect(self.rect_trash)) and self.horizontal > 0:
            self.horizontal = 0
            self.x -= 5
        elif (self.rect_player.colliderect(self.rect_waterfont) or self.rect_player.colliderect(self.rect_trash)) and self.horizontal < 0:
            self.horizontal = 0
            self.x += 5
        elif (self.rect_player.colliderect(self.rect_waterfont) or self.rect_player.colliderect(self.rect_trash)) and self.vertical > 0:
            self.vertical = 0
            self.y -= 5
        elif (self.rect_player.colliderect(self.rect_waterfont) or self.rect_player.colliderect(self.rect_trash)) and self.vertical < 0:
            self.vertical = 0
            self.y += 5

        # trash
        if self.rect_player.colliderect(self.rect_trash) and self.horizontal > 0:
            self.horizontal = 0
            self.x -= 5
        elif self.rect_player.colliderect(self.rect_trash) and self.horizontal < 0:
            self.horizontal = 0
            self.x += 5
        elif self.rect_player.colliderect(self.rect_trash) and self.vertical > 0:
            self.vertical = 0
            self.y -= 5
        elif self.rect_player.colliderect(self.rect_trash) and self.vertical < 0:
            self.vertical = 0
            self.y += 5

        # right
        if self.x >= WIDTH * 0.82:
            if self.horizontal > 0: 
                self.horizontal = 0
        # down
        if self.y >= HEIGHT * 0.68:
            if self.vertical > 0: 
                self.vertical = 0
        # left
        if self.x <= WIDTH * 0.08:
            if self.horizontal < 0: 
                self.horizontal = 0
        # up
        if self.y <= HEIGHT * 0.06:
            if self.vertical < 0: 
                self.vertical = 0

        return self.horizontal, self.vertical

    def update(self):
        self.horizontal, self.vertical = self.collision()

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