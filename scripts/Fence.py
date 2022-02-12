import pygame

class Fence(pygame.sprite.Sprite):
    def __init__(self, pos, groups, size, path, hitbox, hitbox_pos):
        pygame.sprite.Sprite.__init__(self, groups)
        self.image = pygame.image.load(f"data/sprites/scenary/Wall/{path}.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.size = size
        self.image = pygame.transform.scale(self.image, size)
        self.hitbox = pygame.Rect(pos[0] + hitbox_pos[0], pos[1] + hitbox_pos[1], hitbox[0], hitbox[1])
        self.hitbox_interact = pygame.Rect(pos[0] + hitbox_pos[0], pos[1] + hitbox_pos[1], hitbox[0], hitbox[1])
    