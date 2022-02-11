import pygame

class Fence(pygame.sprite.Sprite):
    def __init__(self, pos, groups, size, path):
        pygame.sprite.Sprite.__init__(self, groups)
        self.image = pygame.image.load(f"data/sprites/scenary/Wall/{path}.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.size = size
        self.image = pygame.transform.scale(self.image, size)
    