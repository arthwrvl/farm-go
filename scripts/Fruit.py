import pygame
from pygame.locals import *
from scripts.constants import *


class Fruit:
    def __init__(self, name, shelf_life, img, sale_price):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.shelf_life = shelf_life
        self.image = img
        self.sale_price = sale_price
        self.fruits = [name, shelf_life, img, sale_price]
       

    def show_img(self, screen, x, y):
        self.image = pygame.transform.scale(self.image, (int(SCALE * 12), int(SCALE * 12)))
        screen.blit(self.image, (x, y)) 

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

fruits = list()
fruits.append(Fruit("Apple", 20, pygame.image.load("data/sprites/itens/Fruit/apple.png"), 6))
fruits.append(Fruit("Avocado", 16, pygame.image.load("data/sprites/itens/Fruit/avocado.png"), 6))
fruits.append(Fruit("Banana", 12, pygame.image.load("data/sprites/itens/Fruit/banana.png"), 3))
fruits.append(Fruit("Blueberry", 30, pygame.image.load("data/sprites/itens/Fruit/blueberry.png"), 9))
fruits.append(Fruit("Carrot", 30, pygame.image.load("data/sprites/itens/Fruit/carrot.png"), 6))
fruits.append(Fruit("Lemon", 12, pygame.image.load("data/sprites/itens/Fruit/lemon.png"), 3))
fruits.append(Fruit("Orange", 28, pygame.image.load("data/sprites/itens/Fruit/orange.png"), 6))
fruits.append(Fruit("Papaya", 14, pygame.image.load("data/sprites/itens/Fruit/papaya.png"), 6))
fruits.append(Fruit("Plum", 45, pygame.image.load("data/sprites/itens/Fruit/plum.png"), 9))
fruits.append(Fruit("Potato", 50, pygame.image.load("data/sprites/itens/Fruit/potato.png"), 6))
