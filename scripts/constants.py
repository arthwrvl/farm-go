import pygame

pygame.init()
#region Constants
WIDTH = int(pygame.display.Info().current_w/2)
HEIGHT = int(pygame.display.Info().current_h/2)
TITLE = "Farm Go"
FPS = 60
BACKGROUND_IMAGE = pygame.image.load("data/sprites/scenary/background.png")
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))
SCALE = WIDTH/256
PLAYER_WIDTH = int(SCALE * 16)