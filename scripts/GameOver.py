import pygame 
from pygame.locals import *
from scripts.constants import *


class GameOver:
    def __init__(self):
        pass

    def DrawGameOver(self, screen, score):
        background = pygame.image.load("data/sprites/store/background.png").convert_alpha()
        background = pygame.transform.scale(background, (int(150*SCALE), int(105*SCALE)))
        bgrect = background.get_rect(center = (WIDTH/2, HEIGHT/2))
        screen.blit(background, bgrect)

        text = get_font(int(10*SCALE)).render("Game Over", 1, "#48180e")
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/4*0.8))
        screen.blit(text, text_rect)

        text = get_font(int(8*SCALE)).render("Congratulations!", 1, "#48180e")
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT*0.45))
        screen.blit(text, text_rect)

        text = get_font(int(8*SCALE)).render(f"Your score: {str(score)}", 1, "#48180e")
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT*0.6))
        screen.blit(text, text_rect)

