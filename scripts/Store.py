import pygame 
from pygame.locals import *
from scripts.Button import Button
from scripts import Fruit
from scripts import Seed
from scripts.StoreItem import StoreItem
from scripts.constants import *


class Store(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups, screen):
        pygame.sprite.Sprite.__init__(self, groups)
        #* load images
        self.sprite = pygame.image.load("data/sprites/scenary/Store/store_2.png")
        self.image = self.sprite
        self.screen = screen
        #* set rect
        self.pos = pos
        self.close_button = Button("", (WIDTH - WIDTH/4*0.87, HEIGHT/4*0.63))
        self.open = False
        
        self.size = size
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]/10*8)
        self.hitbox_interact = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def Interact(self, player):
        if self.open == False:
            self.open = True
    
    def DrawStore(self, screen):
        background = pygame.image.load("data/sprites/store/background.png").convert_alpha()
        background = pygame.transform.scale(background, (int(150*SCALE), int(105*SCALE)))

        self.itens = self.LoadItens()

        text = get_font(int(10*SCALE)).render("Store", 1, "#48180e")
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/4*0.8))
        bgrect = background.get_rect(center = (WIDTH/2, HEIGHT/2))

        screen.blit(background, bgrect)
        screen.blit(background, bgrect)
        screen.blit(self.close_button.image, self.close_button.rect)
        screen.blit(text, text_rect)
        for i in range(0, 2):
            for j in range(0, 5):
                item_rect = pygame.Rect(self.itens[i*5+j].rect.left + 7*SCALE*j + (j*self.itens[i*5+j].rect.width), self.itens[i*5+j].rect.top + 4*SCALE*i + + (i*self.itens[i*5+j].rect.height), self.itens[i*5+j].rect.width, self.itens[i*5+j].rect.height)
                self.itens[i*5+j].rect = item_rect
                screen.blit(self.itens[i*5+j].image, item_rect)
                price = get_font(int(5*SCALE)).render("$ " + str(self.itens[i*5+j].seed.price), 1, "#48180e")
                name = get_font(int(4*SCALE)).render(str(self.itens[i*5+j].seed.fruit.name), 1, "#48180e")
                price_rect = price.get_rect(topleft=(item_rect.width/2 + item_rect.x - price.get_rect().width/2, item_rect.height/2 + item_rect.y + SCALE*11))
                name_rect = name.get_rect(topleft=(item_rect.width/2 + item_rect.x - name.get_rect().width/2, item_rect.height/2 + item_rect.y + SCALE*5))
                screen.blit(price, price_rect)
                screen.blit(name, name_rect)

    def LoadItens(self):
        itens = list()
        for i in range(0, Seed.seeds.__len__()):
            itens.append(StoreItem(Seed.seeds[i], (WIDTH/4*0.91, HEIGHT/4*1.08)))
            
        return itens


        
        



