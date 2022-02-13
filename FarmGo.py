#from asyncio import constants
import pygame
from pygame.locals import *
from sys import exit
from scripts import Soil
from scripts import Waterfont
from scripts import Player
from scripts import Store
from scripts import Trash
from scripts import Fence
from scripts import Order
from scripts.constants import *

pygame.init()


#TODO: create the UI


class FarmGo:
    BUTTON_PRESS_TIME = AUX_CURRENT_TIME = 0

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
    
    def newGame(self):
        #* all sprites that will be rendered
        self.allSprites = YsortGroup()
        #* Dedicated to colision
        self.collideSprites = pygame.sprite.Group()
        #* Dedicated to soil (cause it isn't affected by layer order)
        self.soilsSprite = pygame.sprite.Group()
        self.order = Order.Order()
        #* Draw Level
        self.soils = self.drawGrid(int(SCALE * 16), int(WIDTH/7), int(HEIGHT/2.5))
        self.soilsSprite.add(self.soils)
        self.waterfont = Waterfont.Waterfont((int((WIDTH/8)*4.6), int(HEIGHT/4)), int(SCALE * 50), [self.allSprites, self.collideSprites])
        self.store = Store.Store((14*SCALE, 0), (int(SCALE * 76), int(53*SCALE)), [self.allSprites, self.collideSprites], self.screen)
        
        self.trash = Trash.Trash((int(WIDTH/2), int(2*SCALE)), int(SCALE * 32), [self.allSprites, self.collideSprites])
        
        self.fence_right = Fence.Fence((int(WIDTH - 33*SCALE), int(44*SCALE)), [self.collideSprites, self.allSprites], (int(SCALE*8), int(91*SCALE)), "side", (int(SCALE*8), int(70*SCALE)), (0, 10*SCALE))
        self.fence_left = Fence.Fence((int(15*SCALE), int(44*SCALE)), [self.collideSprites, self.allSprites], (int(SCALE*8), int(91*SCALE)), "side_2", (int(SCALE*8), int(85*SCALE)), (0,0))
        self.fence_bottom = Fence.Fence((int(15*SCALE), int((HEIGHT - 21.5*SCALE))), [self.collideSprites, self.allSprites], (int(SCALE*128), int(22*SCALE)), "bottom", (int(SCALE*128), int(11*SCALE)), (0,11*SCALE))

        #* Draw Player
        self.player = Player.Player(int((WIDTH/2) - (PLAYER_WIDTH/2)), int((HEIGHT/2) - (PLAYER_WIDTH*1.5/2)), PLAYER_WIDTH, PLAYER_WIDTH/10, self.collideSprites, self.soils)
        self.allSprites.add(self.player)

        #self.soilsSprite.add(self.player)
        self.run()
    
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.updateSprites()
            self.drawSprites()


    def events(self):
        self.current_time = pygame.time.get_ticks() // 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.running:
                    self.running = False
                    pygame.quit()
                    exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.screen = pygame.display.set_mode((int(WIDTH/2), int(HEIGHT/2)))

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
                    if self.store.open == True:
                        self.store.open = not self.store.close_button.Interact()
                        print(self.store.open)
                    if self.player.selectedSoil != {}:
                        self.player.selectedSoil.Interact()
                    if self.player.select != {}:
                        self.player.select.Interact()
                if event.button == 2:
                    self.BUTTON_PRESS_TIME = pygame.time.get_ticks() // 1000
                    self.SEED_TIME = self.player.selectedSoil.seed.growing_time
                    print(self.SEED_TIME)
                if event.button == 3:
                    if self.player.selectedSoil != {}:
                        self.player.selectedSoil.ChangeSeed()
        
        if self.BUTTON_PRESS_TIME != 0:
            if self.current_time - self.BUTTON_PRESS_TIME >= self.SEED_TIME:
                if self.player.selectedSoil != {}:
                    self.player.selectedSoil.SaveSeed()         
                self.BUTTON_PRESS_TIME = 0  
    
    def updateSprites(self):
        self.allSprites.update()
        self.soilsSprite.update()
        

    def drawSprites(self):
        self.screen.blit(BACKGROUND_IMAGE, (0, 0))
        self.soilsSprite.draw(self.screen)
        #self.allSprites.draw(self.screen)
        self.allSprites.Custom_draw()

        print(self.store.open)
        if self.store.open == True:
            self.store.DrawStore(self.screen)

        self.order.NewOrder(self.AUX_CURRENT_TIME, self.screen)
        self.AUX_CURRENT_TIME = self.order.GetCurrentTime()
            
        #pygame.draw.rect(self.screen, (255, 0, 0), self.waterfont.hitbox_interact)
        #pygame.draw.rect(self.screen, (255, 0, 0), self.fence_bottom.hitbox)
        #pygame.draw.rect(self.screen, (255, 0, 0), self.fence_right.hitbox)
        #pygame.draw.rect(self.screen, (0, 255, 0), self.player.hitbox)
        #pygame.draw.rect(self.screen, (255, 0, 0), self.player.hitbox_soil)
        pygame.display.flip()

    def drawGrid(self, cellsize, width, height):
        soils = list()
        gap = int(cellsize/16)
        for i in range(4):
            for j in range(3):
                solo = Soil.Soil((width + i * cellsize + gap*i, height + j * cellsize + gap*j), cellsize)
                soils.append(solo)
        return soils
    


class YsortGroup(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.display_surface = pygame.display.get_surface()

    def Custom_draw(self):
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            self.display_surface.blit(sprite.image, sprite.rect)

game = FarmGo()
game.newGame()


