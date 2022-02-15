import pygame
class Can:
    def __init__(self):
        self.images = list()
        self.images.append(pygame.image.load("data/sprites/itens/can/empty.png").convert_alpha())
        self.images.append(pygame.image.load("data/sprites/itens/can/full.png").convert_alpha())
        self.maxvalue = 10
        self.value = 2

        if self.value > 0:
            self.image = self.images[1]
        else:
            self.image = self.images[0]
    
    def use(self):
        if self.value > 0:
            self.value -= 1
            return True

    