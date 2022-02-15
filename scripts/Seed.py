import pygame
from scripts import Fruit
from random import randint
from pygame.locals import *


class Seed:
    def __init__(self, index, price, growing_time):
        self.fruit = Fruit.fruits[index]
        self.name = self.fruit.name + " seed"
        self.price = price
        self.image = pygame.image.load(f"data/sprites/itens/Seed/seed_{index}.png")
        self.growing_time = growing_time
        #self.rect = self.image.get_rect(topleft = (0,0))
        #self.pos = Seed.pos
        #self.sorted_fruit = Fruit.Fruit.sorted_fruit(self.pos)
        #self.fruit = [self.sorted_fruit.name, self.sorted_fruit.shelf_life, self.sorted_fruit.img, self.sorted_fruit.sale_price]
        #self.growing_time = (growing_time + self.fruit[1]) // 2
        #self.price = (self.fruit[1] - self.growing_time) * 10
        #self.img = self.seeds[Fruit.Fruit.fruits.index([self.sorted_fruit.name, self.sorted_fruit.shelf_life, self.sorted_fruit.img, self.sorted_fruit.sale_price])]
    def show_image(self, screen, x, y):
        screen.blit(self.image, (x, y))

    def show_fruit(self, screen, x, y):
        screen.blit(self.fruit.image, (x, y))

seeds = list()
seeds.append(Seed(0, 2, 12))
seeds.append(Seed(1, 2, 10))
seeds.append(Seed(2, 1, 13))
seeds.append(Seed(3, 3, 15))
seeds.append(Seed(4, 2, 8))
seeds.append(Seed(5, 1, 13))
seeds.append(Seed(6, 2, 7))
seeds.append(Seed(7, 2, 11))
seeds.append(Seed(8, 3, 8))
seeds.append(Seed(9, 2, 11))



''' 
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
'''
