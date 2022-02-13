import pygame

from scripts.constants import *

class StoreItem:
    def __init__(self, name, price, pos):
        self.name = name
        self.price = price
        self.image = pygame.image.load(f"data/sprites/store/itens/{name}.png")
        self.image = pygame.transform.scale(self.image, (int(SCALE * 22), int(SCALE * 34)))
        self.pos = pos
        self.rect = self.image.get_rect(topleft = pos)