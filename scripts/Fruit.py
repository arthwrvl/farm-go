import pygame
from random import randint
from pygame.locals import *
from scripts.constants import *


class Fruit:
    fruits = [
        ["Apple", 20, pygame.image.load("data/sprites/itens/Fruit/apple.png")],
        ["Avocado", 16, pygame.image.load("data/sprites/itens/Fruit/avocado.png")],
        ["Banana", 12, pygame.image.load("data/sprites/itens/Fruit/banana.png")],
        ["Blueberry", 30, pygame.image.load("data/sprites/itens/Fruit/blueberry.png")],
        ["Carrot", 30, pygame.image.load("data/sprites/itens/Fruit/carrot.png")],
        ["Lemon", 12, pygame.image.load("data/sprites/itens/Fruit/lemon.png")],
        ["Orange", 28, pygame.image.load("data/sprites/itens/Fruit/orange.png")],
        ["Papaya", 14, pygame.image.load("data/sprites/itens/Fruit/papaya.png")],
        ["Plum", 45, pygame.image.load("data/sprites/itens/Fruit/plum.png")],
        ["Potato", 50, pygame.image.load("data/sprites/itens/Fruit/potato.png")],
    ]

    def __init__(self, name, shelf_life, img):
        pygame.sprite.Sprite.__init__(self)

        self.name = name
        self.shelf_life = shelf_life
        self.img = img
        self.fruits.append([name, shelf_life, img])
       
    @classmethod
    def random_fruit(cls):
        ID = randint(0, 9)
        name = cls.fruits[ID][0]
        shelf_life = cls.fruits[ID][1]
        img = cls.fruits[ID][2]

        return cls(name, shelf_life, img)

    def show_img(self, screen, x, y):
        self.img = pygame.transform.scale(self.img, (int(SCALE * 14), int(SCALE * 14)))
        screen.blit(self.img, (x, y)) 

    @property
    def shelf_life(self):
        return self._shelf_life

    @shelf_life.setter
    def shelf_life(self, value):
        value = int(value)
        
        if value < 10:
            value = 10
        elif value > 60:
            value = 60

        self._shelf_life = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        value = str(value).title()

        self._name = value

