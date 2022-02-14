import pygame
from random import randint
from pygame.locals import *
from scripts.constants import *


class Fruit:
    fruits = [
        ["Apple", 20, pygame.image.load("data/sprites/itens/Fruit/apple.png"), 6],
        ["Avocado", 16, pygame.image.load("data/sprites/itens/Fruit/avocado.png"), 6],
        ["Banana", 12, pygame.image.load("data/sprites/itens/Fruit/banana.png"), 3],
        ["Blueberry", 30, pygame.image.load("data/sprites/itens/Fruit/blueberry.png"), 9],
        ["Carrot", 30, pygame.image.load("data/sprites/itens/Fruit/carrot.png"), 6],
        ["Lemon", 12, pygame.image.load("data/sprites/itens/Fruit/lemon.png"), 3],
        ["Orange", 28, pygame.image.load("data/sprites/itens/Fruit/orange.png"), 6],
        ["Papaya", 14, pygame.image.load("data/sprites/itens/Fruit/papaya.png"), 6],
        ["Plum", 45, pygame.image.load("data/sprites/itens/Fruit/plum.png"), 9],
        ["Potato", 50, pygame.image.load("data/sprites/itens/Fruit/potato.png"), 6]
    ]

    def __init__(self, name, shelf_life, img, sale_price):
        pygame.sprite.Sprite.__init__(self)

        self.name = name
        self.shelf_life = shelf_life
        self.img = img
        self.sale_price = sale_price
        self.fruits = [name, shelf_life, img, sale_price]
       
    @classmethod
    def random_fruit(cls):
        ID = randint(0, 9)
        name = cls.fruits[ID][0]
        shelf_life = cls.fruits[ID][1]
        img = cls.fruits[ID][2]
        sale_price = cls.fruits[ID][3]

        return cls(name, shelf_life, img, sale_price)

    @classmethod
    def sorted_fruit(cls, pos):
        name = cls.fruits[pos][0]
        shelf_life = cls.fruits[pos][1]
        img = cls.fruits[pos][2]
        sale_price = cls.fruits[pos][3]

        return cls(name, shelf_life, img, sale_price)

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

