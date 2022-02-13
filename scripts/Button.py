import pygame

from scripts.constants import SCALE

class Button:
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.image = pygame.image.load("data/sprites/store/close.png")
        self.image = pygame.transform.scale(self.image, (int(SCALE * 12), int(SCALE * 12)))
        self.rect = self.image.get_rect(topright = pos)

    def Interact(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        return False
