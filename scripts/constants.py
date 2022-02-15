import pygame
import pygame.freetype

pygame.init()
pygame.font.init()

#region Constants
WIDTH = int(pygame.display.Info().current_w/2)
HEIGHT = int(pygame.display.Info().current_h/2)
TITLE = "Farm Go"
FPS = 60
BACKGROUND_IMAGE = pygame.image.load("data/sprites/scenary/background.png")
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))
SCALE = WIDTH/256
PLAYER_WIDTH = int(SCALE * 16)

def get_font(size):
    return pygame.font.Font("data/fonts/pixelated.ttf", size)
def get_second_font(size):
    return pygame.font.Font("data/fonts/game_over.ttf", size)

