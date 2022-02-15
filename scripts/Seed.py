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

