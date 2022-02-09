import pygame, Fruit
from random import randint
from pygame.locals import *


class Seed:
    def __init__(self, growing_time):
        fruit = Fruit.Fruit.random_fruit()
        self.fruit = [fruit.name, fruit.shelf_life, fruit.img]
        self.growing_time = (growing_time + self.fruit[1]) // 2
        self.price = (self.fruit[1] - self.growing_time) * 10

    @classmethod
    def random_growing_time(cls):
        growing_time = randint(10, 30)

        return cls(growing_time)

    @property
    def growing_time(self):
        return self._growing_time

    @growing_time.setter
    def growing_time(self, value):
        value = int(value)

        if value < 10:
            value = 10
        elif value > 30:
            value = 30

        self._growing_time = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = float(value.replace("R$", ""))

        if value < 50:
            value = 50
        elif value > 200:
            value = 200

        self._price = value

