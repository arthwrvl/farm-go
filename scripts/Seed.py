import pygame
from scripts import Fruit
from random import randint
from pygame.locals import *


class Seed:
    seeds = [
        pygame.image.load(f"data/sprites/itens/Seed/seed_{i}.png")
        for i in range(len(Fruit.Fruit.fruits))
    ]

    def __init__(self, growing_time):
        self.random_fruit = Fruit.Fruit.random_fruit()
        self.fruit = [self.random_fruit.name, self.random_fruit.shelf_life, self.random_fruit.img]
        self.growing_time = (growing_time + self.fruit[1]) // 2
        self.price = (self.fruit[1] - self.growing_time) * 10
        self.img = self.seeds[Fruit.Fruit.fruits.index([self.random_fruit.name, self.random_fruit.shelf_life, self.random_fruit.img])]
        
    @classmethod
    def random_growing_time(cls):
        growing_time = randint(5, 15)

        return cls(growing_time)

    def show_img(self, screen, x, y):
        screen.blit(self.img, (x, y))

    def show_img_fruit(self, screen, x, y):
        self.random_fruit.show_img(screen, x, y)

    @property
    def growing_time(self):
        return self._growing_time

    @growing_time.setter
    def growing_time(self, value):
        value = int(value)

        if value < 5:
            value = 5
        elif value > 15:
            value = 15

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

