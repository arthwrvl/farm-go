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
from scripts import Fruit
from scripts.Can import Can
from scripts.Hoe import Hoe
from scripts.Inventory import Inventory
from scripts.Slot import Slot
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
        #self.order = Order.Order()
        #* Draw Level
        self.soils = self.drawGrid(int(SCALE * 16), int(WIDTH/7), int(HEIGHT/2.2))
        self.soilsSprite.add(self.soils)
        self.waterfont = Waterfont.Waterfont((int((WIDTH/8)*4.6), int(HEIGHT/4)), int(SCALE * 50), [self.allSprites, self.collideSprites])
        self.store = Store.Store((14*SCALE, 0), (int(SCALE * 76), int(53*SCALE)), [self.allSprites, self.collideSprites], self.screen)
        
        self.trash = Trash.Trash((int(WIDTH/2), int(2*SCALE)), int(SCALE * 32), [self.allSprites, self.collideSprites])
        
        self.fence_right = Fence.Fence((int(WIDTH - 33*SCALE), int(44*SCALE)), [self.collideSprites, self.allSprites], (int(SCALE*8), int(91*SCALE)), "side", (int(SCALE*8), int(70*SCALE)), (0, 10*SCALE))
        self.fence_left = Fence.Fence((int(15*SCALE), int(44*SCALE)), [self.collideSprites, self.allSprites], (int(SCALE*8), int(91*SCALE)), "side_2", (int(SCALE*8), int(85*SCALE)), (0,0))
        self.fence_bottom = Fence.Fence((int(15*SCALE), int((HEIGHT - 21.5*SCALE))), [self.collideSprites, self.allSprites], (int(SCALE*128), int(22*SCALE)), "bottom", (int(SCALE*128), int(11*SCALE)), (0,11*SCALE))

        inventory = Inventory(5, (WIDTH*0.73, HEIGHT*0.86), 12)
        hoe = Hoe()
        can = Can()
        inventory.addItem(hoe)
        inventory.addItem(can)
        self.soiltoremove = None
        self.growing_seeds = list()
        self.seeds_time = list()
        self.planted_time = list()


        #* Draw Player
        self.player = Player.Player(int((WIDTH/2) - (PLAYER_WIDTH/2)), int((HEIGHT/2) - (PLAYER_WIDTH*1.5/2)), PLAYER_WIDTH, PLAYER_WIDTH/10, self.collideSprites, self.soils, inventory)
        self.allSprites.add(self.player)

        #self.soilsSprite.add(self.player)
        self.run()
    
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.updateSprites()
            self.drawSprites()
            self.events()

    def events(self):
        self.current_time = pygame.time.get_ticks() // 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.running:
                    self.running = False
                    pygame.quit()
                    exit()
            if event.type == KEYDOWN:    
                if event.key == K_1 or event.key == K_KP_1:
                    self.player.inventory.selected = 0
                elif event.key == K_2 or event.key == K_KP_2:
                    self.player.inventory.selected = 1
                elif event.key == K_3 or event.key == K_KP_3:
                    self.player.inventory.selected = 2
                elif event.key == K_4 or event.key == K_KP_4:
                    self.player.inventory.selected = 3
                elif event.key == K_5 or event.key == K_KP_5:
                    self.player.inventory.selected = 4
            if event.type == KEYUP:
                if event.key == K_w or event.key == K_s:
                    self.player.vertical = 0
                if event.key == K_a or event.key == K_d:
                    self.player.horizontal = 0
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.BUTTON_PRESS_TIME = pygame.time.get_ticks()
                    if self.player.selectedSoil != {}:
                        if self.player.selectedSoil.state == 4:
                            print("clicked on state 4")
                            self.soiltoremove = self.player.selectedSoil
                        self.player.selectedSoil.Interact(self.player, self.screen)
                        if self.player.selectedSoil.state == 3:
                            self.growing_seeds.append(self.player.selectedSoil)
                            self.seeds_time.append(self.player.selectedSoil.seed.growing_time)
                            self.planted_time.append(pygame.time.get_ticks() // 1000)

                        break
                    if self.player.select != {}:
                        self.player.select.Interact(self.player)
                        break
                if event.button == 2:
                    if self.player.selectedSoil != {}:
                        print("planted")
                        self.BUTTON_PRESS_TIME = pygame.time.get_ticks() // 1000
                        self.SEED_TIME = self.player.selectedSoil.seed.growing_time
                        print(f"SEED TIME = {self.SEED_TIME}")
                if event.button == 3:
                    if self.player.selectedSoil != {}:
                        self.player.selectedSoil.ChangeSeed()
                if event.button == 4:
                    if self.player.inventory.selected < 4:
                        self.player.inventory.selected += 1
                    else:
                        self.player.inventory.selected = 0
                if event.button == 5:
                    if self.player.inventory.selected > 0:
                        self.player.inventory.selected -= 1
                    else:
                        self.player.inventory.selected = 4
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    if self.store.open == True:
                        self.store.open = not self.store.close_button.Interact()
                        for i in self.store.itens:
                            i.interact(self.player)
                            #self.player.inventory.add(i)
        
        if self.soiltoremove != None:
            print("tem")
            print(len(self.growing_seeds))
            for i in range(0, len(self.growing_seeds)):
                if self.soiltoremove == self.growing_seeds[i]:
                    print("removendo")
                    self.growing_seeds.pop(i)
                    self.seeds_time.pop(i)
                    self.planted_time.pop(i)
                    self.soiltoremove = None
                    break
        for i in range(0, len(self.growing_seeds)):
            #print(str(self.current_time - self.planted_time[i]) + " " + str(self.seeds_time[i]))
            if self.current_time - self.planted_time[i] > self.seeds_time[i] * 2:
                if self.growing_seeds[i].state != 0:
                    self.growing_seeds[i].bad_fruit()
            elif self.current_time - self.planted_time[i] > self.seeds_time[i]:
                if self.growing_seeds[i].state != 0:
                    self.growing_seeds[i].grow_seed()
    #
    def updateSprites(self):
        self.allSprites.update()
        self.soilsSprite.update(self.screen)

    def drawSprites(self):
        self.screen.blit(BACKGROUND_IMAGE, (0, 0))
        self.soilsSprite.draw(self.screen)
        for i in self.soilsSprite:
            i.overdraw(self.screen)
        #self.allSprites.draw(self.screen)
        self.allSprites.Custom_draw()
        self.player.inventory.drawInventory(self.screen)
        #print(self.store.open)
        if self.store.open == True:
            self.store.DrawStore(self.screen)

        #self.order.NewOrder(self.AUX_CURRENT_TIME, self.screen)
        #self.AUX_CURRENT_TIME = self.order.GetCurrentTime()
        #self.order.CheckOrderCollision(self.player.hitbox, self.player)
            
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


