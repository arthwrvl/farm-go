import pygame 
from pygame.locals import *
from scripts.constants import *


class Info:
    def __init__(self):
        pass

    def DrawScore(self, screen, score):
        background_image = pygame.image.load("data/sprites/Order/order.png")
        background_image = pygame.transform.scale(background_image, (int(30*SCALE), int(17*SCALE)))
        bgrect = background_image.get_rect(topright = (WIDTH * 0.88, HEIGHT * 0.01))
        screen.blit(background_image, bgrect)

        title = get_font(int(4*SCALE)).render("Score", 1, "#48180e")
        title_rect = title.get_rect(center=(WIDTH - bgrect.width * 1.53, bgrect.y + 4*SCALE))
        screen.blit(title, title_rect)

        text = get_font(int(9*SCALE)).render(str(score), 1, "#48180e")
        text_rect = text.get_rect(center=(WIDTH - bgrect.width * 1.53, bgrect.y + 10*SCALE))
        screen.blit(text, text_rect)
        
        
    def DrawMoney(self, screen, money):
        background_image = pygame.image.load("data/sprites/Order/order.png")
        background_image = pygame.transform.scale(background_image, (int(30*SCALE), int(17*SCALE)))
        bgrect = background_image.get_rect(topright = (WIDTH * 0.76, HEIGHT * 0.01))
        screen.blit(background_image, bgrect)

        title = get_font(int(4*SCALE)).render("Money", 1, "#48180e")
        title_rect = title.get_rect(center=(WIDTH - bgrect.width * 2.56, bgrect.y + 4*SCALE))
        screen.blit(title, title_rect)

        text = get_font(int(9*SCALE)).render("$ " + str(money), 1, "#48180e")
        text_rect = text.get_rect(center=(WIDTH - bgrect.width * 2.56, bgrect.y + 10*SCALE))
        screen.blit(text, text_rect)

    def DrawTime(self, screen, time):
        if time >= 240:
            time = 240

        background_image = pygame.image.load("data/sprites/Order/order.png")
        background_image = pygame.transform.scale(background_image, (int(30*SCALE), int(17*SCALE)))
        bgrect = background_image.get_rect(topright = (WIDTH, HEIGHT * 0.01))
        screen.blit(background_image, bgrect)

        title = get_font(int(4*SCALE)).render("Time", 1, "#48180e")
        title_rect = title.get_rect(center=(WIDTH - bgrect.width * 0.5, bgrect.y + 4*SCALE))
        screen.blit(title, title_rect)

        text = get_font(int(9*SCALE)).render(str(time), 1, "#48180e")
        text_rect = text.get_rect(center=(WIDTH - bgrect.width * 0.5, bgrect.y + 10*SCALE))
        screen.blit(text, text_rect)

        