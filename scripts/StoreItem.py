from tkinter.tix import Select
import pygame

from scripts.constants import *

class StoreItem:
    def __init__(self, seed, pos):
        self.seed = seed
        self.image = pygame.image.load(f"data/sprites/store/itens/{self.seed.fruit.name}.png")
        self.image = pygame.transform.scale(self.image, (int(SCALE * 22), int(SCALE * 34)))
        self.pos = pos
        self.rect = self.image.get_rect(topleft = pos)
    
    
    def interact(self, player):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and self.seed.price <= player.money:
            player.inventory.addItem(self.seed)
            print("bought " + self.seed.fruit.name)
            player.money -= self.seed.price
            return True
