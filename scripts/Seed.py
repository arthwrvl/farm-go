import pygame
from scripts import Fruit
from random import randint
from pygame.locals import *


class Seed:
    pos = -1
    seeds = [
        pygame.image.load(f"data/sprites/itens/Seed/seed_{i}.png")
        for i in range(len(Fruit.Fruit.fruits))
    ]
    picked_fruits = {}

    def __init__(self, growing_time):
        self.pos = Seed.pos
        self.sorted_fruit = Fruit.Fruit.sorted_fruit(self.pos)
        self.fruit = [self.sorted_fruit.name, self.sorted_fruit.shelf_life, self.sorted_fruit.img, self.sorted_fruit.sale_price]
        self.growing_time = (growing_time + self.fruit[1]) // 2
        self.price = (self.fruit[1] - self.growing_time) * 10
        self.img = self.seeds[Fruit.Fruit.fruits.index([self.sorted_fruit.name, self.sorted_fruit.shelf_life, self.sorted_fruit.img, self.sorted_fruit.sale_price])]
        
    @classmethod
    def random_growing_time(cls):
        growing_time = randint(5, 10)

        if cls.pos < len(Fruit.Fruit.fruits) - 1:
            #print(cls.pos)
            cls.pos += 1
        else:
            #print(cls.pos)
            cls.pos = 0

        return cls(growing_time)

    def show_img(self, screen, x, y):
        screen.blit(self.img, (x, y))

    def show_img_fruit(self, screen, x, y):
        self.sorted_fruit.show_img(screen, x, y)

    @property
    def growing_time(self):
        return self._growing_time

    @growing_time.setter
    def growing_time(self, value):
        value = int(value)

        if value < 5:
            value = 5
        elif value > 10:
            value = 10

        self._growing_time = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = int(value.replace("R$", ""))

        if value < 50:
            value = 50
        elif value > 200:
            value = 200

        self._price = value

