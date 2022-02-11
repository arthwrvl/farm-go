import pygame
from pygame.locals import *
from sys import exit
from scripts import Soil
from scripts import Waterfont
from scripts import Player
from scripts import Store
from scripts import Trash



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
#endregion

class FarmGo:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
    
    def newGame(self):
        self.allSprites = pygame.sprite.Group()
        self.soils = self.drawGrid(int(SCALE * 16), int(WIDTH/7), int(HEIGHT/2.5))
        self.allSprites.add(self.soils)
        self.waterfont = Waterfont.Waterfont(int((WIDTH/8)*4.4), int(HEIGHT/4), int(SCALE * 64))
        self.allSprites.add(self.waterfont)
        self.player = Player.Player(int((WIDTH/2) - (PLAYER_WIDTH/2)), int((HEIGHT/2) - (PLAYER_WIDTH*1.5/2)), PLAYER_WIDTH, PLAYER_WIDTH/10)
        self.allSprites.add(self.player)
        self.store = Store.Store(int(WIDTH/2.185), 0, int(SCALE * 128))
        self.allSprites.add(self.store)
        self.trash = Trash.Trash(int(WIDTH/2), int(2*SCALE), int(SCALE * 32))
        self.allSprites.add(self.trash)
        self.run()
    
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.updateSprites()
            self.drawSprites()

    def checkSoilColision(self):
        self.soilColision = pygame.sprite.spritecollide(self.player, self.soils, False)
        if self.soilColision:
            if self.player.selectedSoil != {}:
                if self.player.selectedSoil != self.soilColision[len(self.soilColision) - 1]:
                    self.player.selectedSoil.deselect()
                    self.player.selectedSoil = self.soilColision[len(self.soilColision) - 1]
                    self.player.selectedSoil.select()
            else:
                self.player.selectedSoil = self.soilColision[len(self.soilColision) - 1]
                self.player.selectedSoil.select()          
        else:
            if self.player.selectedSoil != {}:
                self.player.selectedSoil.deselect()
                self.player.selectedSoil = {}

    def events(self):
        self.checkSoilColision()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.running:
                    self.running = False
                    pygame.quit()
                    exit()
            if event.type == KEYDOWN:
                if event.key == K_w:
                    self.player.vertical = -1
                elif event.key == K_s:
                    self.player.vertical = 1
                if event.key == K_a:
                    self.player.horizontal = -1
                elif event.key == K_d:
                    self.player.horizontal = 1
            if event.type == KEYUP:
                if event.key == K_w or event.key == K_s:
                    self.player.vertical = 0
                if event.key == K_a or event.key == K_d:
                    self.player.horizontal = 0
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.soilColision:
                        self.player.selectedSoil.interact()
    
    def updateSprites(self):
        self.allSprites.update()

    def drawSprites(self):
        self.screen.blit(BACKGROUND_IMAGE, (0, 0))
        self.allSprites.draw(self.screen)
        pygame.display.flip()

    def drawGrid(self, cellsize, width, height):
        soils = list()
        gap = int(cellsize/16)
        for i in range(4):
            for j in range(3):
                solo = Soil.Soil(width + i * cellsize + gap*i, height + j * cellsize + gap*j, cellsize)
                soils.append(solo)
        return soils

game = FarmGo()
game.newGame()


